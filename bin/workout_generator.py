from datetime import datetime, timedelta
import json

datetime_pointer = datetime(2025, 6, 9)
workouts = []

while True:
    print(f"DATETIME: {datetime_pointer} {datetime_pointer.weekday()}")
    dct = {
        'date': datetime.strftime(datetime_pointer, "%a %b %w"),
        'focus': 'Endurance',
        'detail': '',
    }
    if datetime_pointer.weekday() == 0 or datetime_pointer.weekday() == 4:
        dct['focus'] = 'Run / Drills'
    elif datetime_pointer.weekday() == 1 or datetime_pointer.weekday() == 3:
        dct['focus'] = 'Workout / Speed'
    else:
        dct['focus'] = 'Off'
    workouts.append(dct)
    if datetime_pointer > datetime(2025, 8, 10):
        break
    datetime_pointer += timedelta(days=1)

print(json.dumps(workouts, indent=4))

