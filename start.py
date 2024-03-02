import os
import asyncio
import schedule
import time
from telegram import Bot

# Telegram bot token
TOKEN = "YOUR_BOT_TOKEN"
# Channel username (include @)
CHANNEL = "@ChannelName"
# Path to the file containing motivational posts
POSTS_FILE = "posts.txt"
# Interval between posting each message (in minutes)
POST_INTERVAL_MINUTES = 1

# Initialize the bot
bot = Bot(token=TOKEN)

async def post_to_channel():
    with open(POSTS_FILE, 'r', encoding='utf-8') as file:
        posts = file.readlines()

    for post in posts:
        # Post text message to the channel
        await bot.send_message(chat_id=CHANNEL, text=post.strip())
        # Wait for the specified interval before posting the next message
        await asyncio.sleep(POST_INTERVAL_MINUTES * 60)

# Schedule posting every 1 minute
schedule.every(1).minutes.do(lambda: asyncio.run(post_to_channel()))

# Main loop
while True:
    schedule.run_pending()
    time.sleep(1)
