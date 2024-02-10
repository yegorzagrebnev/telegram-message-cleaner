from telethon.sync import TelegramClient

api_id = "" or str(input("Please enter your API ID: "))
api_hash = "" or str(input("Please enter your API hash: "))
phone_number = "" or str(input("Please enter your phone number: "))

client = TelegramClient("session_name", api_id, api_hash)

async def main():
    await client.start(phone_number)
    dialogs = await client.get_dialogs()
    print("Chats list:")
    for i, dialog in enumerate(dialogs, start=1):
        print(f"{i}. {dialog.name}")

    chat_numbers = input("Please type the numbers of the chats from which you want to delete your messages: ")
    selected_chats = [dialogs[int(num) - 1] for num in chat_numbers.split(',')]

    for chat in selected_chats:
        async for message in client.iter_messages(chat):
            if message.out:
                print(f"Deleting message with ID {message.id}")
                await client.delete_messages(chat, message)

    print("All your messages from selected chats are gone by now.")

    await client.disconnect()

with client:
    client.loop.run_until_complete(main())