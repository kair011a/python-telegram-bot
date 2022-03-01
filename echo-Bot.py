import config

from telegram import Update
from telegram import Bot

from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

updater = Updater(config.token)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
	user = update.effective_user
	update.message.reply_markdown_v2(
		fr'Hi {user.mention_markdown_v2()}')

def help(update: Update, context: CallbackContext):
	update.message.reply_text("Content is empty...")

def echo(update: Update, context: CallbackContext):
	update.message.reply_text("Bekjan chmo")

def main():
	dispatcher.add_handler(CommandHandler('start', start))
	dispatcher.add_handler(CommandHandler('help', help))


	dispatcher.add_handler(MessageHandler(Filters.text, echo))	

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
