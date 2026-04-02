from fastapi import FastAPI, Path

app = FastAPI(debug=True, title="My API", description="This is a sample API", version="1.0.0")
@app.get("/")
def index():
    return {"message": "Hello World"} 

@app.get("/second")
async def second():
    return {"message": "This is the second endpoint"}