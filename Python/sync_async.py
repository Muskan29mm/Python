# Python code for synchronous programming

# import time
#
# def task(name, delay):
#     print(f"Starting task : {name}")
#     time.sleep(delay)
#     print(f"Ending task : {name}")
#
# def main():
#     start_time = time.time()
#
#     task("task1", 6)
#     task("task2", 4)
#     task("task3", 2)
#
#     end_time = time.time()
#     print(f"Total Execution time: {end_time - start_time:.2f} seconds ")
# 
# if __name__ == "__main__":
#     main()

# Python code for asynchronous programming
import asyncio

async def func():
    print("Hello")
    await asyncio.sleep(5)
    print("Hello World!")

asyncio.run(func())