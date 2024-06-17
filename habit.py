from datetime import datetime, timedelta
from enum import Enum



class Habit:
    class DefineFrequency(Enum):

        DAILY = "Daily"
        WEEKLY = "Weekly"
        MONTHLY = "Monthly"

    def __init__(self,
                 habit_name: str,
                 habit_frequency: DefineFrequency,
                 creation_date: datetime,
                 completion_dates=None
                 ):
        """
        Parameters:
        - habit_name: User inputs the name of new habit
        - habit_frequency: User inputs desired frequency
        - creation_date: User inputs date and time when habit is created
        - completion_dates: Dictionary which stores dates of completion as keys and
                            True or False as value pairs.
        """
        self._habit_name = habit_name
        self._habit_frequency = habit_frequency
        self._creation_date = creation_date
        self._completion_dates = completion_dates if completion_dates is not None else {}
        self._deadline = self.display_next_deadline(creation_date)

    def mark_completed(self, completion_date):
        """
        Mark the habit as completed
        Default value is False, if completed it updates to True

        Args:
        - completion_date (datetime): The date when the habit was completed
        """

        self._completion_dates[completion_date] = True

    def display_next_deadline(self, date: datetime):
        if self._habit_frequency == Habit.DefineFrequency.DAILY:
            return date + timedelta(days=1)
        elif self._habit_frequency == self.DefineFrequency.WEEKLY:
            return date + timedelta(weeks=1)
        elif self._habit_frequency == self.DefineFrequency.MONTHLY:
            return date + timedelta(days=30)
        else:
            raise ValueError("Invalid habit frequency")

    @property
    def habit_name(self):
        print(f"{self._habit_name} is accessed")
        return self._habit_name

    @habit_name.setter
    def habit_name(self, value):
        print(f"{self._habit_name} is now {value}")
        self._habit_name = value

    @habit_name.deleter
    def habit_name(self):
        print(f"{self._habit_name} is deleted")
        del self._habit_name

    @property
    def habit_frequency(self):
        print(f"{self._habit_frequency} is accessed")
        return self._habit_frequency

    @habit_frequency.setter
    def habit_frequency(self, new_frequency: str):
        print(f"{self._habit_frequency} is now {new_frequency}")
        self._habit_frequency = new_frequency

    @property
    def creation_date(self):
        print(f"{self._creation_date} is accessed")
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        print(f"{self._creation_date} is now {value}")
        self._creation_date = value

    @property
    def completion_dates(self):
        """
        Overview of days when the habit was completed or not
        """
        print(f"{self._completion_dates} are accessed")
        return self._completion_dates

    @completion_dates.setter
    def completion_dates(self, value):
        """
        Setting the days in advance when habit must be completed
        :parameter: date in the form of Year-Month-Day
        """
        print(f"{self._completion_dates} are now {value}")
        self._completion_dates = value

    @property
    def last_deadline(self):
        print(f"{self._deadline} is accessed")
        return self._deadline

    @last_deadline.setter
    def last_deadline(self, value):
        """
        Setting the new last deadline until when habit must be completed
        :return: New last deadline
        """
        print(f"{self._deadline} is now {value}")
        self._deadline = value

    def __str__(self):
        """
        Get the overview of habit
        :return: -str: String representation of a habit
        """
        return f"Habit name: {self._habit_name} \n" \
               f"Habit frequency: {self._habit_frequency}\n" \
               f"Habit creation date: {self._creation_date}\n" \
               f"Habit completion dates: {self._completion_dates} \n" \
               f"Habit last deadline: {self._deadline} \n"

    def get_habit_streak(self):
        """
        Get the longest streak of specific habit
        """
        current_streak = 0
        longest_streak = 0

        for date, completed in sorted(self._completion_dates.items()):
            if completed:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 0

        """Update longest streak"""
        longest_streak = max(longest_streak, current_streak)

        return longest_streak

