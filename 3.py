import datetime

class Task:
    def __init__(self, DateStart, DateFinish, Description):
        self.DateStart = DateStart
        self.DateFinish = DateFinish
        self.Description = Description

tasks = [Task(datetime.date(2020,1,1), datetime.date(2020,1,13), 'new year'),
Task(datetime.date(2020, 2, 23), datetime.date(2020, 3, 8), '23 feb and 8 mar'),
Task(datetime.date(2020, 4, 20),  datetime.date(2020, 5, 20), 'spring'),
Task(datetime.date(2020, 6, 1), datetime.date(2020, 8, 31), 'summer'),
Task(datetime.date(2020, 9, 1), datetime.date(2020, 12, 31), 'autumn and winter')]

max_datefinish = datetime.date(2020, 1, 1)
for task in tasks:
    if task.DateFinish > max_datefinish:
        max_datefinish = task.DateFinish
for task in tasks:
    if max_datefinish == task.DateFinish:
        print(task.DateStart, task.DateFinish, task.Description)