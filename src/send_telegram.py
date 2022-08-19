import asyncio
import telegram



my_token = 'xxx'
my_id = xxx


async def send_message(text_message):    
    '''send message'''
    async with bot:
        await bot.send_message(text=text_message, chat_id=my_id)


bot = telegram.Bot(my_token)
if __name__ == '__main__':
    asyncio.run(send_message('Hello, I\'m bot!!!'))
