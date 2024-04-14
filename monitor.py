# -*- coding: utf-8 -*-
#
# Requirement: pyserial
#

import sys

from collections import OrderedDict

from fs725 import FS725Instrument
from commands import fs725_commands


COM_PORT = "/dev/ttyUSB0"


def print_fs725_metrics(com_port, query_sel):
    """Print metrics of FS725 Rb Frequency Standard in Prometheus format

    Parameters
    ----------
    com_port : str
        Path to device to talk to FS725.
    query_sel : list of strings
        Selection of commands to query.
    """

    # Connect to FS725 and print connection state metric
    fs725 = FS725Instrument(com_port)
    print_connected_metric(state=fs725.isConnected)

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

        # Do the actual queries and print the resulting metrics
        for query in queries.values():
            make_query_and_print(fs725, query)

        # Close connection to FS725
        fs725.close()


def make_query_and_print(fs725, query):
    """Make a single query to the FS725 and print the resulting metric."""

    metric_name = f"fs725_{query.mnem}"

    value = fs725.getCurrentValue(query.mnem)

    if isinstance(query.rtn_type, type):
        print_metric(
            metric_name=metric_name,
            value=query.rtn_type(value),
            description=f"{query.description}",
        )
    else:
        split_values = value.split(",")
        for ival, val in enumerate(split_values):
            print_metric(
                metric_name=f"{metric_name}_{ival + 1}",
                value=query.rtn_type[ival](val),
                description=f"{query.description}: {ival + 1}",
            )


def print_connected_metric(state):
    """Print metric to indicate whether the FS725 is up and connected."""

    print_metric(
        metric_name="fs725_serial_connection_state",
        value=int(state),
        description="Whether serial connection to the FS725 is up",
    )


def print_metric(metric_name, value, description):
    """Print metric in text-based exposition format for Prometheus."""

    print(f"# HELP {metric_name} {description}")
    print(f"# TYPE {metric_name} gauge")
    print(f"{metric_name} {value}")


if __name__ == "__main__":
    query_sel = sys.argv[1:] if len(sys.argv) > 1 else ["all"]
    sys.exit(print_fs725_metrics(com_port=COM_PORT, query_sel=query_sel))
