from typing import Literal, Dict
from pydantic import Field

from ucl_open.core.rig import Rig

from ucl_open_y_maze import __semver__


class UclOpenYMazeRig(Rig):
    version: Literal[__semver__] = __semver__
    ...