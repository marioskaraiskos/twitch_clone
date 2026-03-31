import os
import asyncio
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = os.getenv("BOT_USERNAME")
CHANNEL_NAME = os.getenv("CHANNEL_NAME")
OAUTH_TOKEN = os.getenv("OAUTH_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=OAUTH_TOKEN,
            prefix="!",
            initial_channels=[CHANNEL_NAME],
        )

    async def event_ready(self):
        print(f"Logged in as   | {self.nick}")
        print(f"User ID        | {self.user_id}")
        print(f"Channel        | {CHANNEL_NAME}")

    async def event_message(self, message):
        if message.echo:
            return

        print(f"{message.author.name}: {message.content}")

        if message.content.lower() == "hello":
            await message.channel.send(f"Hello @{message.author.name}! PogChamp")

        await self.handle_commands(message)

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {ctx.author.name}")
    @commands.command(name="nikos")
    async def nikos(self, ctx: commands.Context):
        await ctx.send(f"nikos stroggilos joined the crew! {ctx.author.name}")

    @commands.command(name="dice")
    async def dice(self, ctx: commands.Context):
        import random
        result = random.randint(1, 6)
        await ctx.send(f"@{ctx.author.name} rolled a {result}!")

    @commands.command(name="uptime")
    async def uptime(self, ctx: commands.Context):
        await ctx.send("Uptime command coming soon!")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()       # create a fresh event loop
    asyncio.set_event_loop(loop)          # set it as the current loop
    bot = Bot()
    bot.run()