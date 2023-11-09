from pyromod import Client
from pyrogram import types, filters
import qrcode
import random
import os

current_file_path = os.path.abspath(__file__)
parent_folder = os.path.dirname(current_file_path)


@Client.on_message(filters.command('qr'))
async def qr(app: Client, message: types.Message):
    await app.send_message(
        message.chat.id, 'Please send the text you want to make it QR')
    query: types.Message = await app.listen(chat_id=message.chat.id, user_id=message.from_user.id)
    ran = random.randint(10000, 99999)
    img = qrcode.make(query.text)
    img.save(f'{parent_folder}\\qr_{ran}.png')
    await app.send_photo(message.chat.id, photo=f'{parent_folder}\\qr_{ran}.png')
    os.remove(f'{parent_folder}\\qr_{ran}.png')
