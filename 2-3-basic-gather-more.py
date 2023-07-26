# 2-1-basic-gather-more.py
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
    # create tasks list hello function with arguments 0-9
    coros = [hello(i) for i in range(10)]
    # call list of tasks gather
    await asyncio.gather(*coros)

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
# Wed Jul 26 14:38:55 2023 hello 0 started
# Wed Jul 26 14:38:55 2023 hello 1 started
# Wed Jul 26 14:38:55 2023 hello 2 started
# Wed Jul 26 14:38:55 2023 hello 3 started
# Wed Jul 26 14:38:55 2023 hello 4 started
# Wed Jul 26 14:38:55 2023 hello 5 started
# Wed Jul 26 14:38:55 2023 hello 6 started
# Wed Jul 26 14:38:55 2023 hello 7 started
# Wed Jul 26 14:38:55 2023 hello 8 started
# Wed Jul 26 14:38:55 2023 hello 9 started
# Wed Jul 26 14:38:59 2023 hello 0 done
# Wed Jul 26 14:38:59 2023 hello 1 done
# Wed Jul 26 14:38:59 2023 hello 2 done
# Wed Jul 26 14:38:59 2023 hello 3 done
# Wed Jul 26 14:38:59 2023 hello 4 done
# Wed Jul 26 14:38:59 2023 hello 5 done
# Wed Jul 26 14:38:59 2023 hello 6 done
# Wed Jul 26 14:38:59 2023 hello 7 done
# Wed Jul 26 14:38:59 2023 hello 8 done
# Wed Jul 26 14:38:59 2023 hello 9 done
# Time: 4.00 sec
#