import os

from ucl_open_y_maze.task import (
    UclOpenYMazeTaskLogic,
    UclOpenYMazeTaskParameters,
    RewardProbability,
    DoorCommand
)

task_logic = UclOpenYMazeTaskLogic(
    task_parameters=UclOpenYMazeTaskParameters(
        arm_reward_probabilities = {'a': RewardProbability(probability=1), 'b': RewardProbability(probability=0)},
        trigger_door_mapping = {0: [DoorCommand(door_id=0, probability=1)], 1: [DoorCommand(door_id=0, probability=1)]},
        trigger_visual_mapping = {}
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