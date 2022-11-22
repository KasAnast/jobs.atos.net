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
import time
from threading import Thread
from threading import Event
import subprocess
import speech_recognition as sr

import re
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import html2text
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
# import json
# import operator
from fpdf import FPDF
import os
import sys

sys.path.insert(0, r'C:\Users\akasy\python\scraper\jobs.atos.net')

import scraper, pdf_lib

titles = ['python', 'go', 'golang', '1C','java','git','gitlab','linux','windows','sap', 'C#','']
loctab = ['UK','RU','US','']
text = ''
region = ''
# def call(text, region):
#     sk = ['NodeJS', 'Angular', 'TypeScript', 'Robot Framework',
#           'Linux', 'Unix', 'Cloud', 'Cybersecurity', 'Devops',
#           'Java', 'C', 'C++', 'C#', 'React', 'Oracle', 'Shell', 'Perl',
#           'Go', 'Golang', 'Python', 'Rust', 'Javascript',
#           'SQL', 'Git', 'Angular', 'Vue', 'Docker', 'Kubernetes']
#     dict_of_key_skills = {}
#     dict_of_key_skills['strSearch'] = text
#     dict_of_key_skills['strArea'] = region
#     dict_of_key_skills['strUrl'] = []
#     dict_of_key_skills['strJobTitle'] = []
#     dict_of_key_skills['strArrKeySkills'] = []
#     next_page = 0
#     repeat = True
#     options = Options()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     while repeat:
#         url = 'https://jobs.atos.net/search/?q=' + text + '&locationsearch=' + region + '&startrow=' + str(next_page)
#         driver.get(url)
#         content = driver.page_source
#         soup = BeautifulSoup(content, "html.parser")
#         try:
#             count_jobs_str = soup.find('span', {'class': 'paginationLabel'})
#             count_jobs_split = re.findall(r'\d+', count_jobs_str.text)
#             for a in soup.findAll('a', {'class': 'jobTitle-link'}):
#                 link = a['href']
#                 link = 'https://jobs.atos.net' + link
#                 if link not in dict_of_key_skills['strUrl']:
#                     dict_of_key_skills['strUrl'].append(link)
#                     link_text = requests.get(link).text
#                     soup_l = BeautifulSoup(link_text, 'html.parser')
#                     title = soup_l.find(attrs={
#                         'itemprop': 'title'})
#                     if title:
#                         dict_of_key_skills['strJobTitle'].append(title.text)
#                     span = soup_l.find('span', attrs={
#                         'class': 'jobdescription'})
#                     d = html2text.HTML2Text()
#                     d.ignore_links = True
#                     skills = d.handle(span.text)
#                     array = re.split(r'/|,| |\n|;|(?!.* ).', skills, flags=re.DOTALL)
#                     list = frozenset(array)
#                     for skill in list:
#                         for s in sk:
#                             if skill.upper() == s.upper():
#                                 if s.upper() not in dict_of_key_skills['strArrKeySkills']:
#                                     dict_of_key_skills['strArrKeySkills'].append(s)
#             repeat = count_jobs_split[1] < count_jobs_split[2]
#             dict_of_key_skills['amountvac'] = count_jobs_split[2]
#             if repeat:
#                 next_page = count_jobs_split[1]
#         except:
#             repeat = False
#     driver.quit()
#     return dict_of_key_skills
#
# def analisys(dict,dict_of_key_skills):
#     for key_skill in dict_of_key_skills['strArrKeySkills']:
#         if dict.setdefault(key_skill) == None:
#             dict[key_skill] = 1
#         else:
#             dict[key_skill] += 1
# def json_create(dict_json):
#     with open("skills.json", "w") as outfile:
#         json.dump(dict_json, outfile)
# def prepare_data(text, region):
#     dict_of_key_skills = call(text, region)
#     dict_json = {}
#     dict_json['strSearch'] = dict_of_key_skills['strSearch']
#     dict_json['strArea'] = dict_of_key_skills['strArea']
#     dict_json['strUrl'] = dict_of_key_skills['strUrl']
#     dict_json['strJobTitle'] = dict_of_key_skills['strJobTitle']
#     dict_json['amountvac'] = dict_of_key_skills['amountvac']
#     dicti = {}
#     analisys(dicti, dict_of_key_skills)
#     sorted_d = dict(sorted(dicti.items(), key=operator.itemgetter(1), reverse=True))
#     dict_json['skills'] = sorted_d
#     json_create(dict_json)
#     dict_json['amountvacstr'] = f"{(len(dict_json['skills']))} skills are found"
#     return dict_json

