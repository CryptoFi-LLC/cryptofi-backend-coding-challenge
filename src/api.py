from fastapi import FastAPI


app = FastAPI(
    title="CryptoFi Backend Coding Challenge",
)


@app.get("/")
def hello_world():
    """
    NOTE: This is route is used as an example for the test suite
    No action needed here
    """
    return {"hello": "world"}


@app.get("/recurring-orders")
def get_recurring_orders():
    return {}


@app.post("/recurring-orders")
def post_recurring_orders():
    return {}
