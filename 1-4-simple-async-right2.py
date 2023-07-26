# 1-4-simple-async-right2.py
import asyncio
import time

# Sleep Function
async def sleep():
    # Print time when sleep is called
    print(f'Time: {time.time() - start:.2f}')
    # Sleep for one second using asyncio library
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

# main function
async def main():
    # Make task run gather
    await asyncio.gather(sum("A", [1,2]), sum("B", [1,2,3]))

if __name__ == '__main__':
    # init start time
    start = time.time()
    # asyncio run main function
    asyncio.run(main())
    # init end time
    end = time.time()
    # calculate time when main function used
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

# Time: 3.01 sec
#