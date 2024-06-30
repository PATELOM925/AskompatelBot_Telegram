from aiogram import Bot, Dispatcher, types, executor 
from dotenv import load_dotenv
import os
import logging
import openai

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
model = "gpt-3.5-turbo"

#configuring logging
logging.basicConfig(level=logging.INFO)

#intialize our bot
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

class Reference:
    def __init__(self) -> None:
        self.response=""
 
rf = Reference() 

def clear_past():
    rf.response= ""      
    

@dp.message_handler(commands=['start'])
#creating a decorator
async def command_start_handler(message: types.Message):
    await message.reply("HI,\nI am ECHO BOT!,\nBuilt by OM,\n How can I help you?")
    
@dp.message_handler(commands=['clear'])
async def clear(mesage: types.Message):
    clear_past()
    await mesage.reply("I've cleared the past conversation and context")
    
@dp.message_handler(commands=['help'])
#creating a decorator
async def helper(message: types.Message):
    help = """sumary_line
    Hey TelegramBot this side!!,
    I am created by OM,
    
    Please Follow the below commands:
    /start - To Start a conversation.
    /clear - To Clear the conversation.
    /help - To get this help Menu.
    I hope this helps :)
    """
    await message.reply(help)


@dp.message_handler()
#creating a decorator
async def main_bot(message: types.Message):
   print(f"USER: \n\t{message.text}")
   response = openai.ChatCompletion.create(
       model = model,
       messages = [
           {"role": "assistant", "content": rf.response}, #our assistant
           {"role": "user", "content": message.text} #our user
           
       ]
   )
   rf.response = response["choices"][0]['message']['content']
   print(f">> Bot: \n\t{rf.response}")
   await bot.send_message(chat_id = message.chat.id, text = rf.response)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)