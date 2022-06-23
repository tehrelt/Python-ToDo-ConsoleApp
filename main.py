import os
from db import *

while True:
    print('0. Exit')
    print('1. Add task')
    print('2. Update task')
    print('3. Print tasks')
    
    key = input('Enter a task number: ')
    match key:
        case '1':
            title = input('Enter a title: ')
            body = input('Enter a body: ')
            state = input('State (todo - 0, inprogress - 1, done - 2)')
            insert_task(str(title), str(body), int(state))

        case '2':
            id = input('Enter an id: ')
            state = input('State (todo - 0, inprogress - 1, done - 2)')
            update_state_task(int(id), int(state))
        case '3':
            print_tasks()

        case 'clear':
            clear_table()
        case '0': 
            break


