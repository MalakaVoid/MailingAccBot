import asyncio
import os
import sys
import time
from pyrogram import Client
from pyrogram import types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from globals import admins, chat_exmps, groups_to_add
from txt_controller import get_groups, add_group
from pyrogram import filters
from StateClass import States
import os

#program
current_admin_user = None
app = Client("account", os.getenv("API_ID"), os.getenv("API_HASH"))
cur_state = States()
get_groups()


with app:
    for dialog in app.get_dialogs():
        if str(dialog.chat.username) in groups_to_add:
            groups_to_add.remove(str(dialog.chat.username))
            chat_exmps.append(dialog.chat)

with app:
    for group_name in groups_to_add:
        try:
            chat = app.join_chat(group_name)
            chat_exmps.append(chat)
        except Exception as e:
            print(str(e) + "\n")

#handler
@app.on_message(filters.user(admins) & filters.private)
async def admins_chat(client, message: types.Message):
    global current_admin_user
    global cur_state
    if message.text == "/start" and current_admin_user == None:
        current_admin_user = message.chat.username
        cur_state.option_menu_state()
        await app.send_message(message.chat.id,
                               text="Выберите опцию - 1, 2, 3, 4:\n"
                                    "1 - Начать рассылку\n"
                                    "2 - Показать группы для рассылки\n"
                                    "3 - Добавить группу для рассылки\n"
                                    "4 - Выйти\n")
    elif message.text == "/start" and current_admin_user != message.chat.username:
        await app.send_message(chat_id=message.chat.id,
                               text="Другой пользователь использует рассылку, попробуйте позже.")
    elif current_admin_user == str(message.chat.username):
        if cur_state.get_state() == "option_menu_state":
            txt_input = message.text
            if txt_input == "1":
                cur_state.get_message_to_mail_state()
                await app.send_message(chat_id=message.chat.id,
                                       text="Введите сообщение для рассылки:")
            elif txt_input == "2":
                msg_txt = "Группы:\n"
                for e_chat in chat_exmps:
                    msg_txt += f"ссылка: {e_chat.username} название: {e_chat.title}\n"
                await app.send_message(chat_id=message.chat.id,
                                       text=msg_txt)
                await app.send_message(message.chat.id,
                                       text="Выберите опцию - 1, 2, 3, 4:\n"
                                            "1 - Начать рассылку\n"
                                            "2 - Показать группы для рассылки\n"
                                            "3 - Добавить группу для рассылки\n"
                                            "4 - Выйти\n")
            elif txt_input == "3":
                cur_state.get_group_to_add_state()
                await app.send_message(chat_id=message.chat.id,
                                       text="Введите ссылку на группу:")
            elif txt_input == "4":
                current_admin_user = None
                cur_state.end_states()
        elif cur_state.get_state() == "get_message_to_mail_state":
            await app.send_message(chat_id=message.chat.id,
                                   text="Идет отправка сообщений, пожалуйста подождите!")
            await send_message(message.text, message.chat)
            await app.send_message(chat_id=message.chat.id,
                                   text="Сообщения успешно отправлены!")
            await app.send_message(message.chat.id,
                                   text="Выберите опцию - 1, 2, 3, 4:\n"
                                        "1 - Начать рассылку\n"
                                        "2 - Показать группы для рассылки\n"
                                        "3 - Добавить группу для рассылки\n"
                                        "4 - Выйти\n")
            cur_state.option_menu_state()
        elif cur_state.get_state() == "get_group_to_add_state":
            await join_chat_group(message.text, message.chat)
            await app.send_message(message.chat.id,
                                   text="Выберите опцию - 1, 2, 3, 4:\n"
                                        "1 - Начать рассылку\n"
                                        "2 - Показать группы для рассылки\n"
                                        "3 - Добавить группу для рассылки\n"
                                        "4 - Выйти\n")
            cur_state.option_menu_state()


async def join_chat_group(group_txt, admin_chat):         #Добавление в группы
    group_name = added_line = group_txt.replace("https://t.me/", "")
    try:
        chat = await app.join_chat(group_name)
        chat_exmps.append(chat)
        add_group(group_txt)
    except Exception as e:
        ex_txt = str(e)
        await app.send_message(chat_id=admin_chat.id,
                               text=ex_txt)

async def send_message(message_txt, admin_chat):  #Отправка рассылки
    for e_chat in chat_exmps:
        try:
            await app.send_message(e_chat.id,
                                   text=message_txt)
        except Exception as e:
            await app.send_message(chat_id=admin_chat.id,
                                   text=f"Произошла проблема с группой {e_chat.username}. Ошибка: {e}\n")
        time.sleep(5)

if __name__ == '__main__':
    app.run()



