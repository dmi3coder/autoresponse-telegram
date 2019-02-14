import time
from telethon import TelegramClient, events

# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own
api_id = YOUR_ID
api_hash = YOUR_HASH
# fill in your own details here
phone = '+3800000000000'
username = 'username'
password = 'password'  # if you have two-step verification enabled

# content of the automatic reply
message = """Due to high workload,  I am currently checking and responding to telegram twice daily at 13:00 GMT+2 and 16:00 GMT+2.\n
If you require urgent assistance (please ensure it is urgent) that cannot wait until either 13:00 or 16:00, please contact me via phone at +380000000000 \n
Thank you for understanding this move to more efficiency and effectiveness. It helps me accomplish more to serve you better.\n
Sincerely,\n
\n
Yourname
"""



def main():
    # Create the client and connect
    client = TelegramClient(username, api_id, api_hash, update_workers=1, spawn_read_thread=False)
    client.start(phone, password)

    @client.on(events.NewMessage(incoming=True))
    def _(event):
        if event.is_private:
            print(time.asctime(), '-', event.message)  # optionally log time and message
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            client.send_message(event.message.from_id, message)



    print(time.asctime(), '-', 'Auto-replying...')
    client.idle()
    client.disconnect()
    print(time.asctime(), '-', 'Stopped!')


if __name__ == '__main__':
    main()

