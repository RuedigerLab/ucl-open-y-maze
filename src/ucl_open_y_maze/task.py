# Import core types
from typing import Literal, Dict, List, Optional
from pydantic import Field

from swc.aeon.io import reader
from swc.aeon.schema import BaseSchema, data_reader

from ucl_open_y_maze import __semver__

class RewardProbability(BaseSchema):
    probability: float = Field(default = 0, ge=0, le=1)
    
class DoorCommand(BaseSchema):
    door_id: int
    probability: float = Field(default = 0, ge=0, le=1)
    
class VisualStimulation(BaseSchema):
    screen_id: int
    ...

class UclOpenYMazeTaskParameters(BaseSchema):
    rng_seed: Optional[float] = Field(default=None, description="Seed of the random number generator")
    arm_reward_probabilities: Dict[str, RewardProbability]
    trigger_door_mapping: Dict[int, List[DoorCommand]]
    trigger_visual_mapping: Dict[int, VisualStimulation]

class UclOpenYMazeTaskLogic(BaseSchema):
    version: Literal[__semver__] = __semver__
    name: Literal["UclOpenYMaze"] = Field(default="UclOpenYMaze", description="Name of the task logic", frozen=True)
    task_parameters: UclOpenYMazeTaskParameters = Field(description="Parameters of the task logic")
    ...