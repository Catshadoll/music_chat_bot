import telebot
from telebot import types
from functools import partial

class MusicBot:
    def __init__(self, yandex_token, vk_token):
        self.yandex_token = yandex_token
        self.vk_token = vk_token
        self.user_preferences = {}
        self.user_message = None

    def start(self, message):
        self.user_message = message
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Настроение')
        markup.add(itembtn1)
        bot.send_message(message.chat.id, "Пожалуйста выберите:", reply_markup=markup)
        bot.register_next_step_handler(message, self.handle_mood)

    def handle_mood(self, message):
        self.user_preferences['mood'] = message.text
        moods = ['Счастливый', 'Грустный', 'Расслабленный', 'Возбужденный']
        markup = types.ReplyKeyboardMarkup(row_width=2)
        buttons = [types.KeyboardButton(mood) for mood in moods]
        markup.add(*buttons)
        bot.send_message(message.chat.id, "Выберите свое настроение:", reply_markup=markup)
        bot.register_next_step_handler(message, self.handle_genre)

    def handle_genre(self, message):
        self.user_preferences['mood'] = message.text
        genres = ['Поп', 'Рок', 'Джаз', 'Классика', 'Электроника', 'Металлика', 'Фанк']
        markup = types.ReplyKeyboardMarkup(row_width=2)
        buttons = [types.KeyboardButton(genre) for genre in genres]
        markup.add(*buttons)
        bot.send_message(message.chat.id, "Выберите жанр:", reply_markup=markup)
        bot.register_next_step_handler(message, self.handle_source)

    def handle_source(self, message):
        self.user_preferences['genre'] = message.text
        sources = ['Яндекс.Музыка', 'ВКонтакте']
        markup = types.ReplyKeyboardMarkup(row_width=2)
        buttons = [types.KeyboardButton(source) for source in sources]
        markup.add(*buttons)
        bot.send_message(message.chat.id, "Выберите источник плейлиста:", reply_markup=markup)
        bot.register_next_step_handler(message, self.show_playlist)

    def show_playlist(self, message):
        self.user_preferences['source'] = message.text
        # Здесь вы можете добавить код для получения плейлиста на основе предпочтений пользователя
        bot.send_message(message.chat.id, f"Ваш плейлист на основе ваших предпочтений: {self.user_preferences}")

    def main(self):
        global bot
        bot = telebot.TeleBot('6557764348:AAHNMgJGPp7WyRUcQg5yKxEskQnAeW2GOSY')

if __name__ == '__main__':
    bot = MusicBot('y0_AgAAAAA_RnBCAAq7lwAAAADwW1cUUKVxyP9JQA6QCTZr8mcehD7zv-I', 'your_vk_token')
    bot.main()
