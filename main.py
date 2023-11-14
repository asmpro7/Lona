from pyrogram import filters, types
from pyromod import Client
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from plugins.Reminder.reminder import get_time
schduler = AsyncIOScheduler()

api_id = 0
api_hash = '0'
token = '0'
admin = 0

bot = Client('Bot', api_id=api_id, api_hash=api_hash, bot_token=token, plugins=dict(root='plugins', include=[
    'search', 'T2S.T2S', 'elements.elements', 'qr.qr', 'mention', 'events', 'fact', 'Reminder.reminder'
]))


@bot.on_message(filters.private & filters.user(admin) & filters.command('stat'))
async def stat(app: Client, msg: types.Message):
    await app.send_message(msg.chat.id, 'Working')


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
bot.run()
