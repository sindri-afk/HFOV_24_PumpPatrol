import json
from ..models.virtualworkout_model import Workout
class VirtualWorkoutRepository:
    def __init__(self, file_path="VirtualPrograms/data/programs.json"):
        self.file_path = file_path
        
    def get_all_workout_programs(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)
            return [Workout.from_dict(item) for item in data]

    def filter_workouts_by_body_part(self, body_part):

        virtualworkouts = self.get_all_workout_programs()
        for workout in virtualworkouts:
            if workout.program_name == body_part:
                return workout
        return None