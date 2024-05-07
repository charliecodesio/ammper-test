from fastapi import FastAPI
from routers.product import router as product_router
app = FastAPI()



@app.get('/')
def message():
    return "Hello!"

app.include_router(product_router)