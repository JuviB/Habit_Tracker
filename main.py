import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit

def menu():
    print("1. Enter a new habit")
    print("2. Display existing habits")
    print("3. Exit")
    choice = input("Enter your choice (1, 2 or 3): ")
    return choice

def display_habits(habits):
    # Extract habit attributes for DataFrame
    habit_data = [(habit.name, habit.time_since, habit.remaining_days, habit.minutes_saved, habit.money_saved) for habit in habits]

    # Creates a DataFrame
    df = pd.DataFrame(habit_data, columns=['Name', 'Time Since', 'Remaining days', 'Minutes saved', 'Money saved'])

    # Create a nice table
    print(tabulate(df, headers='keys', tablefmt='psql'))

def main():
    # Habits
    habits = [
        track_habit('Coffee', datetime(2024, 1, 12, 12), cost=30, minutes_used=5),
        track_habit('Alcohol', datetime(2023, 12, 5, 22), cost=500, minutes_used=15),
        track_habit('Fizzy drinks', datetime(2023, 10, 16, 19), cost=15, minutes_used=3),
        track_habit('Sugar / Candy', datetime(2024, 1, 1, 1), cost=1, minutes_used=3),
    ]

    while True:
        choice = menu()

        if choice == '1':
            # Prompt user for input for a new habit
            new_habit_name = input("Enter the name of the new habit: ").upper()
            new_habit_start_date = datetime.strptime(input("Enter the start date of the new habit (YYYY-MM-DD HH:MM): "), '%Y-%m-%d %H:%M')
            new_habit_cost = float(input("Enter the cost of the new habit per day: "))
            new_habit_minutes_used = float(input("Enter the amount of minutes used for the new habit: "))

            # Create a new Habit instance for the user-input habit
            new_habit = track_habit(new_habit_name, new_habit_start_date, cost=new_habit_cost, minutes_used=new_habit_minutes_used)

            # Add the new habit to the list
            habits.append(new_habit)

        elif choice == '2':
            # Display existing habits
            display_habits(habits)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == '__main__':
    main()