def get_chat_id(update, context):
    chat_id = -1

    if update.message is not None:
        chat_id = update.message.chat.id
    elif update.callback_query is not None:
        chat_id = update.callback_query.message.chat.id
    elif update.poll is not None:
        chat_id = context.bot_data[update.poll.id]

    return chat_id


def send_action(update, context, event):
    event.wait()
    while event.is_set():
        context.bot.send_chat_action(chat_id=get_chat_id(update, context),
                                     action='typing')
        time.sleep(5)
def send_searched_info(update, context, event):
    event.set()
    dict_json = scraper.prepare_data(text, region)
    str = ''
    for key, value in dict_json['skills'].items():
        str = f"{str}\n{key} - {value}"
    update.message.reply_text(f"{dict_json['amountvacstr']}\n"
                              f"{str}")
    with open("skills.json", "rb") as outfile:
        context.bot.send_document(chat_id=get_chat_id(update, context),
                                  document=outfile,
                                  filename='skills.json')
    pdf = pdf_lib.print(dict_json)
    with open("skills.pdf", "rb") as outfile:
        context.bot.send_document(chat_id=get_chat_id(update, context),
                                  document=outfile,
                                  filename='skills.pdf')
    event.clear()
def send_reply_search(update, context):
    event = Event()
    Thread(target=send_action, args=(update, context, event)).start()
    Thread(target=send_searched_info, args=(update, context, event)).start()

def search(update, context):
    update.message.reply_text('Processing... Please, wait!')
    send_reply_search(update, context)


def set(update, context):
    keyboardInline = [[InlineKeyboardButton("Title", callback_data='title')],
                      [InlineKeyboardButton("Location", callback_data='loc')]]

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
    global text, region, titles, loctab
    query = update.callback_query
    update.callback_query.delete_message
    match query.data:
        case 'title':
            keyboard = []
            for key_skill in titles:
                keyboard.append([InlineKeyboardButton(key_skill, callback_data=f"T{key_skill}")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.callback_query.edit_message_text('Please choose title:', reply_markup=reply_markup)
        case 'loc':
            keyboard = []
            for key_skill in loctab:
                keyboard.append([InlineKeyboardButton(key_skill, callback_data=f"L{key_skill}")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.callback_query.edit_message_text('Please choose location:', reply_markup=reply_markup)
        case _:
            match query.data[0]:
                case 'T':
                    text = query.data[1:]
                    update.callback_query.edit_message_text("Title: %s" % query.data[1:])
                case 'L':
                    region = query.data[1:]
                    update.callback_query.edit_message_text("Location: %s" % query.data[1:])

def show(update, _):
    update.message.reply_text(f"Title: {text}\nLocation: {region}")
def help(update, _):
    update.message.reply_text(
"I can help you to find frequency of occurrence in the text "
"of vacancies of searched skill at the site jobs.atos.net \n"
"You can control me by sending these commands:\n"

"/search - for start searching\n"
"/show - for check current details for search\n"
"/set - for set up details for search")

def cancel(update, _):
    update.message.reply_text('Operation cancelled. /help')

def unknown(update, _):
    update.message.reply_text('Unrecognized command. /help')

def voice(update, _):
    src_filename = update.message.voice.get_file().download()
    dest_filename = 'voice.wav'
    process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename])
    if process.returncode != 0:
        raise Exception("Something went wrong")
    voice = sr.AudioFile('voice.wav')
    r = sr.Recognizer()
    with voice as source:
        audio = r.record(source)
    update.message.reply_text(f'{r.recognize_google(audio)}')
    os.remove(src_filename)
    os.remove(dest_filename)

def text_rec(update, _):
    global text, region, titles, loctab
    array = re.split(' ', update.message.text, flags=re.DOTALL)
    list = frozenset(array)
    for word in list:
        for t in titles:
            if t.upper() == word.upper():
                text = t
        for l in loctab:
            if l.upper() == word.upper():
                region = l
    show(update, _)
def main():
    # Create the Updater and past it your bot's token.
    updater = Updater("5473579136:AAGa7eshR8bvApduIDgT8mcFL6w5M3HNbOE", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('search', search))
    updater.dispatcher.add_handler(CommandHandler('set', set))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('cancel', cancel))
    updater.dispatcher.add_handler(CommandHandler('show', show))

    updater.dispatcher.add_handler(MessageHandler(Filters.text, text_rec))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    updater.dispatcher.add_handler(MessageHandler(Filters.voice, voice))
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()