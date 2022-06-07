
class ToDo:
    def __init__(self):
        self.todo = {}

    def add_task(self, task='', time='', importance=''):
        self.todo[task] = [time, importance]

    def delete_task(self, task):
        del self.todo[task]

    def print_tasks(self):
        for i, k in self.todo.items():
            print(f'Task: {i}, time: {k[0]}, importance: {k[1]}', end='\n\n')


def get_data_fig(*args, **kwargs):
    print(kwargs)
    s = ['type', 'color', 'closed', 'width']
    a = args[0]+args[1]+args[2]
    p = [a,]
    for i in s:
        if i in kwargs:
            print(i)
            s.append(kwargs[i])
    return tuple(p)

print(get_data_fig(1,2,3,{'type':'gavno'}))