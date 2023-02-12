import openai
import os
import dotenv
from aiogram import Bot, Dispatcher, executor


dotenv.load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')
bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message):
    await message.reply(
        'Привет! Теперь Вы можете использовать нейросеть ChatGPT бесплатно и без ограничений. Отправьте любое '
        'сообщение, чтобы начать! Для большей эффективности пишите запросы на английском')


@dp.message_handler()
async def chat(message):
    check_member = await bot.get_chat_member(-1001645202674, message.from_user.id)
    if check_member.status in ["member", "creator"]:
        response = await openai.Completion.acreate(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        await message.reply(response['choices'][0]['text'])
    else:
        await message.reply('Для продолжения подпишитесь на наш канал: @neural_ai_news')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)