from pyrogram import Client, types, filters
import requests


def reFact():
    res = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random')
    data = res.json()
    text = data['text']
    return text


@Client.on_message(filters.command('fact'))
async def fact(app: Client, msg: types.Message):
    await app.send_message(msg.chat.id, reply_to_message_id=msg.id, text=reFact())
