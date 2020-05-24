import logging
import pendulum
import traceback
import re

import discord

from discord.ext import commands
from discord.embeds import Embed
from discord.colour import Color
from django.conf import settings

#log = logging.getLogger(__name__)

class About(commands.Cog):
    """
    All about me!
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def about(self, ctx):
        """
        All about the bot
        """
        await ctx.trigger_typing()

        embed = Embed(title="AuthBot: The Authening")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/icons/516758158748811264/ae3991584b0f800b181c936cfc707880.webp?size=128"
        )
        embed.colour = Color.blue()

        embed.description = "This is a multi-de-functional discord bot tailored specifically for Alliance Auth Shenanigans."
        regex = r"^(.+)\/d.+"

        matches = re.finditer(regex, settings.DISCORD_CALLBACK_URL, re.MULTILINE)

        for m in matches:
            url = m.groups()
        embed.set_footer(text="Lovingly developed for Init.™ by AaronKable")

        embed.add_field(
            name="Number of Servers:", value=len(self.bot.guilds), inline=True
        )
        embed.add_field(name="Unwilling Monitorees:", value=len(self.bot.users), inline=True)
        embed.add_field(
            name="Auth Link", value="[{}]({})".format(url[0], url[0]), inline=False
        )

        embed.add_field(
            name="Creator", value="<@318309023478972417>", inline=False
        )

        return await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def uptime(self, ctx):
        """
        Returns the uptime
        """
        await ctx.send(
            pendulum.now(tz="UTC").diff_for_humans(
                self.bot.currentuptime, absolute=True
            )
        )

def setup(bot):
    bot.add_cog(About(bot))
