# STAGE 1
class TaskList():
    def __init__(self, lst):
        self.lst = lst

    def today(self):
        print('Today:')
        i = 0
        for item in self.lst:
            i += 1
            print(f'{i}) {item}')


tasks = ['Do yoga', 'Make breakfast', 'Learn basics of SQL', 'Learn what is ORM']

today = TaskList(tasks)

today.today()
