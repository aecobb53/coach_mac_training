from datetime import datetime, timedelta
import json
import pyperclip

datetime_pointer = datetime(2025, 6, 9)
workouts = []

while True:
    print(f"DATETIME: {datetime_pointer} {datetime_pointer.weekday()}")
    dct = {
        'date': datetime.strftime(datetime_pointer, "%a %b %d"),
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

# print(json.dumps(workouts, indent=4))


with open('etc/workout_plan.csv', 'r') as cf:
    csv = []
    for line in cf.readlines():
        line = line.strip()
        line_l = [l.strip() for l in line.split(',')]
        csv.append(line_l)
    header = [i.lower() for i in csv.pop(0)[:3]]
    workouts2 = [{k: v for k, v in zip(header, i)} for i in csv]
    for item in workouts2:
        x=1
        item['date'] = datetime.strftime(
            datetime.strptime(item['date'], "%m/%d/%Y"),
            "%a %b %d")



# print(json.dumps(workouts2, indent=4))
# pyperclip.copy(json.dumps(workouts2, indent=4))


# REVAMPED
with open('etc/workout_plan.csv', 'r') as cf:
    csv = []
    for line in cf.readlines():
        line = line.strip()
        line_l = [l.strip() for l in line.split(',')]
        csv.append(line_l)
    header = [i.lower() for i in csv.pop(0)[:3]]
    workouts2 = [{k: v for k, v in zip(header, i)} for i in csv]
    for item in workouts2:
        item['date'] = datetime.strptime(item['date'], "%m/%d/%Y")
workouts3 = []
week = []
week_pointer = 1
for index, item in enumerate(workouts2):
    x=1
    if item['date'].weekday() == 0 and week:
        for thing in week:
            thing['date'] = datetime.strftime(thing['date'], "%a %b %d")
        workouts3.append({
            'tile_header': f"Week {week_pointer}",
            'tile_info_1': '',
            'tile_info_2': '',
            'day_data': week,
            })
        week = []
        week_pointer += 1
    week.append(item)
# Last lines
for thing in week:
    thing['date'] = datetime.strftime(thing['date'], "%a %b %d")
workouts3.append({
    'tile_header': f"Week {week_pointer}",
    'tile_info_1': '',
    'tile_info_2': '',
    'day_data': week,
    })


print(json.dumps(workouts3, indent=4))
pyperclip.copy(json.dumps(workouts3, indent=4))
x=1

