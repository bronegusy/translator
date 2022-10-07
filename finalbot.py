
import telebot
from telebot import types


bot = telebot.TeleBot("")

mess = ""

#alphabet = ёслаоюшбъцфентизмчьыйщхжэдявркгу__fumdjqreolwcxnhvaysibztkgp
alphabet = {"а": "ё", "б": "с", "в": "л", "г": "а", "д": "о", "е": "ю", "ё": "ш", "ж": "б", "з": "ъ", "и": "ц", "й": "ф", "к": "е", "л": "н", "м": "т", "н": "и", "о": "з", "п": "м", "р": "ч", "с": "ь", "т": "ы", "у": " ", "ф": "щ", "х": "х", "ц": "ж", "ч": "э", "ш": "д", "щ": "я", "ъ": "в", "ы": "в", "ь": "р", "э": "к", "ю": "г", "я": "у",
            "a": "f", "b": "u", "c": "m", "d": "d", "e": "j", "f": "q", "g": "r", "h": "e", "i": "o", "j": "l", "k": "w", "l": "c", "m": "x", "n": "n", "o": "h", "p": "v", "q": "a", "r": "y", "s": "s", "t": "i", "u": "b", "v": "z", "w": "t", "x": "k", "y": "g", "z": "p", " ": "й", ";": ";", ":": ":"}

@bot.message_handler(commands=['start'])
def buttons(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Зашифровать', callback_data='question_1')
    item2 = types.InlineKeyboardButton('Разшифровать', callback_data='question_2')
    markup.add(item, item2)
 
    bot.send_message(message.chat.id, 'Во хотите зашифровать или разшифровать?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "question_1":
            #@bot.send_message(cmessage.chat.id, )

            def shifr1ask(message):
                sent = bot.send_message(message.chat.id, "Какое слово вы хотите зашифровать?")
                bot.register_next_step_handler(sent, review)
            def review(message):
                message_to_save = message.text
                mess = message_to_save
                return mess
            word = ""
            for i in mess:
                for h in alphabet:
                    if i == h:
                        word = word + alphabet[h]
            @bot.send_message(call.message.chat.id, mess)

bot.polling() 
