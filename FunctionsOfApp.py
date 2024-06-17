from habit import Habit
from datetime import datetime
from typing import List
from collections import defaultdict


def define_frequency() -> Habit.DefineFrequency:
    """Function returns an instance of the DefineFrequency enumeration class."""
    input_frequency = input("Choose 'D' for Daily, 'W' for weekly, 'M' for monthly").upper()
    frequency = None

    if input_frequency == "D":
        print("Habit is defined as daily")
        frequency = Habit.DefineFrequency.DAILY
    elif input_frequency == "W":
        print("Habit is defined as weekly")
        frequency = Habit.DefineFrequency.WEEKLY
    elif input_frequency == "M":
        print("Habit is defined as monthly")
        frequency = Habit.DefineFrequency.MONTHLY
    else:
        print("Invalid input. Please choose 'D', 'W', or 'M'.")

    return frequency


def create_new_habit():
    """
    User creates new instance of the Habit class
    """
    habit_name = input("Write the name of the new habit you want to track:")
    habit_frequency = define_frequency()
    creation_date = datetime.now()

    habit = Habit(
        habit_name=habit_name,
        habit_frequency=habit_frequency,
        creation_date=creation_date,
        completion_dates={}
    )
    return habit


def check_off_habit(habit: Habit):
    """
    User marks habit as completed
    """
    completion_date = datetime.now()
    habit.mark_completed(completion_date)
    print("Habit marked as completed!")
    return habit.completion_dates


def choose_habit_from_the_list(list_of_habits: List[Habit]):
    """
    User chooses habit from the list by entering its index
    """
    chosen_habit_index = input("Choose the index of a habit")
    chosen_habit = list_of_habits[int(chosen_habit_index)-1]
    return chosen_habit


def print_list_of_habits(list_of_habits: List[Habit]):
    """
    User prints the list of all tracked habits
    """
    for index, habit_from_list in enumerate(list_of_habits):
        print(f"Habit {index + 1}:\n{habit_from_list}")


def edit_habit_details(habit: Habit):
    """
    User edits details of a habit
    """
    habit.habit_name = input("Define new name:")
    habit.habit_frequency = define_frequency()


def get_habit_with_longest_streak(list_of_habits: List[Habit]):
    """
    Getting the habit with the longest streak out of a list of habits
    """
    # Initialize variables to track the longest streak and its corresponding index
    longest_streak = 0
    index_of_longest_streak = -1
    for index, habit in enumerate(list_of_habits):
        streak = habit.get_habit_streak()
        print(f"streak of habit{index + 1}: {streak}")
        # Check if the current habit's streak is longer than the recorded longest streak
        if streak > longest_streak:
            longest_streak = streak
            index_of_longest_streak = index
    if index_of_longest_streak != -1:
        print(f"The habit{index_of_longest_streak + 1} has the longest streak in the list: {longest_streak}")
    else:
        print("No habits found in the list.")


def get_streaks_of_all_habits(list_of_habits: List[Habit]):
    """
    Obtaining streaks of all habits
    """
    for index, habit in enumerate(list_of_habits):
        print(f"Streak of habit {index+1} is: {habit.get_habit_streak()}")


def show_habits_with_same_periodicity(list_of_habits: List[Habit]):
    input_frequency = input("Enter the periodicity (Daily, Weekly, Monthly)").upper()
    grouped_habits = defaultdict(list)
    for habit in list_of_habits:
        if habit.habit_frequency.upper() == input_frequency:
            grouped_habits[habit.habit_frequency].append(habit)
    return grouped_habits










        


