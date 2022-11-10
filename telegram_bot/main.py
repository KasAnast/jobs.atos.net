# from telegram.ext.updater import Updater
# from telegram.update import Update
# from telegram.ext.callbackcontext import CallbackContext
# from telegram.ext.commandhandler import CommandHandler
# from telegram.ext.messagehandler import MessageHandler
# from telegram.ext.pollhandler import PollHandler
# from telegram.ext.filters import Filters


# updater = Updater("5473579136:AAGa7eshR8bvApduIDgT8mcFL6w5M3HNbOE",
#                   use_context=True)


# def start(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Hi")
# def help(update: Update, context: CallbackContext):
#     update.message.reply_text("I will help, you need wait")
#
#
# def unknown_text(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Sorry I can't recognize you , you said '%s'" % update.message.text)
#
#
# def unknown(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Sorry '%s' is not a valid command" % update.message.text)
#
#
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('help', help))
# updater.dispatcher.add_handler(MessageHandler(
#     # Filters out unknown commands
#     Filters.command, unknown))
#
# # Filters out unknown messages.
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
#
# updater.start_polling()
# updater.idle()

#
# class QuizQuestion:
#     def __init__(self, question="", answers=[], correct_answer=""):
#         self.question = question
#         self.answers = answers
#         self.correct_answer = correct_answer
#         self.correct_answer_position = self.__get_correct_answer_position__()
#
#     def __get_correct_answer_position__(self):
#         ret = -1
#
#         i = 0
#         for answer in self.answers:
#             if answer.lower() == self.correct_answer.lower():
#                 ret = i
#                 break
#             i = i + 1
#
#         return ret
#
#     def __str__(self):
#         return f"question:{self.question} answers:{self.answers} correct_answer:{self.correct_answer} correct_answer_position:{self.correct_answer_position} "
#
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Poll
# from telegram.ext import (
#     Updater,
#     CommandHandler,
#     MessageHandler,
#     Filters,
#     CallbackQueryHandler,
#     PollHandler
# )
# import telegram
#
#
# def get_chat_id(update, context):
#     chat_id = -1
#
#     if update.message is not None:
#         chat_id = update.message.chat.id
#     elif update.callback_query is not None:
#         chat_id = update.callback_query.message.chat.id
#     elif update.poll is not None:
#         chat_id = context.bot_data[update.poll.id]
#
#     return chat_id
#
# def start_command_handler(update, context):
#     quiz_question = QuizQuestion()
#     quiz_question.question = "What tastes better?"
#     quiz_question.answers = ["water", "ice", "wine"]
#     quiz_question.correct_answer_position = 2
#     quiz_question.correct_answer = "wine"
#     message = context.bot.send_poll(
#         chat_id=get_chat_id(update, context),
#         question=quiz_question.question,
#         options=quiz_question.answers,
#         type=Poll.QUIZ,
#         correct_option_id=quiz_question.correct_answer_position,
#         is_anonymous=True,
#         explanation="Well, honestly that depends on what you eat",
#         explanation_parse_mode=telegram.ParseMode.MARKDOWN_V2
#     )
#     context.bot_data.update({message.poll.id: message.chat.id})
#
# def help_command_handler(update, context):
#     """Send a message when the command /help is issued."""
#     update.message.reply_text("Type /start")
#
# def main_handler(update, context):
#     update.message.reply_text(
#           "Sorry I can't recognize you , you said '%s'" % update.message.text)
#
#
#
#
# updater = Updater("5473579136:AAGa7eshR8bvApduIDgT8mcFL6w5M3HNbOE", use_context=True)
#
# dp = updater.dispatcher
#
# # command handlers
# dp.add_handler(CommandHandler("help", help_command_handler))
# dp.add_handler(CommandHandler("start", start_command_handler))
#
# # message handler
# dp.add_handler(MessageHandler(Filters.text, main_handler))
#
#
#
# # Start the Bot
# updater.start_polling()

# from telegram.ext.updater import Updater
# from telegram.ext.commandhandler import CommandHandler
# updater = Updater("5473579136:AAGa7eshR8bvApduIDgT8mcFL6w5M3HNbOE",
#                   use_context=True)
#
#
# def start(update, context):
#     update.message.reply_text(
#         f"User: {update.message.from_user.first_name} \nLanguage: {update.message.from_user.language_code}")
#
# updater.dispatcher.add_handler(CommandHandler('start', start))
#
# updater.start_polling()
# updater.idle()


from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, \
    CallbackQueryHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Start')
def set(update, context):
    keyboardInline = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],
                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markupInline = InlineKeyboardMarkup(keyboardInline)

    # keyboard = [[KeyboardButton("Option 1", callback_data='1'),
    #              KeyboardButton("Option 2", callback_data='2'),
    #              KeyboardButton("Option 3", callback_data='3')]]
    # reply_markup = ReplyKeyboardMarkup(keyboard)
    # reply_markup.resize_keyboard = True
    # reply_markup.one_time_keyboard = True
    # reply_markup.selective = True
    update.message.reply_text('Please choose:', reply_markup=reply_markupInline)


def button(update, _):
    query = update.callback_query
    if query.data == '1':
        update.callback_query.delete_message
        keyboard = [[InlineKeyboardButton("A", callback_data='A'),
                     InlineKeyboardButton("B", callback_data='B')],
                    [InlineKeyboardButton("C", callback_data='C')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.callback_query.edit_message_text('Please choose:', reply_markup=reply_markup)
        update.callback_query.delete_message
    else:
        update.callback_query.edit_message_text("Selected option: %s" % query.data)
        update.callback_query.delete_message

def help(update, _):
    update.message.reply_text(
'''I can help you to find frequency of occurrence in the text 
of vacancies of searched skill at the site jobs.atos.net
    
You can control me by sending these commands:

/search - for start searching
/set - for set up searching details or "''')

def cancel(update, _):
    update.message.reply_text('Operation cancelled. /help')

def unknown(update, _):
    update.message.reply_text('Unrecognized command. /help')

def main():
    # Create the Updater and past it your bot's token.
    updater = Updater("5473579136:AAGa7eshR8bvApduIDgT8mcFL6w5M3HNbOE", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('set', set))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('cancel', cancel))

    updater.dispatcher.add_handler(MessageHandler(Filters.text, help))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()