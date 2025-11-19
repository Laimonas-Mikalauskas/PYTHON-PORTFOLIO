import datetime

def register_activeness(current_time=None):
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 9 <= hour < 17:
        print(f'Activeness is registered: {current_time}')
    else:
        print(f'Not at work time: {current_time}')

register_activeness()
