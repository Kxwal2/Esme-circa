"""Extension module to change character id encoding."""
import traceback
import logging

import discord

from settings import CONFIG
from core import cid
from core.exceptions import (
    MissingPermissions
)

class ToolCID():
    """Cog handling cid encoding."""
    async def tool_encode(
        self,
        interaction: discord.Interaction,
        character_id: int
    ):
        """Return alphabetical character id."""
        try:
            if not CONFIG.check_permission(
                CONFIG.commands.tool_cid.permission,
                interaction.user
            ):
                raise MissingPermissions(
                    f"{interaction.user.mention} is missing permissions to use command."
                )

            char_id: str = cid.encode_cid(character_id)

            await interaction.response.send_message(
                embed=discord.Embed(
                    title="Character ID",
                    description=f"```{char_id}```",
                    color=discord.Color.green()
                ),
                ephemeral=True
            )

        except (
            MissingPermissions
        ) as e:
            logging.warning("%s: %s", interaction.user.id, e)
            await interaction.response.send_message(
                embed=discord.Embed(
                    title="Character ID Failed",
                    description=e,
                    color=discord.Color.red()
                ),
                ephemeral=True
            )

        except (
            Exception
        ) as e:
            logging.error("%s: %s %s %s", interaction.user.id, type(e), e, traceback.format_exc())
            await interaction.response.edit_message(
                embed=discord.Embed(
                    title="Procesing Failed",
                    description="Internal Error.",
                    color=discord.Color.red()
                )
            )

    async def tool_decode(
        self,
        interaction: discord.Interaction,
        character_id: str
    ):
        """Return integer character id."""
        try:
            if not CONFIG.check_permission(
                CONFIG.commands.tool_cid.permission,
                interaction.user
            ):
                raise MissingPermissions(
                    f"{interaction.user.mention} is missing permissions to use command."
                )

            char_id: int = cid.decode_cid(character_id)

            await interaction.response.send_message(
                embed=discord.Embed(
                    title="Character ID",
                    description=f"```{char_id}```",
                    color=discord.Color.green()
                ),
                ephemeral=True
            )

        except (
            MissingPermissions
        ) as e:
            logging.warning("%s: %s", interaction.user.id, e)
            await interaction.response.send_message(
                embed=discord.Embed(
                    title="Character ID Failed",
                    description=e,
                    color=discord.Color.red()
                ),
                ephemeral=True
            )

        except (
            Exception
        ) as e:
            logging.error("%s: %s %s %s", interaction.user.id, type(e), e, traceback.format_exc())
            await interaction.response.edit_message(
                embed=discord.Embed(
                    title="Procesing Failed",
                    description="Internal Error.",
                    color=discord.Color.red()
                )
            )
