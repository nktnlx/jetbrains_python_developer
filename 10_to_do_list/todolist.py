# STAGE 1
# class TaskList():
#     def __init__(self, lst):
#         self.lst = lst
#
#     def today(self):
#         print('Today:')
#         i = 0
#         for item in self.lst:
#             i += 1
#             print(f'{i}) {item}')
#
#
# tasks = ['Do yoga', 'Make breakfast', 'Learn basics of SQL', 'Learn what is ORM']
#
# today = TaskList(tasks)
#
# today.today()


# STAGE 2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# creating DB file
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# creating declarative meta class from which our Tasks class will inherit
Base = declarative_base()


# creating definition of the table in our Task class (child class to the Base)
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='')
    deadline = Column(Date, default=datetime.today)

    def __repr__(self):
        return self.task


# create a table in our DB
Base.metadata.create_all(engine)

# creating a session object to access our database
Session = sessionmaker(bind=engine)
session = Session()


# tasker main menu
def menu():
    choice = input('''1) Today's tasks
2) Add task
0) Exit\n''')
    return choice


# checking what's on today
def today_tasks():
    print('\nToday:')
    rows = session.query(Task).all()
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for item in rows:
            print(f'{item.id}. {item.task}')
        print('')


# adding a task for today to our DB
def add_task():
    new_task = input('Enter task\n')
    new_row = Task(task='{}'.format(new_task), deadline=datetime.today())
    session.add(new_row)
    session.commit()
    print('The task has been added!\n')
    # rows = session.query(Task).all()


# running the script
def main():
    while True:
        user_choice = menu()
        if user_choice == '1':
            today_tasks()
        elif user_choice == '2':
            add_task()
        elif user_choice == '0':
            print('\nBye!')
            break


main()