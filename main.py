from FunctionsOfApp import *


habit1 = Habit(
    habit_name="Daily hydration goal",
    habit_frequency=Habit.DefineFrequency.DAILY,
    creation_date=datetime.now(),
    completion_dates={}
)
habit2 = Habit(
    habit_name="Running",
    habit_frequency=Habit.DefineFrequency.DAILY,
    creation_date=datetime.now(),
    completion_dates={}
)
habit3 = Habit(
    habit_name="Swimming",
    habit_frequency=Habit.DefineFrequency.WEEKLY,
    creation_date=datetime.now(),
    completion_dates={}
)
habit4 = Habit(
    habit_name="Reading a book",
    habit_frequency=Habit.DefineFrequency.WEEKLY,
    creation_date=datetime.now(),
    completion_dates={}
)
habit5 = Habit(
    habit_name="Outdoor adventure",
    habit_frequency=Habit.DefineFrequency.MONTHLY,
    creation_date=datetime.now(),
    completion_dates={}
)

if __name__ == '__main__':

    list_of_habits = [habit1, habit2, habit3, habit4, habit5]
    while True:
        try:

            user_choice = input("""
            
Enter 1 to mark the habit completed
Enter 2 to view the list of all habits
Enter 3 to create new habit
Enter 4 to delete existing habit
Enter 5 to edit habit details
Enter 6 to get longest streak from the list
Enter 7 to get longest streaks of all habits
    

""")
            if user_choice == "1":
                # User chooses habit from the list and marks it as completed
                chosen_habit = choose_habit_from_the_list(list_of_habits)
                check_off_habit(habit=chosen_habit)

            elif user_choice == "2":
                # User accesses the list of all habits
                print_list_of_habits(list_of_habits)

            elif user_choice == "3":
                # User creates new habit and appends it to the list
                new_habit = create_new_habit()
                list_of_habits.append(new_habit)
                print("New habit added to the tracking list!")

            elif user_choice == "4":
                # User chooses index of a habit and removes it
                habit_to_delete = choose_habit_from_the_list(list_of_habits)
                list_of_habits.remove(habit_to_delete)
                print("Habit deleted successfully!")

            elif user_choice == "5":
                # User chooses habit from the list and edits details
                habit_to_edit = choose_habit_from_the_list(list_of_habits)
                edit_habit_details(habit=habit_to_edit)

            elif user_choice == "6":
                # Getting the habit with the highest streak
                get_habit_with_longest_streak(list_of_habits)

            elif user_choice == "7":
                # Getting the streaks of all habits from a list
                get_streaks_of_all_habits(list_of_habits)

        except Exception as e:
            # Display any exceptions that occur during the program execution
            print(f"Exception: {e}")
