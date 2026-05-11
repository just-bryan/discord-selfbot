import discord
import os

TOKEN = os.getenv("TOKEN")  # Make sure to set your token in the environment variables
ALERT_CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # Set the alert channel ID in environment variables

class SelfBot(discord.Client):
    async def on_ready(self):
        print(f"✅ Logged in as {self.user}")
        print(f"📡 Monitoring {len(self.guilds)} servers")
        
        channel = self.get_channel(ALERT_CHANNEL_ID)
        if channel:
            await channel.send("🤖 Self-bot is now watching for new members")
        else:
            print("❌ Could not find channel — check channel ID")

    async def on_member_join(self, member):
        channel = self.get_channel(ALERT_CHANNEL_ID)
        if channel:
            await channel.send(f"🔔 {member.name} joined {member.guild.name}")
            print(f"✅ Alert sent: {member.name} joined {member.guild.name}")

# No intents! Self-bots don't use them
client = SelfBot()
client.run(TOKEN)