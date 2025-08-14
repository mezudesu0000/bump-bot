import os
import pathlib

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("TOKENが設定されていません")

bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
    print(f"ログインが完了しました：{bot.user} (ID：{bot.user.id})")

    cog_path = pathlib.Path("cogs")
    for file in cog_path.glob("*.py"):
        if file.name.startswith("_"):
            continue
        module = f"cogs.{file.stem}"
        try:
            await bot.load_extension(module)
            print(f"読み込み成功：{module}")
        except Exception as e:
            print(f"読み込み失敗：{module} / {e}")

bot.run(TOKEN)