from pyrogram import Client, types, filters, enums

NUM = 4


@Client.on_message(filters.group & filters.command('all'))
async def mention(app: Client, msg: types.Message):
    user = await msg.chat.get_member(msg.from_user.id)
    if user.status in (enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR):
        members = app.get_chat_members(msg.chat.id)
        total = []
        async for member in members:
            member: types.ChatMember
            if member.user.username:
                total.append(f'@{member.user.username}')
            else:
                total.append(member.user.mention())

        for i in range(0, len(total), NUM):
            message = ' '.join(total[i:i+NUM])
            await app.send_message(msg.chat.id, message)
    else:
        await app.send_message(msg.chat.id, 'Admins only can do that !', reply_to_message_id=msg.id)
