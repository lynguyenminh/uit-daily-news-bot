import asyncio
import telegram


f = open('account.txt', 'r')
lines = [i[:-1] for i in f.readlines() if i[-1] == '\n']
my_token = lines[0]
my_id = int(lines[1])


async def send_message(text_message):    
    '''send message'''
    async with bot:
        await bot.send_message(text=text_message, chat_id=my_id)


bot = telegram.Bot(my_token)
if __name__ == '__main__':
    asyncio.run(send_message('Hello, I\'m bot!!!'))
