from fastapi import FastAPI
from pydantic import BaseModel

from app.telegram_bot import send_telegram_message
from app.logger import log_event

app = FastAPI()


class AlertData(BaseModel):
    alert: str
    symbol: str
    price: str


@app.get("/")
async def home():
    return {"status": "running"}


@app.post("/webhook")
async def webhook(data: AlertData):

    message = f"""
🚨 GRID ALERT

Type: {data.alert}
Symbol: {data.symbol}
Price: {data.price}
"""

    send_telegram_message(message)

    log_event(message)

    return {"status": "success"}