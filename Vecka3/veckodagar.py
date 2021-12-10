
DAYS = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
        4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}


def weekday(n: int) -> str:
    try:
        return DAYS[n % 7]
    except KeyError:
        return f"{n} not a valid weekday"
        # raise ValueError(f"{n} not a valid weekday")


DAYS_INV = {"Monday": 1, "Tuesday": 2, "Wednesday": 3,
            "Thursday": 4, "Friday": 5, "Saturday": 6,
            "Sunday": 7}


def day_of_week(day: str) -> int:
    if day in DAYS_INV:
        return DAYS_INV[day]
    raise ValueError(f"'{day}' not a valid weekday")


if __name__ == '__main__':
    assert day_of_week("Monday") == 1
    assert day_of_week("Wednesday") == 3
    assert day_of_week("Sunday") == 7
    assert weekday(day_of_week("Monday")) == "Monday"
