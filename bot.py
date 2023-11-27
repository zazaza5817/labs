import telebot
import random
import sqlite3

tg_token = "5842325787:AAFv00DwjC9CrrRgfqQQwjhvb5mkZU_9KJU"
bot = telebot.TeleBot(tg_token)
signup_message_id = 0


@bot.message_handler(commands=['signup'])
def signup_message(message):
    try:
        if message.from_user.id == 818068290:
            global signup_message_id
            con = sqlite3.connect("users.db")
            cur = con.cursor()
            cur.execute("DELETE FROM signed_users")
            con.commit()
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text="ЗАПИСАТЬСЯ", callback_data="turn"), )
            message = bot.send_message(message.chat.id, "Записываться сюда", reply_markup=markup)
            signup_message_id = message.id
    except Exception as e:
        print(e)


@bot.message_handler(commands=['shuffle'])
def signup_message(message):
    try:
        if message.from_user.id == 818068290:
            global signup_message_id
            bot.edit_message_reply_markup(message.chat.id, signup_message_id, reply_markup=None)
            con = sqlite3.connect("users.db")
            cur = con.cursor()
            cur.execute("DELETE FROM queue")
            con.commit()
            res = cur.execute("SELECT nickname FROM signed_users")
            res = res.fetchall()
            random.shuffle(res)
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text="сдал", callback_data="passed"), )
            markup.add(telebot.types.InlineKeyboardButton(text="записаться в конец очереди", callback_data="to_end"), )
            text = ""
            if res:
                cur.execute("DELETE FROM signed_users")
                con.commit()
                for i in range(len(res)):
                    cur.execute(f"""INSERT INTO queue VALUES ('{res[i][0]}')""")
                    con.commit()
                    text += f"{i + 1}. @{res[i][0]}\n"
            else:
                text = "Нет записанных пользователей"
            bot.send_message(message.chat.id, text, reply_markup=markup)
    except Exception as e:
        print(e)


def update_message(res, call):
    text = ""
    if res:
        for i in range(len(res)):
            text += f"{i + 1}. @{res[i][0]}\n"
    else:
        text = "Нет записанных пользователей"
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text="сдал", callback_data="passed"), )
    markup.add(telebot.types.InlineKeyboardButton(text="записаться в конец очереди", callback_data="to_end"), )
    bot.edit_message_text(text, call.message.chat.id, call.message.id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    try:
        if call.from_user.username:
            con = sqlite3.connect("users.db")
            cur = con.cursor()
            if call.data == "turn":
                res = cur.execute("SELECT nickname FROM signed_users")
                res = res.fetchall()
                if (call.from_user.username,) not in res:
                    cur.execute(f"""INSERT INTO signed_users VALUES ('{call.from_user.username}')""")
                    res.append((call.from_user.username,))
                    con.commit()
                    text = "Записавшиеся на следующий рандом\n"
                    for user in res:
                        text += f"@{user[0]}\n"
                    markup = telebot.types.InlineKeyboardMarkup()
                    markup.add(telebot.types.InlineKeyboardButton(text="ЗАПИСАТЬСЯ", callback_data="turn"), )
                    bot.edit_message_text(text, call.message.chat.id, call.message.id, reply_markup=markup)
                bot.answer_callback_query(call.id, "Ты записан")
            elif call.data == "passed":
                res = cur.execute("SELECT nickname FROM queue")
                res = res.fetchall()
                if (call.from_user.username,) in res:
                    if (call.from_user.username,) != res[0]:
                        bot.send_message(call.message.chat.id,
                                         f"@{call.from_user.username} выписан из очереди, будучи не на первом месте")
                    bot.answer_callback_query(call.id, "Выписал тебя из очереди", show_alert=True)
                    cur.execute(f"DELETE FROM queue WHERE nickname = '{call.from_user.username}'")
                    con.commit()
                    res.pop(res.index((call.from_user.username,)))
                    update_message(res, call)
                else:
                    bot.answer_callback_query(call.id, "Ты не в очереди", show_alert=True)
            elif call.data == "to_end":
                res = cur.execute("SELECT nickname FROM queue")
                res = res.fetchall()
                if (call.from_user.username,) not in res:
                    cur.execute(f"""INSERT INTO queue VALUES ('{call.from_user.username}')""")
                    con.commit()
                    bot.answer_callback_query(call.id, "Записал тебя", show_alert=False)
                    res.append((call.from_user.username,))
                    update_message(res, call)

                else:
                    bot.answer_callback_query(call.id, "Ты уже в очереди", show_alert=True)
    except Exception as e:
        print(e)


bot.polling(non_stop=True)
