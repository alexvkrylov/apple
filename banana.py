import telebot
from logic_2 import smiles
from bot_logic import gen_pass  
from datetime import datetime 
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8304835372:AAH9c1J6nZ3S35UnJwfwlxaYVvWeqYeKCYI")

text_messages = {
    
    'info':
        u'My name is TeleBot,\n'
        u'I am a bot that assists these wonderful bot-creating people of this bot library group chat.\n'
        u'Also, I am still under development.'
        u'Suggestions are also welcome, just drop them in this group chat!',
    'help':
        u' /info  - information about telegram bot !\n'
        u'/start,/hello. - greed wellcom with user !\n'
        u'/bye  - say bye to user !\n'
        u'/password  - can print a password with special width !\n'
        u'/heh  - repet the word he 5 times !\n'
        u'/heh 7 - repet the word he amount of times tha your number is saing !\n'
        u'/ping  - saing that he is alive that moment !\n'
        u'/clock - saing what time is it !\n'
        u'/emojialot - making a huge rondom pack of emoji !\n'
        u'/hidrolisk - giving as a picture with hidrolisk !\n'
        u'/zergling - giving as a picture with zergling !\n'
        u'/mutalisk - giving as a picture with mutalisk !\n'
        u'/ultralisk - giving as a picture with ultralisk !\n'
        u'/roach - giving as a picture with roach !\n'
        u'/zarazitel - giving as a picture with zarazitel !\n'
        u'/worker - giving as a picture with worker !\n'
        u'/nadzeratel - giving as a picture with nadzeratel !\n'
        u'/surf_host - giving as a picture with surf_host !\n'
        u'/emoji. - making a rondom pack of emoji !\n',
}

@bot.message_handler(commands=['info'])
def on_info(message):
    bot.reply_to(message, text_messages['info'])

@bot.message_handler(commands=['help'])
def on_info(message):
    bot.reply_to(message, text_messages['help'])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def genpas(message):
    fun_log = gen_pass(8)
    bot.reply_to(message, f"generated password: {fun_log}")

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['emoji'])
def genemoji(message):
    fun_log2 = smiles(4)
    bot.reply_to(message, f"generated emoji: {fun_log2}")

@bot.message_handler(commands=['emojialot'])
def genemoji(message):
    fun_log3 = smiles(200)
    bot.reply_to(message, f"generated emoji: {fun_log3}")


@bot.message_handler(commands=["clock"])
def current_time(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.send_message(message.chat.id,f"Текущее время: {current_time}")


@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Still alive and kicking!")

@bot.message_handler(commands=["hidrolisk"])
def pickdraw(message):
    with open('images/hydralisk.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["zergling"])
def pickdraw_1(message):
    with open('images/zergling.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["mutalisk"])
def pickdraw_2(message):
    with open('images/mutalisk.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["ultralisk"])
def pickdraw_3(message):
    with open('images/ultralisk.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["roach"])
def pickdraw_4(message):
    with open('images/roach.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["zarazitel"])
def pickdraw_5(message):
    with open('images/zarazitel.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["worker"])
def pickdraw_6(message):
    with open('images/worker.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["nadzeratel"])
def pickdraw_7(message):
    with open('images/nadzeratel.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["surf_host"])
def pickdraw_8(message):
    with open('images/surf_host.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
 

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
