from telegram import Update
from telegram.ext import *
from datetime import datetime
from typing import Final

TOKEN: Final = '????? INSERT YOUR API KEY ?????'
BOT_USERNAME: Final = '@?????????'

print('Bot started...')

#COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome! For videos go to ?????????')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('To get help ask @????????? !')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')

#RESPONSES
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey! How are you doing?'

    if 'who are you' in processed:
        return 'I am a ????????? bot!'

    #TESTING TIME
    if 'time' in processed:
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H:%M:%S')
        return str(date_time)

    return 'I dont have the answer to that but you can use /help'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = (update.message.text).lower()

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    #LOOK IF ITS A PRIVATE OR GROUP CHAT - FOR GROUP YOU NEED TO GIVE ADMIN ACCESS
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot: ', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} casued error {context.error}')

if __name__ == '__main__':
    print('Starting program')
    app = Application.builder().token(TOKEN).build()

    #COMMANDS
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #ERRORS
    app.add_error_handler(error)

    #POLLS
    print('Polling...')
    app.run_polling(poll_interval=3)
