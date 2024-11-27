import telebot
bot = telebot.TeleBot('7639952964:AAGLNG_p8d68rjOpH2VckhsQqzw4wNMicm4')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, если не знаешь чем заняться напиши /idea')
 
@bot.message_handler(commands=['idea'])
def main(message):
    bot.send_message(message.chat.id, 'Если тебе скучно, то ты можешь порисовать, погулять или приготовить что-нибудь, идеи для рисования /painting, для прогулки /walk, для готовки /cooking')
 
@bot.message_handler(commands=['painting'])
def main(message):
    bot.send_message(message.chat.id, 'нарисуй гибрид бабочки и дракона')
 
@bot.message_handler(commands=['walk'])
def main(message):
    bot.send_message(message.chat.id, 'договорись с друзьями пойти вместе в кафе, в парк, в место где вы еще не гуляли')
 
@bot.message_handler(commands=['cooking'])
def main(message):
    bot.send_message(message.chat.id, 'приготовь мини торт, это быстро и вкусно')
 
bot.infinity_polling()
