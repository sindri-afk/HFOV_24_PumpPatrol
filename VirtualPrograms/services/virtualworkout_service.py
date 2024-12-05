from ..repositories.virtual_workout_repository import VirtualWorkoutRepository


class VirtualWorkoutService:
    def __init__(self):
        self.repository = VirtualWorkoutRepository()
    
    def view_workout_programs(self):
        return self.repository.get_all_workout_programs()
    

