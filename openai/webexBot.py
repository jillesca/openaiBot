import os

from webex_bot.commands.echo import EchoCommand
from webex_bot.webex_bot import WebexBot

# Create a Bot Object
bot = WebexBot(
    teams_bot_token=os.getenv("WEBEX_TEAMS_ACCESS_TOKEN"),
    approved_users="jillesca@cisco.com",
    bot_name="test NSO AI bot",
    include_demo_commands=True,
    bot_help_subtitle="For now only jillesca is available to work with me",
)

# Add new commands for the bot to listen out for.
bot.add_command(EchoCommand())

# Call `run` for the bot to wait for incoming messages.
bot.run()
