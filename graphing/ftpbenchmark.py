# -*- encoding: utf-8 -*-

from cmk.graphing.v1 import metrics, Title, graphs

UNIT_NUMBER = metrics.Unit(metrics.DecimalNotation(""), metrics.StrictPrecision(0))

metric_a = metrics.Metric(
    name="download_average_duration",
    title=Title("Average seconds per download"),
    unit=metrics.Unit(notation=metrics.DecimalNotation("s")),
    color=metrics.Color.DARK_GREEN
)

metric_b = metrics.Metric(
    name="download_digest_errors",
    title=Title("Corrupted files after download"),
    unit=UNIT_NUMBER,
    color=metrics.Color.DARK_YELLOW
)

metric_c = metrics.Metric(
    name="download_errors",
    title=Title("Error responses during uploads"),
    unit=UNIT_NUMBER,
    color=metrics.Color.LIGHT_RED
)

metric_d = metrics.Metric(
    name="download_exceptions",
    title=Title("Exceptions thrown during uploads"),
    unit=UNIT_NUMBER,
    color=metrics.Color.DARK_RED
)

metric_e = metrics.Metric(
    name="download_timeouts",
    title=Title("Timeouts during downloads"),
    unit=UNIT_NUMBER,
    color=metrics.Color.LIGHT_ORANGE
)

metric_g = metrics.Metric(
    name="upload_errors",
    title=Title("Error responses during uploads"),
    unit=UNIT_NUMBER,
    color=metrics.Color.LIGHT_RED
)

metric_h = metrics.Metric(
    name="upload_exceptions",
    title=Title("Exceptions thrown during uploads"),
    unit=UNIT_NUMBER,
    color=metrics.Color.DARK_RED
)

metric_i = metrics.Metric(
    name="upload_timeouts",
    title=Title("Timeouts during uploads"),
    unit=UNIT_NUMBER,
    color=metrics.Color.LIGHT_ORANGE
)

graph_a = graphs.Graph(
    name="download_errors_combined",
    title=Title("Errors during download benchmarking"),
    simple_lines=[
        "download_digest_errors",
        "download_errors",
        "download_exceptions",
        "download_timeouts"
    ]
)

graph_b = graphs.Graph(
    name="upload_errors_combined",
    title=Title("Errors during upload benchmarking"),
    simple_lines=[
        "download_digest_errors",
        "download_errors",
        "download_exceptions",
        "download_timeouts"
    ]
)
