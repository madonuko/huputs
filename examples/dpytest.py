from discord.ext import commands

import bot
from huputs import TestThingsOut, empty

lets = TestThingsOut()


@lets.add_test("oame test").for_fn(bot.oame)
async def test_oame():
    ctx = empty(commands.Context)()
    ctx.send = lets.override(ctx.send).makeItDoNothing()
    ctx.send = lets.inject(ctx.send)
    await bot.oame(ctx)
    lets.make_sure(ctx.send).ran_with_exactly("howy")


lets.do_this()
