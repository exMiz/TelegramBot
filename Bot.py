from telegram.ext import Updater, CommandHandler
from group import group
import re as regexp
# import logging
import test
import json


def load_db():
    with open('chat_group.json') as json_file:
        chat_group = json.load(json_file)
    return chat_group


def save_db(chat_group):
    with open('chat_group.json', 'w') as json_file:
        json.dump(chat_group, json_file)


def set_group(bot, update):
    global chat_group
    group_id = None
    chat_id = update.message.chat_id
    group_name = regexp.sub("/set_group|\s+", "", update.message.text)

    if group_name:
        try:
            group_id = group[group_name]
            bot.send_message(chat_id, "Я нашел твою группу")
            chat_group[str(chat_id)] = str(group_id)
            save_db(chat_group)
        except Exception as e:
            bot.send_message(chat_id, "Нету такой группы!")
    else:
        bot.send_message(chat_id, "Пример: /set_group ІН.м.п-72")


def schedule(bot, update):
    chat_id = update.message.chat_id

    try:
        chat_group[str(chat_id)]
        schedule_parse = test.shedule(chat_group[str(chat_id)])
        bot.send_message(chat_id, schedule_parse)
    except Exception:
        bot.send_message(chat_id, "Группа не указана. Изпользуй /set_group ")


token = "581622489:AAEIqhNS-CZUhT8hR297ptRJkrjzA8jSOaA"
updater = Updater(token)
dispatcher = updater.dispatcher

try:
    chat_group = load_db()
except Exception as e:
    chat_group = {"0": "0"}

# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO)

schedule_handler = CommandHandler("schedule", schedule)
dispatcher.add_handler(schedule_handler)
set_group_handler = CommandHandler("set_group", set_group)
dispatcher.add_handler(set_group_handler)

if __name__ == "__main__":
    try:
        updater.start_polling()
    except KeyboardInterrupt:
        exit()
