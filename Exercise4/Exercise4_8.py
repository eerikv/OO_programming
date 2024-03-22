# File name:    Exercise4_8.py
# Author:       Eerik Vainio
# Description:  A program to handle orders in form of tasks. Tasks have data
#               such as a description, programmer, workload, if the task is finished
#               or not, and id.

class Task:
    id_counter = 1

    def __init__(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.id_counter
        Task.id_counter += 1

    def __str__(self):
        if self.finished:
            return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED'
        else:
            return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED'

    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        programmers = set()
        for x in self.orders:
            programmers.add(x.programmer)
        return list(programmers)
    
    def mark_finished(self, id: int):
        for x in self.orders:
            if x.id == id:
                x.mark_finished()

    def finished_orders(self):
        order_list = []
        for x in self.orders:
            if x.finished:
                order_list.append(x)
        return order_list

    def unfinished_orders(self):
        order_list = []
        for x in self.orders:
            if not x.finished:
                order_list.append(x)
        return order_list
    
    def status_of_programmer(self, programmer: str):
        finished_tasks = unfinished_tasks = finished_workload = unfinished_workload = 0
        for x in self.orders:
            if x.programmer == programmer:
                if x.is_finished():
                    finished_tasks += 1
                    finished_workload += x.workload
                else:
                    unfinished_tasks += 1
                    unfinished_workload += x.workload

        """ if (finished_tasks == 0 & unfinished_tasks == 0):
            raise ValueError("Programmer not found")
        else: """
        programmer_status = (finished_tasks, unfinished_tasks, finished_workload, unfinished_workload)
        return programmer_status



# Part 1
""" t1 = Task("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())
t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3) """

# Part 2
""" orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

for order in orders.all_orders():
    print(order)

print()

for programmer in orders.programmers():
    print(programmer) """

# Part 3
""" orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

orders.mark_finished(1)
orders.mark_finished(2)

for order in orders.all_orders():
    print(order) """

# Part 4
""" orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status) """


# Game

orders = OrderBook()
print("commands:\n0 exit\n1 add order\n2 list finished tasks\n3 list unfinished tasks\n4 mark task as finished\n5 programmers\n6 status of programmer")

# Game loop
while True:
    user_input = input("command: ")

    match user_input:
        case "0":
            break
        case "1":
            description = input("description: ")
            programmer_and_workload = input("programmer and workload estimate: ").split()
            if (len(programmer_and_workload) != 2):
                print("erroneous input")
            elif (not programmer_and_workload[0].isalpha() or not programmer_and_workload[1].isnumeric()):
                print("erroneous input")
            else:
                orders.add_order(description, str(programmer_and_workload[0]), int(programmer_and_workload[1]))
                print("added!")
        case "2":
            finished_list = []
            for x in orders.finished_orders():
                finished_list.append(x)
            if len(finished_list) > 0:
                for x in finished_list:
                    print(x)
            else:
                print("no finished tasks")
        case "3":
            unfinished_list = []
            for x in orders.unfinished_orders():
                unfinished_list.append(x)
            if len(unfinished_list) > 0:
                for x in unfinished_list:
                    print(x)
            else:
                print("no unfinished tasks")
        case "4":
            id = input("id: ")
            for x in range(len(orders.all_orders())):
                if orders.all_orders()[x].id == int(id):
                    orders.mark_finished(orders.all_orders()[x].id)
                    print("marked as finished")
                    break
            print("erroneous input")
        case "5":
            for x in orders.programmers():
                print(x)
        case "6":
            programmer = input("programmer: ")
            status = orders.status_of_programmer(programmer)
            print(f'tasks: finished {status[0]} not finished {status[1]} done {status[2]} scheduled {status[3]}')
                

        
    print("")
