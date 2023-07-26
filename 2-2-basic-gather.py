# 2-2-basic-gather.py
import asyncio
import time

# hello function
async def hello(i):
    # print start hello function
    print(f"{time.ctime()} hello {i} started")
    # sleep 4 seconds using asyncio library
    await asyncio.sleep(4)
    # print end hello function
    print(f"{time.ctime()} hello {i} done")

# main function
async def main():
    # create task to call function hello with argument 1
    task1 = asyncio.create_task(hello(1)) # returns immediately, the task is created
    #await asyncio.sleep(3)
    # create task to call function hello with argument 2
    task2 = asyncio.create_task(hello(2))
    # call task1 and task2 gather
    await asyncio.gather(task1, task2)

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
# Wed Jul 26 14:38:29 2023 hello 1 started
# Wed Jul 26 14:38:29 2023 hello 2 started
# Wed Jul 26 14:38:33 2023 hello 1 done
# Wed Jul 26 14:38:33 2023 hello 2 done
# Time: 4.00 sec
#