# 3-basic-fac.py
import asyncio
import time

# factorial function : n!
async def factorial(n):
    # init factorial as 1
    f = 1
    # for range from 2 to n
    for i in range(2, n + 1):
        # print start factorial function
        print(f"{time.ctime()} : Computing factorial({n}), currently i={i}...")
        # sleep 1 second using asyncio library
        await asyncio.sleep(1)
        # multiply i to factorial
        f *= i
    # return factorial
    return f

# main function
async def main():
    # run factorial function with argument 2,3,4 gather
    L = await asyncio.gather(factorial(2),factorial(3),factorial(4))
    # print result of factorial function with argument 2,3,4
    print(L) # [2, 6, 24]

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
# Wed Jul 26 14:53:04 2023 : Computing factorial(2), currently i=2...
# Wed Jul 26 14:53:04 2023 : Computing factorial(3), currently i=2...
# Wed Jul 26 14:53:04 2023 : Computing factorial(4), currently i=2...
# Wed Jul 26 14:53:05 2023 : Computing factorial(3), currently i=3...
# Wed Jul 26 14:53:05 2023 : Computing factorial(4), currently i=3...
# Wed Jul 26 14:53:06 2023 : Computing factorial(4), currently i=4...
# [2, 6, 24]
# Time: 3.00 sec
#