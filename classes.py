"""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Course Name:        Software Engineering Part 2
Professor:          Hanna ABI AKL, DSTI
    --------------------------------------
Description:        OOP programming with Python - CLASSES
    --------------------------------------
Author:             Ronald LE PAPE
    --------------------------------------        
Date:               2025-02-28
Version:            1.0
    --------------------------------------
Classes :           Task
                    OrderBook

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""


class Task:
    '''
    ====================================================================================
    This class manages one developper's task
        - assigns a unique task number (id) to a new task
        - assigns a developper
        - assign a status (FINISHED / NOT FINISHED)
        - assign a workload
        - class method to mark task as finished
    ====================================================================================
    '''
    
    # class attribute ID_Count to be incremented by the constructor
    ID_Count = 0

    # CTOR
    def __init__(self, description, programmer, workload):
        type(self).ID_Count += 1            # incrementing ID_Count
        self.__id           = Task.ID_Count # storing current ID_Count as Task._ID. No need for setter for id -> I have to use __id directly ! 
        self.description    = description
        self.programmer     = programmer
        self.workload       = workload
        self.__status       = 0             # by default a Task is NOT FINISHED. No setter for status, therefore I use private attribute __status
                                            # No need for setter because there is a mark_finished() method

    
    # customizing __str__ for the print function
    def __str__(self):
        if self.__status == 0:
            return (str(self.id) + ": " + self.description + " (" + str(self.workload) + " hours), programmer " + self.programmer + " : NOT FINISHED")
        elif self.__status == 1:
            return (str(self.id) + ": " + self.description + " (" + str(self.workload) + " hours), programmer " + self.programmer + " : FINISHED")


    '''
    Getters and setters
    '''    
    # Getter for id. No need for setter. 
    @property
    def id(self):
         return self.__id
    
    # Getter and setter for description
    @property
    def description(self):
         return self.__description
    
    @description.setter
    def description(self, description):
         self.__description = description
         
    # Getter and setter for programmer
    @property
    def programmer(self):
         return self.__programmer
    
    @programmer.setter
    def programmer(self, programmer):
         self.__programmer = programmer

    # Getter and setter for workload
    @property
    def workload(self):
         return self.__workload
    
    @workload.setter
    def workload(self, workload):
         self.__workload = workload

    # Getter for status
    # -> get by is_finished() method

    # Setter for status
    # -> set by mark_finished() method

    '''
    Class methods
    '''
    # boolean representation of status
    def is_finished(self):
        if self.__status == 0:
             return False
        else:
             return True
    
    # method to mark status as FINISHED
    def mark_finished(self):
         self.__status = 1
        



class OrderBook:
    '''
    ====================================================================================
    This class manages the orders' list of the developpers team.
    Internally, the orders are tasks (class Tasks defined above).
        - adds an order (a task) to the OrderBook
        - displays all the orders
        - displays all the programmers
        - displays a list of finished orders
        - displays a list of unfinished orders        
        - displays all the orders of each programmer
        - marks an order as finished
        - dispalys a programmer's status

    ====================================================================================    
    '''

    #CTOR
    def __init__(self):
         self.__order_list = [] # Empty list. Will contain all the tasks/orders


    '''
    Getters and setters
    '''
    # None



    '''
    Class Methods
    '''
    # adding an order in the orderbook: creating a task object for each order, and appending it directly to __order_list
    def order_add(self, description, programmer, workload):
        self.__order_list.append(Task(description, programmer, workload))

    # method which returns the list of all orders
    def all_orders(self):
         return self.__order_list

    # method which returns the list of distinct programmers
    def programmers(self):
        self.__programmers_list = []

        for order in self.__order_list:
           
            self.__alreadyPresent = 0
            
            for programmer in self.__programmers_list:
                 if order.programmer == programmer:      # remember : an order is a task ! I can use the task's getter to retreive the programmer 
                     self.__alreadyPresent += 1
                     break  # we have a match : no need to continue
            if self.__alreadyPresent == 0:  # adding to the list if not already present
                     self.__programmers_list.append(order.programmer) 
        
        return self.__programmers_list
    
    # method which returns a dictionnary of programmers and their respective tasks
    def programmers_orderdict(self):
        self.__programmers_orders_dict = {}

        for order in self.__order_list:

            if self.__programmers_orders_dict.get(order.programmer, 0) == 0: # when programmer is not in the dict yet, get() returns 0, ...
                orders_list = [str(order.id)]
                self.__programmers_orders_dict.update({order.programmer : orders_list}) # .... then update() will create the new key and set the first value 
            else:
                orders_list = self.__programmers_orders_dict.get(order.programmer) + [str(order.id)] # else : concatenating current task ID to the existing list of task IDs for the programmer
                self.__programmers_orders_dict.update({order.programmer : orders_list})

        return self.__programmers_orders_dict  
             
    # method which marks an order as FINISHED
    def mark_finished(self, order_id):
        self.__count = 0

        for order in self.__order_list: # Remember : looping through __order_list = looping through a list of task objects
             if order.id == order_id:
                  order.mark_finished() # -> finishing an order = finishing a task
                  self.__count += 1
        if self.__count == 0:
             raise ValueError("No order id=" + str(order_id) + " could be found !")
    
    # method which returns a list of NOT FINISHED orders
    def notfinished_orders(self):
         self.__notfinished_orders = []
         for order in self.__order_list:
              if not order.is_finished():
                   self.__notfinished_orders.append(order)
         return self.__notfinished_orders

    # method which returns a list of FINISHED orders
    def finished_orders(self):
         self.__finished_orders = []
         for order in self.__order_list:
              if order.is_finished():
                   self.__finished_orders.append(order)
         return self.__finished_orders
    
    # method which returns an order (= a task) by its id. Used in status_of_programmer()
    def get_order_by_id(self, order_id):
        for order in self.__order_list:
             if order.id == order_id:
                  return order        
         
    # Decorator pretty_status() which augments/beautifies OrderBook.status_of_programmer()'s output without changing its code
    @staticmethod
    def pretty_status(func):
        def inner(*args, **kwargs):
            programmer_status = func(*args, **kwargs)
            print("Tasks: finished {0} not finished {1}, Hours: done {2} scheduled {3}".format(programmer_status[0], programmer_status[1], programmer_status[2], programmer_status[3]))            
            return programmer_status
        return inner

    # method which returns the status of a programmer in a tuple
    # (number of finished orders, number of unfinished orders, workload of finished orders, workload of unfinished orders)
    # using a decorator to beautify the output without changing class method's code
    @pretty_status
    def status_of_programmer(self, programmer_name):
         
        self.__orders_dict = self.programmers_orderdict() # reusing the programmers' dictionnary feature as it contains orders grouped by programmer

        if self.__orders_dict.get(programmer_name, 0) == 0: # raising an error if programmer not found in the OrderBook
             raise ValueError("No programmer has the name " + programmer_name + " !")
        
        # initializing tuple values
        self.__total_finished_orders            = 0
        self.__total_unfinished_orders          = 0
        self.__total_workload_finished_orders   = 0
        self.__total_workload_unfinished_orders = 0


        # Reminder : dictionnary __orders_dict looks like this :
        # {'Adele': ['1', '2', '3', '5', '7'], 'Ronald': ['4', '9', '10'], 'Eric': ['6'], 'Robert': ['8']}

        # for each order of provided programmer, I count the finished/unfinished tasks and aggregate the corresponding workloads
        for order_id in self.__orders_dict.get(programmer_name):
            current_order = self.get_order_by_id(int(order_id)) # get order/task object by its id

            # counting tasks and aggregating workloads.....
            if not current_order.is_finished():
                  self.__total_unfinished_orders += 1
                  self.__total_workload_unfinished_orders += current_order.workload
            else:
                  self.__total_finished_orders += 1
                  self.__total_workload_finished_orders += current_order.workload

        # returning the tuple
        return (self.__total_finished_orders, self.__total_unfinished_orders, self.__total_workload_finished_orders, self.__total_workload_unfinished_orders)
    

               










         