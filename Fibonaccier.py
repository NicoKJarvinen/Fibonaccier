import asyncio
import random
import time

# Fibonacci number function
async def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return await fib(n - 1) + await fib(n - 2)

async def main():
    number_of_calls = 2

    n = int(input("Enter a positive number (n): "))

    if n < 0:
        print("Please enter a positive number.")
        return

    # Function that calculates and returns the Fibonacci number with random delay up to 1 second
    async def fib_with_delay(task_id):
        start = time.time()  
        await asyncio.sleep(random.random())
        result = await fib(n)
        end = time.time()  
        elapsed_time = end - start
        return task_id, result, elapsed_time

    tasks = []

    # Create two asynchronous calls to the fib_with_delay function
    for number in range(number_of_calls): 
        task = asyncio.create_task(fib_with_delay(number))
        tasks.append(task)

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    results = []

    # Retrieve results and elapsed times
    for task in tasks:
        result = await task
        results.append(result)

    # Sort the results by elapsed time
    results.sort(key=lambda x: x[2])

    # Print the Fibonacci number and the first finished function call
    print(f"Fibonacci number of {n} = {results[0][1]}")
    print(f"Task {results[0][0]} finished first in {results[0][2]} seconds")

if __name__ == "__main__":
    asyncio.run(main())