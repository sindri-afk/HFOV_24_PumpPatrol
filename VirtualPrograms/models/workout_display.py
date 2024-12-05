def display_workout_program(workouts):
    for workout in workouts:
        print(f"Program Name: {workout.program_name}")
        print(f"Description:\n{workout.program_description}")
    input("\nPress Enter to return to the menu...")