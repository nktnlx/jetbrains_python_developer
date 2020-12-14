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
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Date
# from sqlalchemy.orm import sessionmaker
# from datetime import datetime
#
# # creating DB file
# engine = create_engine('sqlite:///todo.db?check_same_thread=False')
#
# # creating declarative meta class from which our Tasks class will inherit
# Base = declarative_base()
#
#
# # creating definition of the table in our Task class (child class to the Base)
# class Task(Base):
#     __tablename__ = 'task'
#     id = Column(Integer, primary_key=True)
#     task = Column(String, default='')
#     deadline = Column(Date, default=datetime.today)
#
#     def __repr__(self):
#         return self.task
#
#
# # create a table in our DB
# Base.metadata.create_all(engine)
#
# # creating a session object to access our database
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# # tasker main menu
# def menu():
#     choice = input('''1) Today's tasks
# 2) Add task
# 0) Exit\n''')
#     return choice
#
#
# # checking what's on today
# def today_tasks():
#     print('\nToday:')
#     rows = session.query(Task).all()
#     if len(rows) == 0:
#         print('Nothing to do!')
#     else:
#         for item in rows:
#             print(f'{item.id}. {item.task}')
#         print('')
#
#
# # adding a task for today to our DB
# def add_task():
#     new_task = input('Enter task\n')
#     new_row = Task(task='{}'.format(new_task), deadline=datetime.today())
#     session.add(new_row)
#     session.commit()
#     print('The task has been added!\n')
#     # rows = session.query(Task).all()
#
#
# # running the script
# def main():
#     while True:
#         user_choice = menu()
#         if user_choice == '1':
#             today_tasks()
#         elif user_choice == '2':
#             add_task()
#         elif user_choice == '0':
#             print('\nBye!')
#             break
#
#
# main()


# STAGE 3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from datetime import datetime, timedelta

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


# creating our TaskList class
class TaskList:
    def __init__(self):
        # creating a session object to access our database
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        self.menu()

    # main menu and handling user's choices
    def menu(self):
        choice = input('''1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit\n''')
        if choice == '1':  # Today's tasks
            self.today_tasks()
        elif choice == '2':  # Week's tasks
            self.week_tasks()
        elif choice == '3':  # All tasks
            self.all_tasks()
        elif choice == '4':  # Add task
            self.add_task()
        elif choice == '0':  # Exit
            self.exit()

    # printing tasks from database
    def today_tasks(self):
        rows = self.session.query(Task).all()
        today = datetime.today()
        print('\nToday', today.day, today.strftime('%b') + ':')
        if len(rows) == 0:
            print('Nothing to do!\n')
            return self.menu()
        i = 1
        for row in rows:
            if row.deadline == today.date():
                print(f'{i}. {row.task}')
                i += 1
        if i == 1:
            print('Nothing to do!\n')
        print('')
        self.menu()

    # printing all tasks for the next 7 days from today.
    def week_tasks(self):
        today = datetime.today()
        # filtering tasks (today + 7 days)
        rows = self.session.query(Task).filter(and_(Task.deadline <= today.date() + timedelta(days=6), Task.deadline >= today.date())).order_by(Task.deadline).all()
        # creating an auxiliary lists with the next 7 days and days where we have tasks
        all_days_lst = [int(today.strftime('%d')) + _ for _ in range(7)]
        task_days_lst = [row.deadline.day for row in rows]
        # printing the output formatted as asked by the task
        print('')
        for i in range(7):
            today = datetime.today() + timedelta(days=i)
            print(today.strftime('%A %d %b') + ':')
            if int(today.strftime('%d')) in task_days_lst:  # checking if we have a task on this day
                i = 1
                for row in rows:
                    if row.deadline.day == int(today.strftime('%d')):
                        print(f'{i}. {row.task}')
                        i += 1
                print('')
            else:
                print('Nothing to do!\n')
        self.menu()

    # printing all tasks from database
    def all_tasks(self):
        rows = self.session.query(Task).order_by(Task.deadline).all()
        if len(rows) == 0:
            print('\nAll tasks:')
            print('Nothing to do!\n')
            self.menu()
        else:
            print('\nAll tasks:')
            i = 1
            for row in rows:
                print(f'{i}. {row.task}. {row.deadline.day}', row.deadline.strftime('%b'))
                i += 1
            print('')
            self.menu()

    # adding a task to database
    def add_task(self):
        task_to_add = input('\nEnter task\n')
        task_deadline = input('Enter deadline\n')
        new_task = Task(task=task_to_add, deadline=datetime.strptime(task_deadline, '%Y-%m-%d').date(),)
        self.session.add(new_task)
        self.session.commit()
        print('The task has been added!\n')
        self.menu()

    # exiting the script
    def exit(self):
        print('\nBye!')
        return


my_day = TaskList()
