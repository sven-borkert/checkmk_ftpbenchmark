# -*- coding: utf-8 -*-

from collections.abc import Iterator
from pydantic import BaseModel

from cmk.server_side_calls.v1 import (
    HostConfig,
    Secret, ActiveCheckCommand, ActiveCheckConfig
)


class Params(BaseModel):
    """params validator"""
    host: str | None = None
    port: int | None = 21
    user: str | None = None
    password: Secret | None = None
    mode: tuple[str, str | None] = None
    path: str | None = None
    file_size: int | None = 1
    download_benchmarking: bool | None = True
    download_count: int | None = 10
    upload_benchmarking: bool | None = False
    upload_count: int | None = 10
    
def commands_function(
    params: Params, host_config: HostConfig
) -> Iterator[ActiveCheckCommand]:
    command_arguments: list[str] = []
    if params.host is not None:
        command_arguments += ["--host", params.host]
    if params.port is not None:
        command_arguments += ["--port", str(params.port)]
    if params.user is not None:
        command_arguments += ["--user", params.user]
    if params.password is not None:
        command_arguments += ["--password", params.password]
    if params.mode is not None and params.mode[1] == 'active':
        command_arguments += ["--active"]
    if params.path is not None:
        command_arguments += ["--path", params.path]
    if params.file_size is not None:
        command_arguments += ["--file-size", str(params.file_size)]
    if params.download_benchmarking is not None:
        command_arguments += ["--download"]
    if params.download_count is not None:
        command_arguments += ["--download-count", str(params.download_count)]
    if params.upload_benchmarking is not None:
        command_arguments += ["--upload"]
    if params.upload_count is not None:
        command_arguments += ["--upload-count", str(params.upload_count)]
    yield ActiveCheckCommand(service_description="FTP benchmark", command_arguments=command_arguments)


active_check_config = ActiveCheckConfig(
    name="ftpbenchmark",
    parameter_parser=Params.model_validate,
    commands_function=commands_function,
)
