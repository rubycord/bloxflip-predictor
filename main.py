from disnake.ext import commands
import disnake
import random
import time
from random import randint
import discord
import requests
import re
import uuid
# Create a new bot
bot = commands.Bot(command_prefix='.', intents=disnake.Intents.all())
import time
bot.remove_command('help')
import re
@bot.event
async def on_ready():
    print("Bot Is Ready")
#





bad =  "❌"
@bot.slash_command(description="Paid Mines")
@commands.has_role('Buyers')
async def paidmines(ctx, roundid):
  id = str(roundid)
  round_length = len(roundid)
  
  h = id.count("h")
  m = id.count("m")
  z = id.count("z")
  w = id.count("w")
  r = id.count("r")
  y = id.count("y")
  u = id.count("u")
  n = id.count("n")
  s = id.count("s")
  S = id.count("S")
  N = id.count("N")
  U = id.count("U")
  F = id.count("F")
  H = id.count("H")
  M = id.count("M")
  Z = id.count("Z")
  W = id.count("W")
  R = id.count("R")
  Y = id.count("Y")
  ex = id.count("!")
  ass = id.count("69")
  ques = id.count("?")
  slash = id.count("/")
  star = id.count("*")
  money = id.count("$")
  colon = id.count(":")
  doublecolon = id.count(";")
  percent = id.count("%")
  pound = id.count("£")
  at = id.count("@")
  plus = id.count("+")
  mul = id.count("x")
  shark = id.count("<")
  dot = id.count(".")
  shark1 = id.count(">")
  shark2 = id.count("^")
  shark3 = id.count("¥")
  shark4 = id.count("€")
  brack = id.count("[")
  brack1 = id.count("]")
  tag = id.count("#")
  dashcount = id.count("-")
  with open(f"ids.txt","r") as f:
    a = f.read()
    if roundid in a:
      embed = disnake.Embed(title="Paid Mines", description="ID Has Been Used", color=0xFF0000)
      await ctx.send(embed=embed)
      return
    else:
      if round_length < 36 or round_length > 36 or h > 0 or m > 0 or z > 0 or w > 0 or r > 0  or ex > 0 or ques > 0 or slash > 0 or star > 0 or money > 0 or colon > 0 or doublecolon > 0 or percent > 0 or pound > 0 or at > 0 or plus > 0 or mul > 0 or shark > 0 or dot > 0 or shark1 > 0 or shark or shark2 > 0 or shark3 > 0 or shark4 > 0 or brack > 0 or brack1 > 0 or tag > 0 or H > 0 or M > 0 or Z > 0 or W > 0 or R > 0 or Y > 0 or F > 0 or U > 0 or u > 0 or n > 0 or N > 0 or S > 0 or s > 0 or float(dashcount) != 4 or ass > 0:
        embed = disnake.Embed(title="Invalid Input", color=disnake.Color.red())
        await ctx.send(embed=embed)
      else:
          with open(f"ids.txt","a") as f:
            f.write(roundid + "\n")
          grid = ["✅", "❌", "❌", "❓", "✅", "❌", "🪙", "✅"]
      row1 = "Row 1: "+ random.choice(grid) + random.choice(grid) + random.choice(grid) + random.choice(grid) + f"{bad}"
      row2 = f"Row 2: {bad}" + f"{bad}" + f"{bad}" + f"{bad}" + f"{bad}"
      row3 = f"Row 3: {bad}"+ f"{bad}" + f"{bad}" + f"{bad}" + f"{bad}"
      row4 = f"Row 4: {bad}" + f"{bad}" + f"{bad}" + f"{bad}" + f"{bad}"
      row5 = f"Row 5: {bad}" + random.choice(grid) + f"{bad}" + random.choice(grid) + f"{bad}"
      randomasspredictor =   row1 + '\n' + row2 + '\n' + row3 + '\n' + row4 + '\n' + row5
  embed = disnake.Embed(title="Paid Mines", description=f"Grid:\n{randomasspredictor}", color=disnake.Colour.green())
  embed.add_field(name="Game Info:", value=f"✅ Safe Spot (not 100%)\n ❓Possible Bomb/Unknown\n ❌ Dont Go There\n 🪙 Possible Good Spot Using ID\n Round ID: {roundid}", inline=False)
  cash = [
    "First Clicked Tile",
    "Second Clicked Tile",
    "Third Clicked Tile",
  ]
  acc = ["47.0",
         "51.0",
         "54.0",
         "57.0",
         "60.0",
         "23.0",
         "24.0",
         "25.0"
        ]
  embed.add_field(name="Safe Cashout:\n", value=f"{random.choice(cash)}\n Win Chance: {random.choice(acc)}%", inline=False)
  embed.set_footer(text="Dm me for suggestions")
  await ctx.send(embed=embed)


@paidmines.error
async def paid_error(ctx, error):
    if isinstance(error, commands.MissingRole):
      embed = disnake.Embed(title="Error", description="You Must Be A Buyer To Use This Command", color=disnake.Color.red())
      await ctx.send(embed=embed, ephemeral=True)

import string
import discord, sqlite3 , rstr
#Key System

role = "Buyers"

@bot.slash_command(description="Check A Round ID")
@commands.has_role("Buyers")
async def checkid(ctx, id):
  check = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
  uuid = f'{id}'
  if check.match(id):
    embed = disnake.Embed(title="Real ID", description=f"The ID \n{id}", color=disnake.Colour.green())
    await ctx.send(embed=embed, delete_after=30)
  else:
    embed = disnake.Embed(title="Fake ID", description=f"The Fake ID \n{id}", color=disnake.Colour.red())
    await ctx.send(embed=embed, delete_after=30)
import asyncio



@checkid.error
async def check_error(ctx, error):
    if isinstance(error, commands.MissingRole):
      embed = disnake.Embed(title="Error", description="You Must Be A Buyer To Use This Command", color=disnake.Color.red())
      await ctx.send(embed=embed, ephemeral=True)

@bot.slash_command(description="Guess The Number")
async def guess(ctx, *, guess : int):
  x = randint(1, 300)
  if x == guess:
    key=rstr.xeger(r'guessthrnumberkey=[a-zA-Z\d]{25}')
    embed = disnake.Embed(title="Correct!", description=f"{ctx.author.mention} Congarts You have won life time of Maze Predictor\n/nDM Jester To Claim\n\nyour key is: {key}", color=disnake.Color.green())
    embed.set_footer(text=f"{ctx.author.mention}" + f" guessed {guess}")
    await ctx.send(embed=embed)
  else:
    embed = disnake.Embed(title=f"Incorrect The Number Was \n{x}", color=disnake.Color.red())
    await ctx.send(embed=embed, ephemeral=True)


@bot.slash_command(description="Credits")
async def credits(ctx):
  embed = disnake.Embed(title="Credits", description="Bot Made By Jester\n Guess The Number Helped By r3n\n Credits are amazing", color=disnake.Color.green())
  embed.set_footer(text="Dm me for suggestions")
  await ctx.send(embed=embed)

@bot.slash_command(description="Help")
async def help(ctx):
  embed = disnake.Embed(title="Help", description="Paid Commands:\n /paidmines {roundid}\n /check {id}\n Free Commands:\n /guess {number}, More Soon?", color=disnake.Color.green())
  embed.set_footer(text="Dm me for suggestions")
  await ctx.send(embed=embed)
import cloudscraper as cs
import requests



      
bot.run('MTA1NjA4NzkxNTY2MDMzMzA5Ng.GzZ0d5.XJ-cbU60RGwtJbZOWGkuexZYboycO6nAtMdMxg')
