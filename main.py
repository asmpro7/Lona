from pyrogram import Client, filters, types

api_id = 0
api_hash = '0'
token = '0'
admin = 0

bot = Client('Bot', api_id=api_id, api_hash=api_hash, bot_token=token, plugins=dict(root='plugins', include=[
    'search', 'T2S.T2S', 'elements.elements'
]))


@bot.on_message(filters.private & filters.user(admin) & filters.command('stat'))
async def stat(app: Client, msg: types.Message):
    await app.send_message(msg.chat.id, 'Working')

bot.run()
