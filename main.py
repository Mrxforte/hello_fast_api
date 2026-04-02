from fastapi import FastAPI, Path
import asyncio
app = FastAPI(debug=True, title="My API", description="This is a sample API", version="1.0.0")
@app.get("/")
async def index():
    await asyncio.sleep(5)  # Simulate a delay
    return {"message": "Hello World", "description": "You are waited 5 seconds to see this message"} 

@app.get("/second")
async def second():
    await asyncio.sleep(5)  # Simulate a delay
    return {"message": "This is the second endpoint"}

# adding the dict enpoint to the app
@app.get("/user/{user}/{age}")
async def get_user(user: str, age: int):
    await asyncio.sleep(5)  # Simulate a delay
    return {"user": user, "age": age, "message": "User details fetched successfully"}

# using the multiple params in the app
@app.get("/fullname/{first_name}/{last_name}")
async def get_fullname(first_name: str, last_name: str):
    await asyncio.sleep(5)  # Simulate a delay
    return {"full_name": f"{first_name} {last_name}", "message": "Full name fetched successfully simulated 5 seconds delay"}

@app.get("/usercoding/{username}/{language}")
async def get_user_coding(username: str, language: str):
    await asyncio.sleep(5)  # Simulate a delay
    return {"username": username, "language": language, "message": "User coding details fetched successfully simulated 5 seconds delay"}

# simulating the order id  for the user 
@app.get("/order/{order_id}")
async def get_order(order_id: int) -> dict:
    await asyncio.sleep(5)  # Simulate a delay
    return {"order_id": order_id, "message": "Order details fetched successfully simulated 5 seconds delay"}