from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
TRPGmode = "None"
TRPGtype = ["CoC","Paranoia","Others"]

#change TRPG mode
@bot.command()
async def mc(ctx,arg):
    if(arg in TRPGtype):
        TRPGmode = arg
        await ctx.send(f"now changed TRPGmode to {arg}\r\nモードを {arg} に変更しました")
    else:
        await ctx.send(f"this mode isn't supported\r\nそのモードは存在しません")

#AdB to roll B-sides dices A times
@bot.command()
async def r(ctx,arg):
    #prepare
    vals=arg.split('d')
    times=int(vals[0])
    sides=int(vals[1])
    results=[]
    rsltsum=0
    #diceroll
    for i in range(vals[0]):
        roll=random.randint(1,sides)
        results.append(roll)
        rsltsum+=roll
    #result
    await ctx.send(f"roll {arg} -> {rsltsum} : {results}")
    
bot.run(token)
