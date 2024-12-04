from TrackWorkoutHistoryandProgress.workout_service import WorkoutService

workout_service = WorkoutService()

def track_exercise(user, go_back_callback):
    print(f"\nTrack Exercise for {user.username}")
    exercise_name = input("Enter exercise name: ")
    duration = input("Enter exercise duration (e.g., 30 minutes): ")
    intensity = input("Enter intensity level (e.g., Light, Moderate, High): ")

    # Save exercise for the user
    workout_service.add_exercise(user.username, {
        "exercise": exercise_name,
        "duration": duration,
        "intensity": intensity,
    })

    print("\nExercise saved successfully!")
    print("\n1. Add another exercise\n2. Go back to the Workout History menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        track_exercise(user, go_back_callback)
    elif choice == "2":
        return
    go_back_callback(user)


def view_exercise_history(user, go_back_callback):
    print(f"\nExercise History for {user.username}")
    exercises = workout_service.get_exercise_history(user.username)
    if exercises:
        for idx, exercise in enumerate(exercises, start=1):
            print(f"{idx}. {exercise['exercise']} - {exercise['duration']} ({exercise['intensity']})")
    else:
        print("No exercises recorded yet.")

    input("\nPress Enter to go back...")
    go_back_callback(user)  # Call the provided callback to go back
