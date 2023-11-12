from pyrogram import filters, types
from pyromod import Client

api_id = 0
api_hash = '0'
token = '0'
admin = 0

bot = Client('Bot', api_id=api_id, api_hash=api_hash, bot_token=token, plugins=dict(root='plugins', include=[
    'search', 'T2S.T2S', 'elements.elements', 'qr.qr', 'mention', 'events'
]))


@bot.on_message(filters.private & filters.user(admin) & filters.command('stat'))
async def stat(app: Client, msg: types.Message):
    await app.send_message(msg.chat.id, 'Working')

bot.run()
