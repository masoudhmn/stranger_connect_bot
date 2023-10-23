import telebot
from decouple import config
from loguru import logger

print('hi')
class Bot:
    def __init__(self):
        TOKEN = config('TELEGRAMBOT_TOKEN')
        self.bot = telebot.TeleBot(TOKEN, 
                                   parse_mode=None) 
        
        self.send_welcome = self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)

    def send_welcome(self, message):
        self.bot.reply_to(message, 'Hey, Whats up dud?')
    
    def run(self):
        logger.info('Running bot ...')
        self.bot.polling()

if __name__ == '__main__':
    print('main')
    bot = Bot()
    bot.run()

