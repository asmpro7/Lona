from pyrogram import Client,types,filters
from urllib.parse import quote

GOOGLE = r'https://www.google.com/search?q='

@Client.on_inline_query(filters.regex(r'^!s '))
async def search(bot:Client,query:types.InlineQuery):
    SearchUrl = GOOGLE + quote(query.query.split(None,1)[1])
    await query.answer([
        types.InlineQueryResultArticle(
            title='Click Here',
            input_message_content=types.InputTextMessageContent(message_text=f'Your Search about {query.query.split(None,1)[1]}'),         
            reply_markup=types.InlineKeyboardMarkup(
        [
            [types.InlineKeyboardButton('Click to Open',url=SearchUrl)]
        ]

    )
        )
    ])