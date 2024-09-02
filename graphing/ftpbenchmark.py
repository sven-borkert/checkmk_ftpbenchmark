# -*- encoding: utf-8 -*-

from cmk.graphing.v1 import metrics, Title, graphs

UNIT_NUMBER = metrics.Unit(metrics.DecimalNotation(""), metrics.StrictPrecision(0))

metric_a = metrics.Metric(
    name="average_download_seconds",
    title=Title("Average seconds per download"),
    unit=metrics.Unit(notation=metrics.DecimalNotation("s")),
    color=metrics.Color.DARK_GREEN
)

metric_b = metrics.Metric(
    name="digest_errors",
    title=Title("Corrupted files after download"),
    unit=UNIT_NUMBER,
    color=metrics.Color.DARK_YELLOW
)

metric_c = metrics.Metric(
    name="errors",
    title=Title("Error responses from server"),
    unit=UNIT_NUMBER,
    color=metrics.Color.LIGHT_RED
)

metric_d = metrics.Metric(
    name="exceptions",
    title=Title("Exceptions thrown while benchmarking"),
    unit=UNIT_NUMBER,
    color=metrics.Color.DARK_RED
)

metric_e = metrics.Metric(
    name="timeouts",
    title=Title("Timeouts during file transfers"),
    unit=UNIT_NUMBER,
    color=metrics.Color.LIGHT_ORANGE
)

graph_jean_claude_pillemann = graphs.Graph(
    name="errors_combined",
    title=Title("Errors during benchmarking"),
    simple_lines=[
        "digest_errors",
        "errors",
        "exceptions",
        "timeouts"
    ]
)
