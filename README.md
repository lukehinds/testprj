# Echo API

A simple REST API that echoes back whatever data is sent in the request.

## Features

- POST endpoint `/echo` that returns the request body
- Simple health check endpoint at `/`
- FastAPI-powered with automatic OpenAPI documentation

## Requirements

- Python 3.8+
- Poetry for dependency management

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd echo-api
```

2. Install dependencies using Poetry:
```bash
poetry install
```

## Running the API

1. Start the server:
```bash
poetry run python main.py
```

Or alternatively:
```bash
poetry run uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Usage

### Echo Endpoint

Send a POST request to `/echo` with any JSON body:

```bash
curl -X POST http://localhost:8000/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, World!"}'
```

Response:
```json
{
  "echo": {
    "message": "Hello, World!"
  }
}
```

### API Documentation

FastAPI provides automatic interactive API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

- Format code using Black: `poetry run black .`
- Run linting: `poetry run flake8`
- Run tests: `poetry run pytest`