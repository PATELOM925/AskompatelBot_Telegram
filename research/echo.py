from aiogram import Bot, Dispatcher, types, executor 
from dotenv import load_dotenv
import os
import logging

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

#configuring logging
logging.basicConfig(level=logging.INFO)

#intialize our bot 
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
#creating a decorator
async def command_start_handler(message: types.Message):
    await message.reply("HI,\nI am Trial/Research bot!,\nBuilt by OM M. PATEL")
    
    
@dp.message_handler() 
#creating a decorator
async def echo(message: types.Message):
    await message.reply(message.text)

    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
    
