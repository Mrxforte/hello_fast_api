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
async def user(user: str, age: int) -> dict:
    return {"user": user, "age": age}