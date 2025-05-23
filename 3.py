from datetime import date

class Task:
    def __init__(self, date_start, date_finish, description):
        self.date_start = date_start
        self.date_finish = date_finish
        self.description = description

tasks = \
[
    Task(date(2020, 1, 1), date(2020, 1, 13), 'new year'),
    Task(date(2020, 2, 23), date(2020, 3, 8), '23 feb and 8 mar'),
    Task(date(2020, 4, 20), date(2020, 5, 20), 'spring'),
    Task(date(2020, 6, 1), date(2020, 8, 31), 'summer'),
    Task(date(2020, 9, 1), date(2020, 12, 31), 'autumn and winter')
]

max_finish = date(2020, 1, 1)

for task in tasks:
    if task.date_finish > max_finish:
        max_finish = task.date_finish

for task in tasks:
    if task.date_finish == max_finish:
        print(task.date_start, task.date_finish, task.description)