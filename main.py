from todo import ToDo


def main():
    todo = ToDo()
    while True:
        print('Write "stop" if you want: ')
        task = input('Task: ')
        if task == 'stop':
            break
        time = input('Time: ')
        if time == 'stop':
            break
        importance = input('Importance: ')
        if importance == 'stop':
            break
        todo.add_task(task=task, time=time, importance=importance)
    todo.print_tasks()


if __name__ == '__main__':
    main()
