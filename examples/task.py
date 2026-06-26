import os

from ucl_open_y_maze.task import (
    UclOpenYMazeTaskLogic,
    UclOpenYMazeTaskParameters,
    RewardProbability,
    DoorCommand,
    RegionTrigger,
    VisualStimulation
)
from ucl_open.core.base import Vector2

task_logic = UclOpenYMazeTaskLogic(
    task_parameters=UclOpenYMazeTaskParameters(
        n_screens=4,
        region_triggers = {
            0: RegionTrigger(region_polygon=[Vector2(x=61, y=73), Vector2(x=152, y=73), Vector2(x=152, y=157), Vector2(x=61, y=157)], threshold=40, sum_threshold=44000),
            1: RegionTrigger(region_polygon=[Vector2(x=391, y=252), Vector2(x=482, y=252), Vector2(x=482, y=336), Vector2(x=391, y=336)], threshold=40, sum_threshold=44000)
        },
        arm_reward_probabilities = {0: RewardProbability(reward_id=0, probability=1), 1: RewardProbability(reward_id=1, probability=0)},
        trigger_door_mapping = {0: [DoorCommand(door_id=0, probability=1)], 1: [DoorCommand(door_id=1, probability=1)]},
        trigger_visual_mapping = {0: VisualStimulation(screen_id=0), 1: VisualStimulation(screen_id=1)}
    ),
)

def main(path_seed: str = "./local/{schema}.json"):
    example_task_logic = task_logic
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [example_task_logic]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()