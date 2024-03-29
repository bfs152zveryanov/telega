from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings 

updater = Updater(settings.API_KEY, use_context=True)

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
					level = logging.INFO,
					filename = 'bot.log'
					)

def greet_user(bot, update):
	text = 'Написал /start'
	print(text)
	update.message.reply_text("Ты кто, ебать?")

def talk_to_me(bot, update):
	if update.message.chat.username == 'nastyakirgizova':
		user_text = "Привет, Настя! Рад тебя видеть!"
		logging.info("Пользователь: %s, Чат: %s, Сообщение: %s", update.message.chat.username, 
			update.message.chat.id, update.message.text)
		update.message.reply_text(user_text)
	elif update.message.chat.username == 'Shcok7':
		user_text = "Привет, Стасян! Не заебался ещё свой код писать?"
		logging.info("Пользователь: %s, Чат: %s, Сообщение: %s", update.message.chat.username, 
			update.message.chat.id, update.message.text)
		update.message.reply_text(user_text)
	elif update.message.chat.username == 'silentredfox':
		user_text = "Привет, любимая! Как ты?"
		logging.info("Пользователь: %s, Чат: %s, Сообщение: %s", update.message.chat.username, 
			update.message.chat.id, update.message.text)
		update.message.reply_text(user_text)
	else:
		user_text = "Привет, {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
		logging.info("Пользователь: %s, Чат: %s, Сообщение: %s", update.message.chat.username, 
			update.message.chat.id, update.message.text)
		update.message.reply_text(user_text)

def main():
	mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)

	logging.info("Бот запустился")

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	mybot.start_polling()
	mybot.idle() 

main()