




###

### HETETROFITNESS PROJECT ###

###

import discord
from datetime import datetime
import time
from discord.ext import commands, tasks
import asyncio
from discord.ext.commands import bot
import random

#Client (the bot)
client = commands.Bot(command_prefix='?')

### INTRODUCTION CODE ###

@client.event
async def on_ready(): #async = function runs even when there's a delay
    #now we can do stuff! functionalities n whatever

    #[CHANGE FOR HETETRO] CHANGE TO LOUNGE CHANNEL ID WHEN RUNNING OFFICIALLY
    lounge = client.get_channel(CHANNEL ID) 

    intro_message = (
        'HI KLOWNS! My name is HetetroFitness, and I was created to serve the Great House Hetetro and all its klown kweens. I\'m told that Hetetro\'s Discord keeps going dead (lmao oop), but because server fitness is important, I will send a message in hourly intervals whenever we go dead, if you so please, to help things along. My command is just a simple "?watch", and I\'ll watch over the lounge for 7 hours. Thank you for inviting me here, and I hope you like me! And now my watch begins. #LongLiveHetetro'
        )

    await lounge.send(intro_message)
    #await waits for lounge chat to be retrieved first


### FITNESSGRAM TIMED CODE ###

'''
@client.command()
async def check_if_embed(message):
    if len(message.embeds) > 0:
        return True
'''

@client.command()
async def watch(ctx):

    #timezone aware - Pacific Time
    #pacific = timezone('US/Pacific')

    initiation_msg = (f'Channel watch sequence commencing at {ctx.message.created_at}, initiated by {ctx.author}. If no messages are sent within hourly intervals, well then that\'s just sad.')
    await ctx.send(initiation_msg)
    await asyncio.sleep(10)
    
    channel = client.get_channel(CHANNEL ID)
    last_msg = await channel.history(limit=1).flatten()
    for msg in last_msg:
        time_since_command = (msg.created_at - ctx.message.created_at).total_seconds() #msg.created_at is the last msg in channel. ctx is cmd msg.
        #await channel.send(f'Time difference between last message and {ctx.author}\'s watch sequence intiation: {time_since_command} seconds.')
        
        if time_since_command <= 1.0:

            FitnessGram = ('The FitnessGram??? Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [BEEP] A single lap should be completed each time you hear this sound. [DING] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.')
            
            pastels = [
            0xFFB5E8, 0xFF9CEE, 0xF6A6FF,0xB28DFF, 0xC5A3FF, 0xC5A3FF, 0xD5AAFF, 0xDCD3FF, 0xA79AFF, 0xB5B9FF, 0x97A2FF, 
            0xAFCBFF, 0xAFF8DB, 0xC4FAF8, 0x85E3FF, 0x6EB5FF, 0xBFFCC6, 0xE7FFAC, 0xFFC9DE, 0xFFABAB, 0xFFF5BA
            ]
            random_color = random.choice(pastels)

            FitnessGramEmbed = discord.Embed(
                title='"This is so sad."', 
                color=random_color
                )
            
            FitnessGramEmbed.add_field(
                name='-------------------------------------------------------------',
                value=FitnessGram, 
                inline=True
                )

            FG_images = [
                'https://i.ytimg.com/vi/VBnpRw33Tlw/maxresdefault.jpg', #kermit in the car
                'https://i.ytimg.com/vi/KTSxDblqFGk/hqdefault.jpg', #our pain emoji
                'https://smartland.com/blog/wp-content/uploads/2019/12/Cat-1.jpg', #crying cat
                'https://media.discordapp.net/attachments/838551816672641025/867299586477260810/unknown.png?width=423&height=406', #my man o'hare
                'https://cdn.discordapp.com/attachments/867888077992755220/875214404239622224/30b564c24538fd643b865c6f2714afc2.png', #sad barry
                'https://cdn.discordapp.com/attachments/867888077992755220/875214638810271765/50639c1a376a7a9751d761bb0aff1939.png', #kermit in the shower
                'https://media.discordapp.net/attachments/867888077992755220/875215443965648976/0vrps-27ylr90z7ta31.png?width=618&height=406' #sad shrek
            ]         
            random_img = random.choice(FG_images)
            FitnessGramEmbed.set_image(url=random_img)

            await channel.send(embed=FitnessGramEmbed)
        else:
            await channel.send('Good job y\'all for talking lol')

    i = 2 #next hour run
    while i < 8:
        await asyncio.sleep(10)
        channel = client.get_channel(CHANNEL ID)
        next_last_msg = await channel.history(limit=1).flatten()
        for new_msg in next_last_msg:
            time_since_last_hour_mark = (new_msg.created_at - ctx.message.created_at).total_seconds()
            if time_since_last_hour_mark >= 11.0:
                await channel.send(embed=FitnessGramEmbed)   
                
            else:
                await channel.send('Good job y\'all for talking lmao')

        i += 1

    channel = client.get_channel(867546695842529303)
    await channel.send('Watch sequence complete. Have a nice day! Or not idk.')

client.run('TOKEN')
bot.run('TOKEN')


