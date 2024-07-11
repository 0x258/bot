import discord
from discord import app_commands
import requests
import os

intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1260607757577355285))
    print(f'bot ready - Mr Paypal is here... {client.user}')

@tree.command(name="help", description="self explanitory", guild=discord.Object(id=1260607757577355285))
async def _help(interaction: discord.Interaction):
    embed = discord.Embed(title="Purchase Methods", description="", color=0x000000)
    embed.add_field(name="/Paypal", value="sends u a paypal link which u need to buy from", inline=False)
    embed.add_field(name="/Robux", value="sends u a gamepass link which u need to buy from", inline=False)
    embed.add_field(name="/Crypto", value="tells u what to do", inline=False)
    embed.add_field(name="/Giftcard", value="tells u what to do", inline=False)
    embed.add_field(name="/Skins", value="tells u what to do", inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(name="paypal", description="sends u a paypal link which u need to buy from", guild=discord.Object(id=1260607757577355285))
async def _getkey(interaction: discord.Interaction):
    try:
        user_role = discord.utils.get(interaction.user.roles, name='buyer')
        if user_role is None:
            await interaction.response.send_message('## Link Which U Need To Buy From >> __https://Paypal.me/akisiccc <@1007004756880932864>__', ephemeral=False)
            return

        user_id = interaction.user.id

        if user_id in user_keys:
            key = user_keys[user_id]
            embed = discord.Embed(description=f'User found in database, key: {key}')
        else:
            url = 'https://keyauth.win/api/seller/?sellerkey=9e67d6e2f007c4ef3d14b5751b24d090&type=add&expiry=9999&mask=wasted-******-******-******-******-******&level=1&amount=1&format=text'
            response = requests.get(url)
            if response.status_code == 200:
                key = response.text.strip()
                user_keys[user_id] = key
                save_keys()
                embed = discord.Embed(description=f'key generated: {key}')
            else:
                await interaction.response.send_message(f'failed to gen key error code: {response.status_code}', ephemeral=False)
                return

        await interaction.user.send(embed=embed)
        await interaction.response.send_message(f'Key has been sent to your DMs, {interaction.user.mention}.', ephemeral=False)

    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {str(e)}', ephemeral=False)
        print(f'Error: {str(e)}')
    
@tree.command(name="robux", description="sends u a gamepass link which u need to buy from", guild=discord.Object(id=1260607757577355285))
async def _unwhitelist(interaction: discord.Interaction):
    try:
        user_role = discord.utils.get(interaction.user.roles, name='sperm')
        if user_role is None and interaction.user.id != 1261016329461301329:
            await interaction.response.send_message('## Script Gamepass >> __https://www.roblox.com/game-pass/858084316/SCRIPT-INTEREST-LOL__ AimAssist Gamepass >> __https://www.roblox.com/game-pass/858105369/Ahk-aim-assistance__ ', ephemeral=False)
            return

        if days <= 0:
            await interaction.response.send_message('please provide valid num.', ephemeral=False)
            return

        user_id = user.id

        if user_id in user_keys:
            key = user_keys[user_id]
            embed = discord.Embed(description=f'User found in database, key: {key}')
        else:
            url = f'https://keyauth.win/api/seller/?sellerkey=9e67d6e2f007c4ef3d14b5751b24d090&type=add&expiry={days}&mask=wasted-******-******-******-******-******&level=1&amount=1&format=text'
            response = requests.get(url)
            if response.status_code == 200:
                key = response.text.strip()
                user_keys[user_id] = key
                save_keys()

                buyer_role = discord.utils.get(interaction.guild.roles, name='buyer')
                if buyer_role is not None:
                    if buyer_role not in user.roles:
                        await user.add_roles(buyer_role)

                embed = discord.Embed(description=f'key generated: {key}')
            else:
                await interaction.response.send_message(f'failed to generate key: {response.status_code}', ephemeral=False)
                return

        await user.send(embed=embed)
        await interaction.response.send_message(f'key has been sent to {user.mention}', ephemeral=False)

    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {str(e)}', ephemeral=False)
        print(f'Error: {str(e)}')

@tree.command(name="crypto", description="tells u what to do", guild=discord.Object(id=1260607757577355285))
async def _resethwid(interaction: discord.Interaction):
    try:
        user_role = discord.utils.get(interaction.user.roles, name='support')
        if user_role is None and interaction.user.id != 1261016329461301329:
            await interaction.response.send_message('## Hi To Buy With Crypto U Need To Wait For __<@1214792621923246114>__', ephemeral=False)
            return

        if user.id not in user_keys:
            await interaction.response.send_message('No key found for this user.', ephemeral=False)
            return

        key = user_keys[user.id]
        url = f'https://keyauth.win/api/seller/?sellerkey=9e67d6e2f007c4ef3d14b5751b24d090&type=resetuser&user={key}'
        response = requests.get(url)
        if response.status_code == 200:
            embed = discord.Embed(description='hwid has been reset successfully.')
            await user.send(embed=embed)
            await interaction.response.send_message(f'hwid reset successful, check dms {user.mention}.', ephemeral=False)
        else:
            await interaction.response.send_message(f'failed to reset hwid error code: {response.status_code}', ephemeral=False)

    except Exception as e:
        await interaction.response.send_message(f'error: {str(e)}', ephemeral=False)
        print(f'Error: {str(e)}')

@tree.command(name="giftcard", description="tells u what to do", guild=discord.Object(id=1260607757577355285))
async def _blacklist(interaction: discord.Interaction):
    try:
        user_role = discord.utils.get(interaction.user.roles, name='sperm')
        if user_role is None and interaction.user.id != 1261016329461301329:
            await interaction.response.send_message('## Hi To Buy With Giftcard U Need To Wait For __<@1007004756880932864>__', ephemeral=False)
            return

        user_id = user.id

        if user_id not in user_keys:
            await interaction.response.send_message('user not in db.', ephemeral=False)
            return

        key = user_keys[user_id]

        url = f'https://keyauth.win/api/seller/?sellerkey=ddc9b297c80a2efaf271a847c80e6071&type=banuser&user={key}&reason={reason}'
        response = requests.get(url)
        if response.status_code == 200:
            buyer_role = discord.utils.get(interaction.guild.roles, name='buyer')
            if buyer_role in user.roles:
                await user.remove_roles(buyer_role)
            embed = discord.Embed(description=f'{user.mention} has been blacklisted. Reason: {reason}')
            await interaction.response.send_message(embed=embed, ephemeral=False)
        else:
            await interaction.response.send_message(f'failed to blacklist user, error code: {response.status_code}', ephemeral=False)

    except Exception as e:
        await interaction.response.send_message(f'an error occurred: {str(e)}', ephemeral=False)
        print(f'Error: {str(e)}')


@tree.command(name="skins", description="tells u what to do", guild=discord.Object(id=1260607757577355285))
async def _unblacklist(interaction: discord.Interaction):
    try:
        user_role = discord.utils.get(interaction.user.roles, name='sperm')
        allowed_user_id = 1261016329461301329

        if user_role is None and interaction.user.id != allowed_user_id:
            await interaction.response.send_message('## Hi To Buy With Dh Skins U Need To Wait For __<@1007004756880932864>__', ephemeral=False)
            return

        if len(inputofuser) == 44:
            oii = f"hwid={inputofuser}"
        else:
            oii = f"ip={inputofuser}"

        sellerkey = 'ddc9b297c80a2efaf271a847c80e6071'
        req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=delblack&{oii}")

        if req.status_code == 200 and req.json().get("success", False):
            await interaction.response.send_message(embed=discord.Embed(title="successfully unblacklisted user", description=f"{interaction.user.mention}, Unblacklisted {inputofuser}"), ephemeral=False)
        else:
            await interaction.response.send_message(embed=discord.Embed(title="Failed To Unblacklist", description=f"{interaction.user.mention}"), ephemeral=False)

    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {str(e)}', ephemeral=False)
        print(f'Error: {str(e)}')


client.run('bot token')

