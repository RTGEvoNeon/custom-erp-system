from fastapi import FastAPI

app = FastAPI()

@app.get("/orders")
async def get_all_orders():
    return
