from logging import getLogger
from asyncio import gather

from discord.ext import commands
from discord.ext.commands import Context
from discord.utils import get

from constants import GetConstants

logger = getLogger(f"main.{__name__}")


async def selfClean(context: Context):
    """
    Deletes the message that invoked a command is possible
    """
    if context.guild is not None:
        await context.message.delete()


class Tools(commands.Cog):
    """
    A collection of functions used as utilities for other cogs
    """
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        """
        By default this command will delete the message that calls it
        @ctx: context object containing information about the caller
        @amount
        """
        await ctx.channel.purge(limit=amount)
        logger.debug(f"{ctx.author} has cleared the channel {ctx.channel} of {amount} messages")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        On new student joining guild assign them student role and send them a welcome message
        """
        role = get(member.guild.roles, name=GetConstants().STUDENT)
        await gather(member.add_roles(role),
                     member.send(f"{member.mention} welcome! You have been promoted to the role of Student"),
                     member.send(self.client.get_cog("Help").help_messages['all_student'])
                     )
        logger.debug(f"{member.author} has joined the server")


def setup(client):
    """
    Called internally by discord API cog functionality
    I honestly have no idea how this works...
    """
    client.add_cog(Tools(client))