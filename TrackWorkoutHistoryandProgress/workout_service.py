import json

class WorkoutService:
    def __init__(self):
        self.history_file = "TrackWorkoutHistoryandProgress/exercise_history.json"  # Make sure the file path is correct

    def get_exercise_history(self, username):
        try:
            with open(self.history_file, "r") as f:
                exercises = json.load(f)
                # Filter exercises by username
                return [exercise for exercise in exercises if exercise.get("username") == username]
        except Exception as e:
            print(f"Error reading exercise history: {e}")
            return []
    
    def add_exercise(self, username, exercise_data):
        try:
            with open(self.history_file, "r") as f:
                exercises = json.load(f)
        except FileNotFoundError:
            exercises = []
        
        # Add username to the exercise data
        exercise_data["username"] = username
        exercises.append(exercise_data)

        try:
            with open(self.history_file, "w") as f:
                json.dump(exercises, f, indent=4)
        except Exception as e:
            print(f"Error saving exercise: {e}")
