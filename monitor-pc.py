# -*- coding: utf-8 -*-
#
# Requirements: prometheus_client
#

import sys

import prometheus_client as pc

from collections import OrderedDict

from fs725 import FS725Instrument, fs725_commands


PROMETHEUS_GW = "aux:9091"


def print_fs725_metrics(com_port, query_sel):
    """Print metrics of FS725 Rb Frequency Standard in Prometheus format

    Parameters
    ----------
    com_port : str
        Path to device to talk to FS725.
    query_sel : list of strings
        Selection of commands to query.
    """

    # Set up Prometheus client registry
    prom_registry = pc.CollectorRegistry()

    # Connect to FS725
    fs725 = FS725Instrument(com_port)

    if fs725.isConnected is True:

        if query_sel == ["all"]:
            # Select all commands
            queries = fs725_commands
        else:
            # Check if selected commands are valid
            for k in query_sel:
                if k not in fs725_commands:
                    raise KeyError(f"Command '{k}' not found.")
            # Select commands to query
            queries = OrderedDict((k, fs725_commands[k]) for k in query_sel)

        # Do the actual queries and add metrics to Prometheus registry
        for query in queries.values():
            make_query_and_add(fs725, query, prom_registry)

        # Close connection to FS725
        fs725.close()

    # Add connection state metric
    prom_connected = pc.Gauge(
        "fs725_serial_connection_state",
        "Whether serial connection to the FS725 is up",
        registry=prom_registry,
    )
    prom_connected.set(int(fs725.isConnected))

    # Add timestamp
    prom_timestamp = pc.Gauge(
        "fs725_last_success_unixtime",
        "Timestamp from FS725 monitoring script",
        registry=prom_registry,
    )
    prom_timestamp.set_to_current_time()

    # Push Prometheus metrics
    pc.push_to_gateway(PROMETHEUS_GW, job="FS725", registry=prom_registry)


def make_query_and_add(fs725, query, prom_registry):
    """Make a single query to the FS725 and add metric to Prometheus registry."""

    metric_name = "fs725_" + query.description.lower().replace(" ", "_")

    value = fs725.getCurrentValue(query.mnem)

    if type(query.rtn_type) == type:
        prom_metric = pc.Gauge(metric_name, query.description, registry=prom_registry)
        prom_metric.set(query.rtn_type(value))
    else:
        split_values = value.split(",")
        for ival, val in enumerate(split_values):
            metric_name = f"{metric_name}{ival + 1}"
            description = f"{query.description} {ival + 1}"
            prom_metric = pc.Gauge(metric_name, description, registry=prom_registry)
            prom_metric.set(query.rtn_type[ival](val))


if __name__ == "__main__":
    com_port = "/dev/ttyUSB0"
    query_sel = sys.argv[1:] if len(sys.argv) > 1 else ["sf"]
    sys.exit(print_fs725_metrics(com_port=com_port, query_sel=query_sel))
