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
        u' /help  - shoing which commands you can use !\n'
        u' /images  - a list of images you can chouse !\n'
        u' /info  - information about telegram bot !\n'
        u'/start,/hello. - greed wellcom with user !\n'
        u'/bye  - say bye to user !\n'
        u'/password  - can print a password with special width !\n'
        u'/fights - shwing fights of starcraft !\n'
        u'/heh  - repet the word he 5 times !\n'
        u'/heh 7 - repet the word he amount of times tha your number is saing !\n'
        u'/ping  - saing that he is alive that moment !\n'
        u'/clock - saing what time is it !\n'
        u'/emojialot - making a huge rondom pack of emoji !\n'
        u'/emoji. - making a rondom pack of emoji !\n',
    'images':
        u'/zerg - giving a list of pictures with zerg !\n'
        u'/protos - giving a list of pictures with protoses !\n'
        u'/cute - giving a list of pictures with cute !\n',
    'zerg':
        u'/hidrolisk - giving as a picture with hidrolisk !\n'
        u'/zergling - giving as a picture with zergling !\n'
        u'/mutalisk - giving as a picture with mutalisk !\n'
        u'/ultralisk - giving as a picture with ultralisk !\n'
        u'/roach - giving as a picture with roach !\n'
        u'/zarazitel - giving as a picture with zarazitel !\n'
        u'/worker - giving as a picture with worker !\n'
        u'/nadzeratel - giving as a picture with nadzeratel !\n'
        u'/surf_host - giving as a picture with surf_host !\n'
        u'/revanger - giving as a picture with revanger !\n',
    'protos':
        u'/zilot - giving as a picture with zilot !\n'
        u'/stalker - giving as a picture with stalker !\n'
        u'/imortal - giving as a picture with imortal !\n'
        u'/probe - giving as a picture with probe !\n'
        u'/colose - giving as a picture with colose !\n'
        u'/disrapter - giving as a picture with disrapter !\n'
        u'/pheniks - giving as a picture with pheniks !\n'
        u'/cerier - giving as a picture with cerier !\n'
        u'/carapter - giving as a picture with carapter !\n'
        u'/masership - giving as a picture with masership !\n',
    'cute':
        u'/cat - giving as a picture with cat !\n'
        u'/mashroom - giving as a picture with mashroom !\n'
        u'/bird - giving as a picture with bird !\n'
        u'/holicopter - giving as a picture with holicopter !\n'
        u'/pig - giving as a picture with pig !\n'
        u'/apple - giving as a picture with apple !\n'
        u'/horse - giving as a picture with horse !\n'
        u'/horse - giving as a picture with horse !\n'
        u'/kong_vs_gadzila - giving as a picture with kong_vs_gadzilA !\n',
    'fights':
        u'/fight_1 - giving as a picture with fight_1 !\n'
        u'/fight_2 - giving as a picture with fight_2 !\n'
        u'/fight_3 - giving as a picture with fight_3 !\n'
        u'/fight_4 - giving as a picture with fight_4 !\n'
        u'/fight_5 - giving as a picture with fight_5 !\n'
        u'/fight_6 - giving as a picture with fight_6 !\n'
        u'/fight_7 - giving as a picture with fight_7 !\n'
        u'/fight_8 - giving as a picture with fight_8 !\n'
        u'/fight_9 - giving as a picture with fight_9 !\n'
        u'/fight_10 - giving as a picture with fight_10 !\n'
        u'/fight_11 - giving as a picture with fight_11 !\n'
        u'/fight_12 - giving as a picture with fight_12 !\n'
        u'/fight_13 - giving as a picture with fight_13 !\n'
        u'/fight_14 - giving as a picture with fight_14 !\n'
        u'/fight_15 - giving as a picture with fight_15 !\n',
}

@bot.message_handler(commands=['info'])
def on_info(message):
    bot.reply_to(message, text_messages['info'])

@bot.message_handler(commands=['protos'])
def on_images(message):
    bot.reply_to(message, text_messages['protos'])

@bot.message_handler(commands=['zerg'])
def on_images(message):
    bot.reply_to(message, text_messages['zerg'])

@bot.message_handler(commands=['cute'])
def on_images(message):
    bot.reply_to(message, text_messages['cute'])

@bot.message_handler(commands=['images'])
def on_images(message):
    bot.reply_to(message, text_messages['images'])

@bot.message_handler(commands=['fights'])
def on_fights(message):
    bot.reply_to(message, text_messages['fights'])

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

@bot.message_handler(commands=["revanger"])
def pickdraw_9(message):
    with open('images/revanger.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["zilot"])
def pickdraw_10(message):
    with open('images/zilot.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
 
@bot.message_handler(commands=["stalker"])
def pickdraw_11(message):
    with open('images/stalker.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
 
@bot.message_handler(commands=["imortal"])
def pickdraw_12(message):
    with open('images/imortal.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
 
@bot.message_handler(commands=["probe"])
def pickdraw_13(message):
    with open('images/probe.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
 
@bot.message_handler(commands=["colose"])
def pickdraw_14(message):
    with open('images/colose.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["disrapter"])
def pickdraw_15(message):
    with open('images/disrapter.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
 
@bot.message_handler(commands=["pheniks"])
def pickdraw_16(message):
    with open('images/pheniks.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
 
@bot.message_handler(commands=["cerier"])
def pickdraw_17(message):
    with open('images/cerier.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["carapter"])
def pickdraw_18(message):
    with open('images/carapter.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["masership"])
def pickdraw_19(message):
    with open('images/masership.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
 
@bot.message_handler(commands=["fight_1"])
def pickdraw_20(message):
    with open('images/fight_1.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_2"])
def pickdraw_21(message):
    with open('images/fight_2.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_3"])
def pickdraw_22(message):
    with open('images/fight_3.png', 'rb') as f:
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=["fight_4"])
def pickdraw_23(message):
    with open('images/fight_4.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_5"])
def pickdraw_24(message):
    with open('images/fight_5.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_6"])
def pickdraw_25(message):
    with open('images/fight_6.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_7"])
def pickdraw_26(message):
    with open('images/fight_7.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_8"])
def pickdraw_27(message):
    with open('images/fight_8.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_9"])
def pickdraw_28(message):
    with open('images/fight_9.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_10"])
def pickdraw_29(message):
    with open('images/fight_10.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_11"])
def pickdraw_30(message):
    with open('images/fight_11.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_12"])
def pickdraw_31(message):
    with open('images/fight_12.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_13"])
def pickdraw_32(message):
    with open('images/fight_13.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_14"])
def pickdraw_33(message):
    with open('images/fight_14.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["fight_15"])
def pickdraw_34(message):
    with open('images/fight_15.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["cat"])
def pickdraw_35(message):
    with open('images/cat.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["mashroom"])
def pickdraw_36(message):
    with open('images/mashroom.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["bird"])
def pickdraw_37(message):
    with open('images/bird.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["holicopter"])
def pickdraw_38(message):
    with open('images/holicopter.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["pig"])
def pickdraw_39(message):
    with open('images/pig.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["apple"])
def pickdraw_40(message):
    with open('images/apple.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["horse"])
def pickdraw_41(message):
    with open('images/horse.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["rabbit"])
def pickdraw_42(message):
    with open('images/rabbit.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["kong_vs_gadzila"])
def pickdraw_43(message):
    with open('images/kong_vs_gadzila.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
