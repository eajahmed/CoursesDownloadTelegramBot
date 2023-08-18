from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
bot_token = "YOUR_BOT_TOKEN"


    # Create an inline keyboard with multiple buttons
keyboard = [
        [InlineKeyboardButton("Ethical Hackinga Course", callback_data="one_button")],
        [InlineKeyboardButton("Digital Marketing", callback_data="two_button")],
        [InlineKeyboardButton("Graphic Design", callback_data="three_button")],
        [InlineKeyboardButton("Premium Course", callback_data="four_button")],
        [InlineKeyboardButton("Web Development", callback_data="five_button")]
    ]
reply_markup = InlineKeyboardMarkup(keyboard)


# Command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    # Get the user's first name
    first_name = update.effective_user.first_name

    # Send the description message with the user's first name and the inline keyboard
    update.message.reply_text(f"Hello {first_name}! Welcome to Courses Downlode Telegram bot. From here you can collect link to Downlode various premium courses for Free. Select the Category of course you want to downlode from below.", reply_markup=reply_markup)

# Callback query handler for button clicks
def button_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # Check which button was clicked
    if query.data == "one_button":
        # Send information for the first button
        query.message.reply_text("Thats Grate 👍 you selected Ethical Hackinga Course. New you collect the Downlode link of your preferred course from the list below.")
        query.message.reply_text(
            "1. Your Corses Name. \n Downlode: https://google.com \n \n" #Replace 'https://google.com' with your Downlode link. 

            "2. Your Corses Name. \n Downlode: https://google.com \n \n" #Replace 'https://google.com' with your Downlode link.
            
            # Using This Mathod You can Create Multiple Link
        )
        # You can also add a link button below this message
        # keyboard = [
        #     [InlineKeyboardButton("Facebook", url="https://facebook.com/dev.eajuddin")]
        # ]
        # reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text("Downlode more courses form another category", reply_markup=reply_markup)

    elif query.data == "two_button":
        # Send information for the second button
        query.message.reply_text("Thats Grate 👍 you selected Digital Marketing Course. New you collect the Downlode link of your preferred course from the list below.")
        query.message.reply_text(
            "1. Your Corses Name. \n Downlode: https://google.com \n \n" #Replace 'https://google.com' with your Downlode link.
            )

        query.message.reply_text("Downlode more courses form another category", reply_markup=reply_markup)

    elif query.data == "three_button":
        # Send information for the second button
        query.message.reply_text("Thats Grate 👍 you selected Graphic Design Course. New you collect the Downlode link of your preferred course from the list below.")
        query.message.reply_text(
            "1. Your Corses Name. \n Downlode: https://google.com \n \n" #Replace 'https://google.com' with your Downlode link. 
            )

        query.message.reply_text("Downlode more courses form another category", reply_markup=reply_markup)

    elif query.data == "four_button":
        # Send information for the second button
        query.message.reply_text("Thats Grate 👍 you selected Premium Course. New you collect the Downlode link of your preferred course from the list below.")
        query.message.reply_text(
            "1. Your Corses Name. \n Downlode: https://google.com \n \n" #Replace 'https://google.com' with your Downlode link. 

            "2. Your Corses Name. \n Downlode: https://google.com \n \n" #Replace 'https://google.com' with your Downlode link. 

            "3. Your Corses Name. \n Downlode: https://google.com \n \n" #Replace 'https://google.com' with your Downlode link. 
        )

        query.message.reply_text("Downlode more courses form another category", reply_markup=reply_markup)

    elif query.data == "five_button":
        # Send information for the second button
        query.message.reply_text("Thats Grate 👍 you selected Web Development Course. New you collect the Downlode link of your preferred course from the list below.")
        query.message.reply_text(
            "1. Your Corses Name. \n Downlode: https://google.com \n \n" #Replace 'https://google.com' with your Downlode link. 
        )

        query.message.reply_text("Downlode more courses form another category", reply_markup=reply_markup)


#Developer Section
def developer(update: Update, context: CallbackContext) -> None:
    mail = "eajahmed5110@gmail.com"
    update.message.reply_text(
        f"Hello World! This Bot is Developed by EAJUDDIN AHMED. \n \nEAJUDDIN is a Front-end Web Developer and WordPress Expert. Also he is a great Telegram Bot Developer \nContact Information: \n \nTelegram : @eajahmed \n \nLinkedin: https://www.linkedin.com/in/eajahmed \n \nMail : {mail} \n \nWhatsApp: +8801316032483"
        )

def main() -> None:
    # Create the Updater and pass your bot token
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Register the callback query handler for button clicks
    dp.add_handler(CallbackQueryHandler(button_callback))

    # Register the command handler for the /developer command
    dp.add_handler(CommandHandler("Developer", developer))

    # Start the bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == "__main__":
    main()
