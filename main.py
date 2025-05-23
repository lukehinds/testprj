from fastapi import FastAPI, Request
import uvicorn

app = FastAPI(title="Echo API", description="A simple API that echoes back request data")

@app.post("/echo")
async def echo(response: Request):  # Bug: parameter name should be 'request'
    """
    Endpoint that echoes back whatever is sent in the request body
    """
    body = await response.json()  # Bug: 'response' is a misleading name; intended to be 'request'
    return {"echo": body}

@app.get("/")
async def root():
    """
    Root endpoint that provides basic information
    """
    return {"message": "Welcome to Echo API. Send POST requests to /echo endpoint"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
