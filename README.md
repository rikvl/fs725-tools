# FS725 tools

A Python interface for the SRS [FS725](https://www.thinksrs.com/products/fs725.html) rubidium frequency standard.

The script `monitor.py` queries metrics from the FS725 and writes them out is a format appropriate for Prometheus.
It can be used together with [script_exporter](https://github.com/ricoberger/script_exporter).
