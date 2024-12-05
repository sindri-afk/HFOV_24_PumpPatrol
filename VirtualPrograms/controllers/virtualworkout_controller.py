from ..services.virtualworkout_service import VirtualWorkoutService

class VirtualWorkoutController:
    def __init__(self):
        self.service = VirtualWorkoutService()
    
    def view_workout_programs(self):
        workouts = self.service.view_workout_programs()
        for workout in workouts:
            print(workout.to_dict())