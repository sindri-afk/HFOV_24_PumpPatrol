from TrackWorkoutHistoryandProgress.workout_service import WorkoutService
from datetime import datetime

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
        "timestamp": datetime.now().isoformat(),  # Add the timestamp here
    })

    print("\nExercise saved successfully!")
    
    while True:
        print("\n1. Add another exercise\n2. Go back to the Workout History menu")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            track_exercise(user, go_back_callback)
            break  # Exit loop after processing the next exercise
        elif choice == "2":
            go_back_callback(user)
            break  # Return to the Workout History menu
        else:
            print("Invalid choice. Please enter 1 to add another exercise or 2 to go back.")


def view_exercise_history(user, go_back_callback):
    exercises = workout_service.get_exercise_history(user.username)
    
    # Sort exercises by timestamp in descending order
    sorted_exercises = sorted(
        exercises,
        key=lambda x: datetime.fromisoformat(x.get('timestamp', '1970-01-01T00:00:00')),
        reverse=True
    )
    
    # Prepare the exercise details for display
    menu_content = [
        f"{idx}. {exercise['exercise']} - {exercise['duration']} ({exercise['intensity']}) on {datetime.fromisoformat(exercise.get('timestamp', '1970-01-01T00:00:00')).strftime('%H:%M, %a, %b')}"
        for idx, exercise in enumerate(sorted_exercises, start=1)
    ]
    
    # Fill remaining slots with placeholders for UI alignment
    while len(menu_content) < 10:
        menu_content.append(f"{len(menu_content) + 1}.  -  ()")
    
    # Display the menu
    print("\n" + " " * 25 + "┌" + "─" * 70 + "┐")
    print(" " * 25 + f"│{f'Exercise History for {user.username}':^70}│")
    print(" " * 25 + "├" + "─" * 70 + "┤")
    for line in menu_content:
        print(f" " * 25 + f"│{line:<70}│")
    print(" " * 25 + "└" + "─" * 70 + "┘")

    # Prompt to go back
    input("\nPress Enter to go back...")
    go_back_callback(user)
