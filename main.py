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
        await asyncio.sleep(16)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="version | 0.0.1-alpha"), status=discord.Status.online)
        await asyncio.sleep(16)


@bot.command()
async def help(ctx, arg:str=" ⠀"):
    if arg == " ⠀":
        helpembed = discord.Embed(title="Beatrice's commandlist",
                                  description="To look into different sections use `b.help [section]`\n\nHow to understand commands:\n`[]` needs to be given.\n`()` doesnt need to be given.\n**Quick reminder: Do not include `[]`,`()` into the command.**",
                                  color=0xffbddf)
        helpembed.add_field(name="⚙️Moderation", value="_Useful commands to administrate\n your Server and keep it safe._", inline=True)
        helpembed.add_field(name="⁉️Information", value="_Grab informations about\n User, Emotes & more_", inline=True)

        helpembed.set_footer(text="{}".format(lower))
        mess = await ctx.channel.send(embed=helpembed)
    if "moderation" == arg.casefold():
        modembed = discord.Embed(title="Beatrice's Moderation commands",
                          description="",
                          color=0xffbddf)
        modembed.add_field(name="⚙️Moderation", value="Test", inline=False)
        modembed.set_footer(text="{}".format(lower))
        mess = await ctx.channel.send(embed=modembed)
    if "Information" == arg.casefold():
        infoembed = discord.Embed(title="Beatrice's Information commands",
                          description="",
                          color=0xffbddf)
        infoembed.add_field(name="⁉️Information", value="Test", inline=False)
        infoembed.set_footer(text="{}".format(lower))
        mess = await ctx.channel.send(embed=infoembed)
bot.run(token)
