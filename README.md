# Simple FastAPI Server

This is a basic FastAPI server with a simple endpoint.

## Setup

1. Install the requirements:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python main.py
```

Or alternatively:
```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## Available Endpoints

- `GET /` - Returns a "Hello World" message
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation 