import discord
import os
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
QUEUE_CHANNEL_ID = int(os.getenv("QUEUE_CHANNEL_ID"))
ADMIN = os.getenv("ADMIN")
STUDENT = os.getenv("STUDENT")
INSTRUCTOR_ROLE_ID = int(os.getenv("INSTRUCTOR_ROLE_ID"))
STUDENT_ROLE_ID = int(os.getenv("STUDENT_ROLE_ID"))
DISCORD_GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))

client = commands.Bot(command_prefix=">")
client.remove_command("help")




if __name__ == '__main__':
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
    client.run(BOT_TOKEN)