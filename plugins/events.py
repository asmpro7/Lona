from pyrogram import Client, types, filters, enums

is_ok = True


@Client.on_message(filters.service)
async def event(app: Client, even: types.Message):
    if is_ok:
        await even.delete()


@Client.on_message(filters.command('eventOff'))
async def handle_events_off(app: Client, msg: types.Message):
    user = await msg.chat.get_member(msg.from_user.id)
    if user.status in (enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR):
        global is_ok
        is_ok = False
    else:
        await app.send_message(msg.chat.id, 'Admins only can do that !', reply_to_message_id=msg.id)
    await app.send_message(msg.chat.id, 'Auto event remover: Off', reply_to_message_id=msg.id)


@Client.on_message(filters.command('eventOn'))
async def handle_events_on(app: Client, msg: types.Message):
    user = await msg.chat.get_member(msg.from_user.id)
    if user.status in (enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR):
        global is_ok
        is_ok = True
    else:
        await app.send_message(msg.chat.id, 'Admins only can do that !', reply_to_message_id=msg.id)

    await app.send_message(msg.chat.id, 'Auto event remover: On', reply_to_message_id=msg.id)
