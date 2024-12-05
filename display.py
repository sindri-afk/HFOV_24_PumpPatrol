import os
import shutil
import time

def display_menu(title: str, options: dict):

    # Terminal dimensions
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns
    terminal_height = terminal_size.lines

    # Fixed menu box dimensions
    box_width = min(60, terminal_width - 10)
    box_height = len(options) + 6  # Title + options + borders + padding
    horizontal_padding = max(0, (terminal_width - box_width) // 2)
    vertical_padding = max(0, (terminal_height - box_height) // 2)

    # Title centered within the box width
    title_line = f" {title} ".center(box_width - 2, " ")  # Adjust width for borders

    # Prepare menu options
    menu_lines = []
    for key, (desc, _) in options.items():
        option_text = f"{key}. {desc}".ljust(box_width - 2)  # Ensure alignment
        menu_lines.append(option_text)

    # Clear the terminal
    os.system("clear" if os.name == "posix" else "cls")

    # Print the menu
    print("\n" * vertical_padding)
    print(" " * horizontal_padding + "┌" + "─" * (box_width - 2) + "┐")
    print(" " * horizontal_padding + "│" + title_line + "│")
    print(" " * horizontal_padding + "├" + "─" * (box_width - 2) + "┤")
    for line in menu_lines:
        print(" " * horizontal_padding + "│" + line + "│")
    print(" " * horizontal_padding + "└" + "─" * (box_width - 2) + "┘")
    print("\n" * vertical_padding)

    # Get user input
    try:
        choice = int(input("Please select an option: "))
        if choice in options:
            _, action = options[choice]
            if action:
                os.system("clear" if os.name == "posix" else "cls")
                action()  # Call the corresponding function
            else:
                print("Exiting... Goodbye!")
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)
            display_menu(title, options)
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        time.sleep(1)
        display_menu(title, options)