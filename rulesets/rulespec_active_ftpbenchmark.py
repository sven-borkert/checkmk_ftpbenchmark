# -*- encoding: utf-8 -*-

from cmk.rulesets.v1 import Title, Help
from cmk.rulesets.v1.form_specs import (
    Dictionary,
    DictElement,
    CascadingSingleChoice,
    CascadingSingleChoiceElement,
    String,
    Password,
    FixedValue,
    DefaultValue,
    BooleanChoice,
    Integer
)
from cmk.rulesets.v1.rule_specs import Topic, SpecialAgent, ActiveCheck


def _valuespec_active_ftpbenchmark() -> Dictionary:
    return Dictionary(
        title=Title("FTP Benchmark"),
        help_text=Help("This rule is used to set up the FTP benchmark Special agent."),
        elements={
            "host": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("FTP server host/ip"),
                    help_text=Help("The address of the FTP server to connect to"),
                ),
            ),
            "port": DictElement(
                required=True,
                parameter_form=Integer(
                    title=Title("FTP server port"),
                    help_text=Help("The port of the FTP server to connect to"),
                    prefill=DefaultValue(21)
                ),
            ),
            "user": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Username"),
                    help_text=Help("Username for login to FTP server"),
                ),
            ),
            "password": DictElement(
                required=True,
                parameter_form=Password(
                    title=Title("Password"),
                    help_text=Help("Password for login to FTP server"),
                ),
            ),
            "mode": DictElement(
                required=True,
                parameter_form=CascadingSingleChoice(
                    title=Title("Transfer mode"),
                    help_text=Help('FTP transfer mode'),
                    prefill=DefaultValue("passive"),
                    elements=[
                        CascadingSingleChoiceElement(
                            name="passive",
                            title=Title("Passive"),
                            parameter_form=FixedValue(value="passive"),
                        ),
                        CascadingSingleChoiceElement(
                            name="active",
                            title=Title("Active"),
                            parameter_form=FixedValue(value="active"),
                        ),
                    ],
                ),
            ),
            "path": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Path"),
                    help_text=Help("Path to file used for testing"),
                ),
            ),
            "file_size": DictElement(
                required=True,
                parameter_form=Integer(
                    title=Title("File size"),
                    help_text=Help("The size file used for benchmarking"),
                    prefill=DefaultValue(1024)
                ),
            ),
            "download_benchmarking": DictElement(
                required=True,
                parameter_form=BooleanChoice(
                    title=Title("Download benchmarking"),
                    help_text=Help('Enables download benchmarking'),
                )
            ),
            "download_count": DictElement(
                required=True,
                parameter_form=Integer(
                    title=Title("Download count"),
                    help_text=Help("How many times to download a file in one execution"),
                    prefill=DefaultValue(1024)
                ),
            ),
            "upload_benchmarking": DictElement(
                required=True,
                parameter_form=BooleanChoice(
                    title=Title("Upload benchmarking"),
                    help_text=Help('Upload download benchmarking'),
                )
            ),
            "upload_count": DictElement(
                required=True,
                parameter_form=Integer(
                    title=Title("Upload count"),
                    help_text=Help("How many times to update a file in one execution"),
                    prefill=DefaultValue(1024)
                ),
            ),

        },
    )


rule_spec_ftpbenchmark_datasource_programs = ActiveCheck(
    name="ftpbenchmark",
    title=Title("FTP benchmark"),
    topic=Topic.APPLICATIONS,
    parameter_form=_valuespec_active_ftpbenchmark,
    help_text=Help("This is the help text of the FTP benchmark check module"),
)
