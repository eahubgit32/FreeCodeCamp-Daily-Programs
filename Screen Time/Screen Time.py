def too_much_screen_time(hours):
    # Rule 1: Any single day has 10 or more hours
    if any(day >= 10 for day in hours):
        return True

    # Rule 2: Any 3-day rolling average is ≥ 8 hours
    for i in range(len(hours) - 2):
        three_day_avg = sum(hours[i:i+3]) / 3
        if three_day_avg >= 8:
            return True

    # Rule 3: Weekly average is ≥ 6 hours
    weekly_avg = sum(hours) / 7
    if weekly_avg >= 6:
        return True

    return False


print(too_much_screen_time([1, 2, 3, 4, 5, 6, 7]))
