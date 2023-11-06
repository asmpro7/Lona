from pyrogram import Client,types,filters
from gtts import gTTS
import os

current_file_path = os.path.abspath(__file__)
parent_folder = os.path.dirname(current_file_path)

key = '|'
Group = '@LonaHelperGroup'

@Client.on_inline_query(filters.regex(r'^!v.*\|$'))
async def textToSpeach(bot:Client,query:types.InlineQuery):
    text = query.query.split(None,1)[1]
    if len(text) > 3 and ":" in text[0]:                
                    lang=text[1:3]
                    text=text[3:]
                    if text.endswith(key):
                        myobj = gTTS(text=text, lang=lang, slow=False)
                        myobj.save(f"{parent_folder}/LonaVoice.mp3")
                        myobj = open(f"{parent_folder}/LonaVoice.mp3",'rb')
    else:
        lang="en"
        if text.endswith(key):
            myobj = gTTS(text=text, lang=lang, slow=False)
            myobj.save(f"{parent_folder}/LonaVoice.mp3")
            myobj = open(f"{parent_folder}/LonaVoice.mp3",'rb')
            
    audio = await bot.send_audio(Group,myobj,file_name='Lona Audio')
    await query.answer([types.InlineQueryResultAudio(audio.link,'Click Here To Send')])
