# telegram bot
import pandas, os

from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler


# read excel as database
excel_data_df = pandas.read_excel('stuffs.xlsx', sheet_name='Sheet1')
lst_stuffs = excel_data_df['Stuff'].tolist()

# Здесь токен
TOKEN = os.environ.get('TOKEN')
bot = Bot(token=TOKEN)  # Вроде лучше Updater
# Для получения и обработки сообщений класс Updater
updater = Updater(token=TOKEN)
# Укажите id своего аккаунта в Telegram
chat_id = os.environ.get('CHAT_ID')
text = 'Bot is ready to show your stuff, write /start'
# Отправка сообщения
bot.send_message(chat_id, text)


def wake_up(update, context):
    chat = update.effective_chat  # определяет чат
    name = update.message.chat.first_name  # define name
    buttons = ReplyKeyboardMarkup([  # define buttons
                ['/start'],
                ['/stuff', '/add_stuff'],
            ])
    context.bot.send_message(
        chat_id=chat.id,  # айdi чата
        text=f'Good Day, {name}!',
        reply_markup=buttons
        )


def add_stuff(update, context):
    """
    Adds stuff for today
    """
    stuff = update.message.text
    print(stuff)
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='###NOT_READY###',
        )


def show_stuff(update, context):
    """
    Shows stuff for today
    """
    chat = update.effective_chat
    for num, stuff in enumerate(lst_stuffs):
        context.bot.send_message(
            chat_id=chat.id,
            text=f'{num}: {stuff}',
            )


def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    # В ответ на любое текстовое сообщение
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(chat_id=chat.id, text='Добрый день')


# Регистрируется обработчик CommandHandler;
# он будет отфильтровывать только сообщения с содержимым '/start'
# и передавать их в функцию wake_up()
updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('stuff', show_stuff))
updater.dispatcher.add_handler(CommandHandler('add_stuff', add_stuff))
# Регистрируется обработчик MessageHandler;
# из всех полученных сообщений он будет выбирать только текстовые сообщения
# и передавать их в функцию say_hi()
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

# Метод start_polling() запускает процесс polling,
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling(poll_interval=2.0)
# Бот будет работать до тех пор, пока не нажмёте Ctrl-C
updater.idle()
