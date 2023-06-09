def study_schedule(permanence_period, target_time):
    # permanence_period list of tuples (entry, exit)
    counter = 0
    if target_time is None:
        return None
    for time in permanence_period:
        if not isinstance(time[0], int) or not isinstance(time[1], int):
            return None
        if time[0] <= target_time <= time[1]:
            counter += 1
    return counter
