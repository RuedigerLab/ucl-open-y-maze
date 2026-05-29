# Import core types
from typing import Literal
from pydantic import Field

from swc.aeon.io import reader
from swc.aeon.schema import BaseSchema, data_reader

from ucl_open_y_maze import __semver__

# TODO - should inherit from some TaskParameters base class rather than BaseSchema
class UclOpenYMazeTaskParameters(BaseSchema):
    ...


class UclOpenYMazeTaskLogic(BaseSchema):
    version: Literal[__semver__] = __semver__
    name: Literal["UclOpenYMaze"] = Field(default="UclOpenYMaze", description="Name of the task logic", frozen=True)
    task_parameters: UclOpenYMazeTaskParameters = Field(description="Parameters of the task logic")
    ...