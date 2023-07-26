# 1-3-simple-async-right.py
import asyncio
import time

# Sleep Function
async def sleep():
    # Print time when sleep is called
    print(f'Time: {time.time() - start:.2f}')
    # Sleep for one second using asyncio library : this will be right
    await asyncio.sleep(1)

# Sum Function : argument name as task name and numbers is number list
async def sum(name,numbers):
    # init total number as 0
    total = 0
    # from number list
    for number in numbers:
        # print task name and total of (total + number)
        print(f'Task {name}: Computing {total}+{number}')
        # await sleep for 1 second
        await sleep()
        # add number to total
        total += number
    # total sum of all numbers in list
    print(f'Task {name}: Sum = {total}\n')

# init start time
start = time.time()

# create asyncio loop
loop = asyncio.get_event_loop()
# create loop task as list
tasks = [
    # Task A : 1+2
    loop.create_task(sum("A", [1,2])),
    # Task B : 1+2+3
    loop.create_task(sum("B", [1,2,3]))
]
# run loop with wait tasks
loop.run_until_complete(asyncio.wait(tasks))
# close loop
loop.close()

# init end time
end = time.time()
# calculate time when loop used
print(f'Time: {end-start:.2f} sec')

#
# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.00
# Task B: Computing 1+2
# Time: 1.00
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.00
# Task B: Sum = 6

# Time: 3.00 sec
#