import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot('5927070206:AAHOchiyptmgIDKs_iBJ4CNVg3E9KSviJyw')
API = 'feb1d485d1fd4aaa2722bac315773ca7'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tot = types.KeyboardButton('Чё по погодке, капитан')
    hp = types.KeyboardButton('диджей, музычку')
    mn = types.KeyboardButton('photo')
    btn1 = types.KeyboardButton("Я лёша")
    btn2 = types.KeyboardButton("поинтерисоваться хочу")
    markup.add(btn1, btn2, mn, hp, tot)
    bot.send_message(message.chat.id, text="Salam, {0.first_name}!".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Я лёша"):
        bot.send_message(message.chat.id, text="нормально общайся да?!")
    elif(message.text == "поинтерисоваться хочу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хто я?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("домой хочу")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Хто я?"):
        bot.send_message(message.chat.id, "чурка ты")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="чё по кайфу вообще")
    
    elif (message.text == "домой хочу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Я лёша")
        button2 = types.KeyboardButton("поинтерисоваться хочу")
        mn = types.KeyboardButton('photo')
        hp = types.KeyboardButton('диджей, музычку')
        markup.add(button1, button2, mn, hp)
        bot.send_message(message.chat.id, text="иди отсюда", reply_markup=markup)
    
    elif message.text == 'photo':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bn1 = types.KeyboardButton("ёжик")
        bn2 = types.KeyboardButton('споки')
        bn3 = types.KeyboardButton('а ну ка давай назад')
        markup.add(bn1, bn2, bn3)
        bot.send_message(message.chat.id, 'выбирай', reply_markup=markup)

    elif(message.text == 'ёжик'):
        photo = open('jo.png', 'rb')
        bot.send_photo(message.chat.id, photo)

    elif(message.text == 'споки'):
        ph = open('spok2.png', 'rb')
        bot.send_photo(message.chat.id, ph )

    elif(message.text == 'Чё по погодке, капитан'):
            city = 'Ростов-на-Дону'
            res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
            data = json.loads(res.text)
            temp = data["main"]["temp"]
            bot.reply_to(message, f'сейчас погода: {temp}°')

            image = 'sunny.png' if temp > 25.0 else 'sun.png'
            file = open('./' + image, 'rb')
            bot.send_photo(message.chat.id, file)
            
    elif(message.text == 'а ну ка давай назад'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Я лёша")
        btn2 = types.KeyboardButton("поинтерисоваться хочу")
        mn = types.KeyboardButton('photo')
        hp = types.KeyboardButton('диджей, музычку')
        markup.add(btn1, btn2, mn, hp)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif(message.text == 'диджей, музычку'):
        kk = open(r'music.mp3', 'rb')
        bot.send_audio(message.chat.id, kk)
    else:
        bot.send_message(message.chat.id, text="ты чё удумал то")

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'чё за красота')


bot.polling(none_stop=True)
