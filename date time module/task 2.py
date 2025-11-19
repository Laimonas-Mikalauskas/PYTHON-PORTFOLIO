from datetime import datetime

def set_event(name: str, year: int, month: int, day: int, hour: int) -> None:
    """
    Creates event time by given settings and prints it by default format.

    :param name: Event name
    :param year: Year (e.g., 2025)
    :param month: Month (1-12)
    :param day: Day (1-31)
    :param hour: Hour (0-23)
    """
    try:
        event_time = datetime(year, month, day, hour)
        print(f'Event{name} will_happen {event_time.year}-{event_time.month}-{event_time.day} {event_time.hour}:00')
    except Exception as ex:
        print(f'Error by creating a date: {ex}')

set_event('Python lectures', 2025, 12, 10, 14)










