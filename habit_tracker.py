from datetime import datetime

class Habit:
    def __init__(self, name, time_since, remaining_days, minutes_saved, money_saved):
        self.name = name
        self.time_since = time_since
        self.remaining_days = remaining_days
        self.minutes_saved = minutes_saved
        self.money_saved = money_saved

def track_habit(name, start, cost, minutes_used):
    """
    Calculates the time elapsed, time remaining, cost, and minutes wasted on a habit.

    :param name: The name of the habit.
    :param start: The start date of the habit.
    :param cost: The cost of the habit per day.
    :param minutes_used: The amount of minutes used performing the habit.
    :return: Habit
    """

    goal = 60  # Days
    hourly_wage = 30  # Euros

    # Total time elapsed in seconds
    time_elapsed = (datetime.now() - start).total_seconds()

    # Convert timestamp into hours/days
    hours = round(time_elapsed / 60 / 60, 1)
    days = round(hours / 24, 2)

    # Random bonus details
    money_saved = cost * days
    minutes_used = round(days * minutes_used)
    total_money_saved = f'R{round(money_saved + (minutes_used / 60 * hourly_wage), 2)}'

    # Amount of days remaining until you break a habit
    days_to_go = round(goal - days)

    # Displayable information
    if days_to_go <= 0:
        remaining_days = 'Cleared!'
    else:
        remaining_days = f'{days_to_go}'

    if hours > 72:
        time_since = f'{int(days)} days'
    else:
        time_since = f'{hours} hours'

    habit_instance = Habit(name=name,
                           time_since=time_since,
                           remaining_days=remaining_days,
                           minutes_saved=minutes_used,
                           money_saved=total_money_saved)
    
    return habit_instance