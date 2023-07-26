# 1-1-simple-sync.py
import time

# Sleep Function
def sleep():
    # Print time when sleep is called
    print(f'Time : {time.time() - start:.2f}')
    # Sleep for one second
    time.sleep(1)

# Sum Function : argument name as task name and numbers is number list
def sum(name, numbers):
    total = 0
    # from number list
    for number in numbers:
        # print task name and total of (total + number)
        #                     example : 0+1 = 1
        print(f'Task {name}: Computing {total}+{number}')
        # take sleep time one second
        sleep()
        # add number to total
        total += number
    # total sum of all numbers in list
    print(f'Task {name}: Sum = {total}\n')

# init start time
start = time.time()
# init tasks list
tasks = [
    # Task A : 1+2
    sum("A", [1,2]),
    # Task B : 1+2+3
    sum("B", [1,2,3])
]
# init end time
end = time.time()
# calculate time when tasks used
print(f'Time {end-start:.2f} sec')

#
# Task A: Computing 0+1
# Time : 0.00
# Task A: Computing 1+2
# Time : 1.01
# Task A: Sum = 3

# Task B: Computing 0+1
# Time : 2.01
# Task B: Computing 1+2
# Time : 3.01
# Task B: Computing 3+3
# Time : 4.02
# Task B: Sum = 6

# Time 5.02 sec
#