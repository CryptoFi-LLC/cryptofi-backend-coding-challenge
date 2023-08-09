import uvicorn

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 80
    uvicorn.run(
        host=host, port=port, app="api.main:app", reload=True, log_level="debug"
    )
