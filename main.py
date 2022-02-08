import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="b.", help_command=None, intents = discord.Intents().all(), case_insensitive=True)
lower = "Beatrice | paradise#0666"
token = "YOUR TOKEN"

@bot.event
async def on_ready():
    print("Logged user {}".format(bot.user.name))
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="b. | beatrice-bot.com"), status=discord.Status.online)





bot.run(token)
