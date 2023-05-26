def study_schedule(permanence_period, target_time):
    if target_time is None:

        return None

    horas = 0

    for start, finish in permanence_period:
        if type(start) is not int or type(finish) is not int:
            return None

        if start <= target_time <= finish:
            horas += 1

    return horas
