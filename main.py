import asyncio
import random
from telethon import TelegramClient, events

API_ID = 17349
API_HASH = '344583e45741c457fe1862106095a5eb'

START_TEXT = 'magic'

def one_step(emoji='☁'):
    lst = []
    it = 9
    for i in range(1, 73):
        lst.append(emoji)
        if i == it:
            it += 9
            lst.append('\n')
    return lst


def heart(emoji, emoji_heart):
    x = one_step(emoji=emoji)
    x[12] = emoji_heart
    x[13] = emoji_heart
    x[15] = emoji_heart
    x[16] = emoji_heart
    for i in range(21, 28):
        x[i] = emoji_heart
    for i in range(31, 38):
        x[i] = emoji_heart
    for i in range(42, 47):
        x[i] = emoji_heart
    for i in range(53, 56):
        x[i] = emoji_heart
    x[64] = emoji_heart
    return x


async def edit_msg(client, to_id, message, text, index, emoji='❤'):
    await asyncio.sleep(0.2)
    text[index] = emoji
    message = await client.edit_message(to_id, message, ''.join(text))
    return text, message


async def main():
    async with TelegramClient('name', API_ID, API_HASH) as client:
        @client.on(events.NewMessage(pattern=START_TEXT))
        async def handler(event):
            message = await client.send_message(event.message.to_id, message=''.join(one_step()))
            await asyncio.sleep(1)

            msg_text, message = await edit_msg(client, event.message.to_id, message, one_step(), 12)
            msg_text, message = await edit_msg(client, event.message.to_id, message, msg_text, 13)
            msg_text, message = await edit_msg(client, event.message.to_id, message, msg_text, 15)
            msg_text, message = await edit_msg(client, event.message.to_id, message, msg_text, 16)

            for i in range(21, 28):
                msg_text, message = await edit_msg(client, event.message.to_id, message, msg_text, i)

            for i in range(31, 38):
                msg_text, message = await edit_msg(client, event.message.to_id, message, msg_text, i)

            for i in range(42, 47):
                msg_text, message = await edit_msg(client, event.message.to_id, message, msg_text, i)

            for i in range(53, 56):
                msg_text, message = await edit_msg(client, event.message.to_id, message, msg_text, i)

            msg_text, message = await edit_msg(client, event.message.to_id, message, msg_text, 64)
            await asyncio.sleep(1)
            message = await client.edit_message(event.message.to_id, message, ''.join(one_step('🌸')))
            await asyncio.sleep(1)
            message = await client.edit_message(event.message.to_id, message, ''.join(one_step('✨')))
            await asyncio.sleep(1)
            message = await client.edit_message(event.message.to_id, message, ''.join(heart('🍀', '💖')))
            await asyncio.sleep(1)
            message = await client.edit_message(event.message.to_id, message, ''.join(heart('☁', '💟')))
            await asyncio.sleep(1)
            message = await client.edit_message(event.message.to_id, message, ''.join(heart('✨', '💎')))
            await asyncio.sleep(1)
            lst = list(range(0, len(msg_text) + 1))
            random.shuffle(lst)

            for i in lst:
                try:
                    if msg_text[i] == '\n':
                        continue
                    msg_text[i] = '❌'
                    message = await client.edit_message(event.message.to_id, message, ''.join(msg_text))
                except:
                    continue
            try:
                await client.edit_message(event.message.to_id, message, '❤')
            except:
                pass

        await client.run_until_disconnected()


asyncio.run(main())
