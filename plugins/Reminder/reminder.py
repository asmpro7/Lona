from pyromod import Client
from pyrogram import types, filters
import sqlite3
import os
from prettytable import PrettyTable

file = os.path.abspath(__file__)
parent = os.path.dirname(file)


def show(id):
    db = sqlite3.connect(f'{parent}/database.db')
    cr = db.cursor()
    cr.execute(f'''
        SELECT task,time FROM tasks WHERE userID = {id}
''')
    all_tasks = cr.fetchall()
    db.close()
    return all_tasks


def add(id, task, time):
    db = sqlite3.connect(f'{parent}/database.db')
    cr = db.cursor()
    cr.execute(f'''
        INSERT INTO tasks(userID,task,time) VALUES({id},"{task}","{time}")
''')
    db.commit()
    db.close()


def get_time(time):
    db = sqlite3.connect(f'{parent}/database.db')
    cr = db.cursor()
    cr.execute(f'''
        SELECT userID,task FROM tasks WHERE time = "{time}"''')
    data = cr.fetchall()
    db.close()
    return data


def Delete(id):
    db = sqlite3.connect(f'{parent}/database.db')
    cr = db.cursor()
    cr.execute(f'''
        Delete FROM tasks WHERE userID ={id}''')
    db.commit()
    db.close()


@Client.on_message(filters.private & filters.command('reminder'))
async def reminder(app: Client, msg: types.Message):
    await app.send_message(msg.chat.id, 'Choose what you want: ', reply_markup=types.InlineKeyboardMarkup(
        [
            [types.InlineKeyboardButton(
                text='Show all Reminders', callback_data='all_reminders')],
            [types.InlineKeyboardButton(
                text='Add New Reminder', callback_data='add_reminder')]
        ]))


@Client.on_callback_query()
async def show_all(app: Client, query: types.CallbackQuery):
    if query.data == 'all_reminders':
        results = show(query.from_user.id)
        table = PrettyTable(field_names=['task', 'time'])
        table.add_rows(results)
        await app.send_message(query.from_user.id, text=f'`{table}`', reply_markup=types.InlineKeyboardMarkup(
            [

                [
                    types.InlineKeyboardButton(
                        'Delete All', callback_data='Delete')
                ]

            ]

        ))

    elif query.data == 'add_reminder':
        task = await app.ask(query.from_user.id, text='Enter your task')
        time_date = await app.ask(query.from_user.id, text='Enter the date (dd/mm/yyyy)')
        time_time = await app.ask(query.from_user.id, text='Enter the time (hh:mm)')
        time = time_date.text + ' ' + time_time.text

        add(query.from_user.id, task.text, time)
        await app.send_message(query.from_user.id, 'Task added Sucessfully!')
    elif query.data == 'Delete':
        Delete(query.from_user.id)
        await app.send_message(query.from_user.id, 'All Reminders Deleted Sucessfully!')

# add this to the start of the main file:
'''
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from plugins.Reminder.reminder import get_time
schduler = AsyncIOScheduler()
'''

# add this before the run of bot
'''
async def sch():
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(now)
    tasks = get_time(now)
    print(tasks)
    if tasks:
        for task in tasks:
            await bot.send_message(chat_id=task[0], text=task[1])

schduler.add_job(sch, "interval", seconds=60)
schduler.start()
'''
