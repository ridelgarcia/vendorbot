from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler


async def hello(update: Update, context: ContextTypes) -> None:
    menu_main = [[InlineKeyboardButton('Option 1', callback_data='m1'),InlineKeyboardButton('Option 4', callback_data='m4')],
                 [InlineKeyboardButton('Option 2', callback_data='m2')],
                 [InlineKeyboardButton('Option 3', callback_data='m3')]]
    reply_markup = InlineKeyboardMarkup(menu_main)
    
    await update.message.reply_html("<b>Negrita</b>lakdjfhdfjhaldfjh");
    await update.message.reply_text('Choose the option: '+str(update.effective_user.id), reply_markup=reply_markup)
    await update.message.reply_photo(photo=open('resources\static\img\hn.jpg','rb'))
    #update.message.reply_text(f'Ridel\'s bot responds {update.effective_user.username}')

async def message_handler(update:Update,context:ContextTypes) -> None:
    await update.message.reply_text('message handler:' + update.message)



def main() -> int:
    app = ApplicationBuilder().token("5375112670:AAH9YRtoR0n4FwOpxS68IdVi6luUk6I3KEg").build()

    app.add_handler(CommandHandler("ver", hello))    

    app.run_polling()

if __name__ == '__main__':
    main()