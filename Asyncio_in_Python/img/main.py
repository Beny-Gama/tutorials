
import asyncio
# Define a coroutine that simulates a time-consuming task.
async def fetch_data(delay):
    print ("1 - Fetching data...")
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep.
    print ("2 - Data fetched")
    return {"data": "Some data"}
    # Return some data.

# Define another coroutine that calls the first coroutine
async def main():
    print ("3 - Start of main coroutine")
    task = fetch_data(2)    
    print ("4 - End of main coroutine")
    result = await task
    print (f"5 - Received result: {result}")

# Run the main coroutine
asyncio.run(main())