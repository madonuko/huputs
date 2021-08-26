from discord.ext import commands

bot = commands.Bot(">")


@bot.command()
async def oame(ctx):
    await ctx.send("howy")


if __name__ == "__main__":
    bot.run("ODU3NjAzMzM4NDgwMzg2MDQ4.YNR_WQ.bQJS9ujyMQtKzgkMvk5NbFakZGY")
