"""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Course Name :       Software Engineering Part 2
Professor :         Hanna ABI AKL, DSTI

    --------------------------------------
Description:       OOP programming with Python - MAIN PROGRAM
Author:            Ronald LE PAPE

    --------------------------------------        
Date:               2025-02-28
Version:            1.0
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



Contains a program which creates and manages the OrderBook of a software company


"""


# importing classes from classes.py
from classes import *
# importing OS in order to use "cls" ("clear screen") in interactive mode
import os



'''
!!!!! README README README README README README README README README README README !!!!!
'''
EXECUTION_MODE = 1        # 0 => developping mode => showing PART 1 to PART 5
                          # 1 => the program starts at PART6 (user menu/interactive part)




#==========================================================
# MAIN
#==========================================================
if __name__ == '__main__':
    

    if EXECUTION_MODE == 0:   # 0 => developping mode => showing PART 1 to PART 5

        '''
        PART 1
        '''
        print()        
        print("=====================================================================")
        print("         PART 1")
        print("=====================================================================")

        print()
        print("----------------------------------")                
        print("Tasks:")        
        print("----------------------------------")
        print()
        # Tasks operations        

        t1 = Task("program hello world", "Eric", 3)
        print(t1.id, t1.description, t1.programmer, t1.workload)
        print(t1)
        print(t1.is_finished())
        t1.mark_finished()
        print(t1)
        print(t1.is_finished())
        t2 = Task("program webstore", "Adele", 10)
        print(t2)


        '''
        PART 2
        '''
        print()
        print("=====================================================================")
        print("         PART 2")
        print("=====================================================================")        
        
        # creating an empty OrderBook
        orders = OrderBook()

        # adding some orders
        orders.order_add("program webstore", "Adele", 10)
        orders.order_add("program mobile app for workload accounting", "Eric", 25)
        orders.order_add("program app for practising mathematics", "Adele", 100)

        # printing all the orders
        print()
        print("----------------------------------")                
        print("All the orders:")        
        print("----------------------------------")        
        for order in orders.all_orders():
             print(order)     # each order is in fact a task in disguise -> print() will then use Task's __str__() !
             
        print()
        
        print()
        print("----------------------------------")                
        print("All the programmers:")        
        print("----------------------------------")         
        # printing a list of programmers present in the OrderBook
        for programmer in orders.programmers():
               print(programmer)
        print()

        '''
        PART 3
        '''
        print()
        print("=====================================================================")
        print("         PART 3")
        print("=====================================================================") 

        # printing a dictionnary of programmers' orders
        print()
        print("----------------------------------")                
        print("Dictionnary of orders, by programmer:")       
        print("----------------------------------")
        print(orders.programmers_orderdict())
        print()

        '''
        PART 4
        '''
        print()
        print("=====================================================================")
        print("         PART 4")
        print("=====================================================================") 
        print()

        # marking orders 3 and 4 as FINISHED
        orders.mark_finished(3)
        orders.mark_finished(4)
        
        # printing all the orders
        print("----------------------------------")                
        print("All the orders, after orders id=3 and id=4 are marked as FINISHED:")       
        print("----------------------------------")                
        for order in orders.all_orders():
             print(order)
        print()      
     
        # printing NOT FINISHED orders
        print("----------------------------------")                
        print("All NOT FINISHED orders:")       
        print("----------------------------------")        
        for order in orders.notfinished_orders():
            print(order)
        print()

        # printing FINISHED orders
        print("----------------------------------")                
        print("All FINISHED orders:")       
        print("----------------------------------")        
        for order in orders.finished_orders():
            print(order)
        print()            


        '''
        PART 5
        '''
        print()
        print("=====================================================================")
        print("         PART 5")
        print("=====================================================================") 
        print()
        # showing the status of a programmer
        print("----------------------------------")                
        print("Status of programmer Adele (Decorated version followed by undecorated/raw version):")       
        print("----------------------------------")
        status = orders.status_of_programmer("Adele")        
        print(status)
        print()

        exit() # end of execution_mode 0




    # if execution_mode == 1 : user interactive mode
    elif EXECUTION_MODE == 1:


        '''
        PART 6
        '''        

        # Clearing the Screen
        os.system('cls')

        # creating OrderBook
        orders = OrderBook()

        # Menu list
        menu_list = "0: exit\n1: add order\n2: list finished tasks\n3: list unfinished tasks\n4: mark task as finished\n5: programmers\n6: status of programmer\n7: display menu"
        
        # list of autorized command numbers, in order to check user input 
        commands_dict = {  
        '0': "0",
        '1': "1",
        '2': "2",
        '3': "3",
        '4': "4",
        '5': "5",
        '6': "6",
        '7': "7"}

        print("----------------------------------")
        print(menu_list)
        print("----------------------------------")
        print()
     
        while True:
            user_command = input("command: ")

            # checking the existence of user's input
            if commands_dict.get(user_command, 0) == 0:      
                print("\nunknown command number. Type 7 to print menu")
                print()  

            # taking actions.....
            if user_command == str(0):       # 0: exiting program
                exit()

            elif user_command == str(1):     # 1: adding an order
                try:
                    description     = input("description: ")
                    prog_work       = input("programmer and workload estimate: ")
                    programmer      = prog_work.split(" ")[0]
                    workload        = int(prog_work.split(" ")[1])
                    orders.order_add(description, programmer, workload)
                    print("added!")
                except Exception:
                    print("erroneous input")
                print()
               
            elif user_command == str(2):     #2:  printing list of finished orders
                if len(orders.finished_orders()) != 0:
                    for order in orders.finished_orders():
                        print(order)
                else:
                    print("no finished tasks")
                print()

            elif user_command == str(3):     #3: printing list of unfinished orders
                if len(orders.notfinished_orders()) != 0:
                    for order in orders.notfinished_orders():
                        print(order)
                else:
                    print("no unfinished tasks")
                print() 

            elif user_command == str(4):     #4: marking an order as finished
                try:
                    order_id = input("id: ")             
                    orders.mark_finished(int(order_id))
                    print("marked as finished")
                except Exception:
                    print("erroneous input")
                print()

            elif user_command == str(5):     #5: printing the list of programmers
                if len(orders.programmers()) != 0:
                    for programmer in orders.programmers():
                       print(programmer)
                else:
                     print()
                     print("empty OrderBook !")                        
                print()

            elif user_command == str(6):     # 6: printing programmer's status
                try:
                   programmer = input("programmer: ")
                   status = orders.status_of_programmer(programmer) # the output is printed by the decorator pretty_status() !
                except Exception:
                    print("erroneous input") 
                print()

            elif user_command == str(7):     # 7: printing menu
                print()
                print(menu_list)
                print()
            


