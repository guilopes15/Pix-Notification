import os

from dotenv import load_dotenv
from fastapi import FastAPI
from telegram import Bot

from .schema import Message

load_dotenv()

bot = Bot(token=os.getenv('API_TOKEN'))
chat_id = os.getenv('CHAT_ID')

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Ola'}


@app.post('/send', response_model=Message)
async def bot_sends_notification(data: Message):
    await bot.send_message(chat_id=chat_id, text=data.message)
    return {'message': 'OK'}
