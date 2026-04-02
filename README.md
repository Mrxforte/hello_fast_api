# Hello FastAPI

A compact FastAPI playground with a few path-parameter examples, clean JSON responses, and an intentional `5-second` delay on every endpoint to simulate async work.

## Overview

This project is a small learning app built with FastAPI. It demonstrates:

- basic route creation
- async endpoint handlers
- path parameters with strings and integers
- automatic API docs from FastAPI
- delayed responses using `asyncio.sleep(5)`

## Features

- `GET /` welcome endpoint
- `GET /second` secondary demo endpoint
- `GET /user/{user}/{age}` dynamic user details
- `GET /fullname/{first_name}/{last_name}` full-name formatter
- `GET /usercoding/{username}/{language}` coding profile endpoint
- `GET /order/{order_id}` typed integer order lookup

## Tech Stack

- Python
- FastAPI
- Uvicorn
- asyncio

## Project Structure

```text
hello_fast_api/
|-- main.py
|-- README.md
```

## Getting Started

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn
```

### 3. Run the app

```bash
uvicorn main:app --reload
```

The server will usually start at:

```text
http://127.0.0.1:8000
```

## Interactive API Docs

FastAPI generates docs automatically:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns a hello message |
| GET | `/second` | Returns a second sample response |
| GET | `/user/{user}/{age}` | Returns a user name and age |
| GET | `/fullname/{first_name}/{last_name}` | Combines first and last name |
| GET | `/usercoding/{username}/{language}` | Returns username and favorite language |
| GET | `/order/{order_id}` | Returns an order id and message |

## Example Requests

### Root

```bash
curl http://127.0.0.1:8000/
```

Response:

```json
{
  "message": "Hello World",
  "description": "You are waited 5 seconds to see this message"
}
```

### User Details

```bash
curl http://127.0.0.1:8000/user/Azamat/25
```

Response:

```json
{
  "user": "Azamat",
  "age": 25,
  "message": "User details fetched successfully"
}
```

### Full Name

```bash
curl http://127.0.0.1:8000/fullname/John/Doe
```

Response:

```json
{
  "full_name": "John Doe",
  "message": "Full name fetched successfully simulated 5 seconds delay"
}
```

### Coding Profile

```bash
curl http://127.0.0.1:8000/usercoding/alice/python
```

Response:

```json
{
  "username": "alice",
  "language": "python",
  "message": "User coding details fetched successfully simulated 5 seconds delay"
}
```

### Order Lookup

```bash
curl http://127.0.0.1:8000/order/101
```

Response:

```json
{
  "order_id": 101,
  "message": "Order details fetched successfully simulated 5 seconds delay"
}
```

## Important Note

Every endpoint intentionally waits `5 seconds` before responding. This is part of the current app behavior and is useful for testing async responses or simulating slow operations.

## Main Application

The FastAPI app is defined in [main.py](main.py).

## Next Improvements

- add a `requirements.txt` file
- improve response text grammar
- add query parameters and request validation examples
- add unit tests for endpoints

---

Built with FastAPI for learning and experimentation.