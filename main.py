import sys
from time import sleep
sys.path.insert(0, 'discord.py-self')
sys.path.insert(0, 'discord.py-self_embed')

import discord
from discord.ext import commands
import json
import socket 
from colorama import Fore, Back, Style
import os
import random
import string
import aiohttp

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
masked_ip = '.'.join(['*'*len(octet) for octet in ip_address.split('.')])

with open('config1.json', 'r') as file:
    config = json.load(file)



token = config['token']
prefix = config['prefix']
owner_id = config['admin_id']
owner = config['admin_username']
owner_server = config['admin_server']
about_owner = config['about_admin']
apiKey = config["apiKey"]

me = f"<@{owner_id}>"

ip = input()

bot = commands.Bot(command_prefix=prefix)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print(Fore.MAGENTA + '''
       ╔════════════════════════════════════════════════════════════════════════════════════════════════════╗
       ║██████╗░██╗░░██╗░██╗░░░░░░░██╗██╗░██████╗  ░██████╗███████╗██╗░░░░░███████╗██████╗░░█████╗░████████╗║
       ║██╔══██╗██║░██╔╝░██║░░██╗░░██║╚█║██╔════╝  ██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗██╔══██╗╚══██╔══╝║
       ║██████╔╝█████═╝░░╚██╗████╗██╔╝░╚╝╚█████╗░  ╚█████╗░█████╗░░██║░░░░░█████╗░░██████╦╝██║░░██║░░░██║░░░║
       ║██╔═══╝░██╔═██╗░░░████╔═████║░░░░░╚═══██╗  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██╗██║░░██║░░░██║░░░║
       ║██║░░░░░██║░╚██╗░░╚██╔╝░╚██╔╝░░░░██████╔╝  ██████╔╝███████╗███████╗██║░░░░░██████╦╝╚█████╔╝░░░██║░░░║
       ║╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░║ 
       ╚════════════════════════════════════════════════════════════════════════════════════════════════════╝
      ''')

@bot.event
async def on_ready():
   print(Fore.MAGENTA + f'''
  » Logged in as:\r
  » User: ''' + Fore.GREEN + f'{bot.user.name}' + Fore.MAGENTA + ''' \r
  » ID: ''' + Fore.GREEN + f'{bot.user.id}' + Fore.MAGENTA + ''' \r
  » Admin: ''' + Fore.GREEN + f'{owner}' + Fore.MAGENTA + '''
  » Admin ID: ''' + Fore.GREEN + f'{owner_id}' + Fore.MAGENTA + '''
  » CONNECTED @ IP ; ''' + Fore.GREEN + f'{ip_address}' + Fore.MAGENTA + '''
  » HIDDEN CMDS ;
  » ''' + Fore.RED + '>' + Fore.GREEN + 'lol' + Fore.MAGENTA + ' - SERVER RAID METHOD / "FUCKED BY PKW"' + '''
  » ''' + Fore.RED + '>' + Fore.GREEN + 'chaos' + Fore.MAGENTA + ' - SERVER RAID METHOD / "RANDOMIZED NAMES CHAOS"' + '''

        ''')
   print("-" * 35)
   print('''
  » If you need help please type ''' + Fore.GREEN + "'help'" + Fore.MAGENTA + ''' in the command bar below.
  » If not, just press enter.
        ''')
   print("-" * 70)
   print()
   cmd = input(Fore.GREEN + "   [$] Input: " + Fore.MAGENTA)
   await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name="HEIL PKW"))
   if cmd == "help" or cmd == "Help":
        print(Fore.BLUE + """
  » Hiya there ya little """+ Fore.RED + "mischief!" + Fore.BLUE + """ if you're looking for help on how to use this tool 
  » go ahead and type """ + Fore.GREEN + "'cmds'" + Fore.BLUE + """ in  a channel by typing your prefix
    ( > by default ) and typing cmds after! like this:
              
    """ + Fore.RED + ">" + Fore.GREEN + "cmds" + Fore.BLUE + """
              
  » Aaand... you're set my friend! have fun!
    (You can now minimize this and use your bot.)
              """)
   if cmd == "" or cmd == " ":
     print(Fore.BLUE + "\n""  » BOT is " + Fore.GREEN + "online." + Fore.BLUE + "\n \n""    (You can now minimize this window and use your bot)")

  
@bot.command()
async def admin(ctx):
    if str(ctx.author.id) in owner_id:
        await ctx.send(f'> # >Admin;\n> ```\n> Logged in as:\n> User: {bot.user.name}\n> ID: {bot.user.id}\n> CONNECTED @ IP ; {masked_ip}\n> Creation date: {bot.user.created_at.strftime("%d-%m-%Y, %H:%M:%S")}\n> Admin User: {owner}\n> Admin ID: {owner_id} \n> About: {about_owner}\n> Server: {owner_server}```')

@bot.command()
async def ping(ctx):
    user_id = str(ctx.author.id)
    if user_id in owner_id:
      await ctx.send(f'> # >Ping;\n> ```Pong!, {round(bot.latency * 1000 / 1000)}ms```')
      print(Fore.MAGENTA + "  » Ping: ")
      print(Fore.MAGENTA + "  » Pong! " + Fore.GREEN + f'{round(bot.latency * 1000 / 1000)}ms' + Fore.MAGENTA + "")
    
@bot.command()
async def whois(ctx, user: discord.User):
    if str(ctx.author.id) in owner_id:
     await ctx.send(f'> # >Whois;\n> ```\n> Username: {user.name}#{user.discriminator}\n> ID: {user.id}\n> Creation date: {user.created_at.strftime("%d-%m-%Y, %H:%M:%S")}\n> Pfp link:``` <{user.avatar}>')
     print(Fore.MAGENTA + "  » Whois: ")
     print(Fore.MAGENTA + "  » User: " + Fore.GREEN + f'{user.name}#{user.discriminator}' + Fore.MAGENTA + "")
     print(Fore.MAGENTA + "  » ID: " + Fore.GREEN + f'{user.id}' + Fore.MAGENTA + "")
     print(Fore.MAGENTA + "  » Creation date: " + Fore.GREEN + f'{user.created_at.strftime("%d-%m-%Y, %H:%M:%S")}' + Fore.MAGENTA + "")
     print(Fore.MAGENTA + "  » Pfp link: " + Fore.GREEN + f'{user.avatar}' + Fore.MAGENTA + "")

@bot.command()
async def geoloc(ctx, ip):
    if str(ctx.author.id) in owner_id:
     print(Fore.MAGENTA + "  » Geolocated: " + Fore.GREEN + f'{ip}')
     url = f"https://api.ipgeolocation.io/ipgeo?apiKey={apiKey}&ip={ip}"
     async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    output = f"> # >Geoloc;\n> ```\n> IP: {data['ip']}\n> Country: {data['country_name']}\n> State: {data['state_prov']}\n> City: {data['city']}\n> District: {data['district']}\n> Lat / Long: ({data['latitude']}, {data['longitude']})\n> ISP: {data['isp']}\n> Org: {data['organization']}\n> Zip Code: {data['zipcode']}\n> Is in the EU?: {data['is_eu']}\n> Timezone: {data['time_zone']}\n> Currency: {data['currency']}```"
                    await ctx.send(output)
                else:
                    await ctx.send("Failed to fetch geolocation data.")
    else:
        await ctx.send("You are not authorized to use this command.")


@bot.command()
async def ban(ctx, user: discord.User, *, reason=None):
  if str(ctx.author.id) in owner_id:
   await ctx.guild.ban(user, reason=reason)
   await ctx.send(f'> # >Ban;\n> ```\n> Banned {user.name}\n> Description:\n> Username: {user.name}#{user.discriminator}\n> ID: {user.id}\n> Reason: {reason}```')
   print(Fore.MAGENTA + "  » Banned User: ")
   print(Fore.MAGENTA + "  » User: " + Fore.GREEN + f'{user.name}#{user.discriminator}' + Fore.MAGENTA + "")
   print(Fore.MAGENTA + "  » ID: " + Fore.GREEN + f'{user.id}' + Fore.MAGENTA + "")
   print(Fore.MAGENTA + "  » Reason: " + Fore.GREEN + f'{reason}' + Fore.MAGENTA + "")

@bot.command()
async def kick(ctx, user: discord.User, *, reason=None):
  if str(ctx.author.id) in owner_id:
   await ctx.guild.kick(user, reason=reason)
   await ctx.send(f'> # >Kick;\n> ```\n> Kicked {user.name}\n> Description:\n> Username: {user.name}#{user.discriminator}\n> ID: {user.id}\n> Reason: {reason}```')
   print(Fore.MAGENTA + "  » Kicked User: ")
   print(Fore.MAGENTA + "  » User: " + Fore.GREEN + f'{user.name}#{user.discriminator}' + Fore.MAGENTA + "")
   print(Fore.MAGENTA + "  » ID: " + Fore.GREEN + f'{user.id}' + Fore.MAGENTA + "")
   print(Fore.MAGENTA + "  » Reason: " + Fore.GREEN + f'{reason}' + Fore.MAGENTA + "")

@bot.command()
async def pingall(ctx, msg=""):
  if str(ctx.author.id) in owner_id:
   await ctx.send(f"> # >PingAll;\n> ```{msg}```\n> @everyone")
   print(Fore.MAGENTA + "  » Pinged" + Fore.GREEN + f'@everyone' + Fore.MAGENTA + "")
   print(Fore.MAGENTA + "  » Reason: " + Fore.GREEN + f'{msg}' + Fore.MAGENTA + "")

@bot.command()
async def greet(ctx):
  if str(ctx.author.id) in owner_id:
   import random
   greets = [f"Hiya! i'm {me}'s personal bot!!! he is very cool for creating me and i need to obey him now haha\n ... help", f"Hiya gamers! i'm {me}'s bot! nice to meet ya!", f"Hi i'm {me}'s bot . . . \n i'm very cool i swear!", f"Heya! i'm {me}'s personal bot! ''Spam'' to meet ya ;)", f"woah woah! hey gamers! i'm {me}'s personal bot! i do things i guess."]
   await ctx.send(random.choice(greets))


@bot.command()
async def pfp(ctx, user: discord.User):
  if str(ctx.author.id) in owner_id:
   avatar_url = user.avatar.url
   await ctx.send("> # >Pfp;\n"+ avatar_url)

@bot.command()
async def banner(ctx, user: discord.User):
  if str(ctx.author.id) in owner_id:
   banner_url = user.banner.url
   await ctx.send("> # >Pfp;\n"+ banner_url)

@bot.command()
async def slurlist(ctx):
  if str(ctx.author.id) in owner_id:
   await ctx.send("> # >SlurList;\n> ```Welcome! today we're showcasing a list of slurs! in fact, top 20 slurs you should use in 2023!\n> let's start :)\n> NIGGER \n> NEGRO \n> SLAVE BOY \n> NIGGA\n> BLACK NIGGER\n> APE\n> MONKEY\n> SLAVE\n> NIGGEROS\n> 500 teeth dinosaur\n> FAGGOT\n> FAG\n> TRANNY\n> RETARD \n> VEGETABLE \n> SPED\n> REVERSE ADHD\n> BANANA\n> COTTON PICKER \n> ok i dont kno :3 \n> good bye my niggor back 2 d lobby XP```")

@bot.command()
async def prepack(ctx):
  if str(ctx.author.id) in owner_id:
   await ctx.send('\nNigger shut your ass up before i pack your stupid nasty nigga ass so hard your long lost father will come back to watch XDDDDD fucking kill yourself nasty ass nigga you dirty as hell dumb ass nigga you a fucking vegetable dont speak like that to me dumb ass slave nigga go back to your cage or im gonna have to cuff you to the pole like a DOG like you are bark for me you little black slave, woof! woof! shut your bitch ass up dumb ass nigger you stupid as hell bitch ass nigga you nasty asf wtf u doin you miserable fucktard go get a life and touch some grass maybe try making friends every once in a while? oh right i almost forgot youre a stupid ass nigga who cant socialize my bad bro! kill yourself you dirty nigger you dumb as shit bitch ass nigga stop wasting our oxygen you worthless piece of shit slave go pick some cotton and choke on kfc you nasty nigger')

@bot.command()
async def spam(ctx, msg="\n> OH UH!\n> LOOKS LIKE WE DID A FUCKY WUCKYYY :3\n> FUCKED BY PKW\n> WHO IS PKW?\n> PKW IS A DISCORD INDIVIDUAL THAT JUST FUCKED YOU OVER WITH SPAM! HAH!\n> DISCORD: <https://discord.gg/UTWMshSKzy>"):
  if str(ctx.author.id) in owner_id:
   for i in range(1000):
       await ctx.send(f'> # Spam to meet ya!\n> {msg}')

@bot.command()
async def spamping(ctx, ping="@everyone", msg="\n> OH UH!\n> LOOKS LIKE WE DID A FUCKY WUCKYYY :3\n> FUCKED BY PKW\n> WHO IS PKW?\n> PKW IS A DISCORD INDIVIDUAL THAT JUST FUCKED YOU OVER WITH SPAM! HAH!\n> DISCORD: <https://discord.gg/UTWMshSKzy>"):
  if str(ctx.author.id) in owner_id:
   for i in range(1000):
       await ctx.send(f'> # Spam to meet ya!\n>  {msg}\n> {ping}')


@bot.command()
async def spamlink(ctx, ping="@everyone", msg="\n> OH UH!\n> LOOKS LIKE WE DID A FUCKY WUCKYYY :3\n> FUCKED BY PKW\n> WHO IS PKW?\n> PKW IS A DISCORD INDIVIDUAL THAT JUST FUCKED YOU OVER WITH SPAM! HAH!\n> DISCORD: <https://discord.gg/UTWMshSKzy>", link="https://media.discordapp.net/attachments/893961597989572621/1107759935808348301/5D931066-8E14-4CFD-84D8-FE5D851AB3F1.gif"):
  if str(ctx.author.id) in owner_id:
   for i in range(1000):
       await ctx.send(f'> # Spam to meet ya!\n> {msg}\n> {ping}\n> {link}')

@bot.command()
async def spamall(ctx, num_messages=3, ping="@everyone", msg="OH UH!\n> LOOKS LIKE WE DID A FUCKY WUCKYYY :3\n> FUCKED BY PKW\n> WHO IS PKW?\n> PKW IS A DISCORD INDIVIDUAL THAT JUST FUCKED YOU OVER WITH SPAM! HAH!\n> DISCORD: <https://discord.gg/UTWMshSKzy>", link="https://media.discordapp.net/attachments/893961597989572621/1107759935808348301/5D931066-8E14-4CFD-84D8-FE5D851AB3F1.gif"):
  if str(ctx.author.id) in owner_id: 
   guild = ctx.guild

   for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            for _ in range(num_messages):
                await channel.send(f'> # FUCKED BY YOUR FAVE, PKW!\n> {msg}\n> {ping}\n> {link}')

@bot.command()
async def lol(ctx, num_messages=3, ping="@everyone", msg="OH UH!\n> LOOKS LIKE WE DID A FUCKY WUCKYYY :3\n> FUCKED BY PKW\n> WHO IS PKW?\n> PKW IS A DISCORD INDIVIDUAL THAT JUST FUCKED YOU OVER WITH SPAM! HAH!\n> DISCORD: <https://discord.gg/UTWMshSKzy>", link="https://media.discordapp.net/attachments/893961597989572621/1107759935808348301/5D931066-8E14-4CFD-84D8-FE5D851AB3F1.gif"):
 if str(ctx.author.id) in owner_id: 
    
    guild = ctx.guild

    await guild.edit(name='FUCKED BY PKW :3')

    # Change text and voice channel names
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel) or isinstance(channel, discord.VoiceChannel):
            await channel.edit(name='FUCKED BY PKW')

    # Import and set the custom server icon
    await guild.edit(icon=None)

    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            for _ in range(num_messages):
                await channel.send(f'> # FUCKED BY YOUR FAVE, PKW!\n> {msg}\n> {ping}\n> {link}')


    # Change the bot's display name
    BOTme = await guild.fetch_member(bot.user.id)
    await BOTme.edit(nick='PKW PWNS YOU! :)')


@bot.command()
async def chaos(ctx, num_messages=3, ping="@everyone", msg="OH UH!\n> LOOKS LIKE WE DID A FUCKY WUCKYYY :3\n> FUCKED BY PKW\n> WHO IS PKW?\n> PKW IS A DISCORD INDIVIDUAL THAT JUST FUCKED YOU OVER WITH SPAM! HAH!\n> DISCORD: <https://discord.gg/UTWMshSKzy>", link="https://media.discordapp.net/attachments/893961597989572621/1107759935808348301/5D931066-8E14-4CFD-84D8-FE5D851AB3F1.gif"):
    
    guild = ctx.guild

    await guild.edit(name='cHaOs CaUsEd By PkW lMfAo!1!1! :3')

    # Change text and voice channel names
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel) or isinstance(channel, discord.VoiceChannel):
            new_name = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10))
            await channel.edit(name=new_name)

    # Import and set the custom server icon
    await guild.edit(icon=None)

    # Change the bot's display name
    BOTme = await guild.fetch_member(bot.user.id)
    await BOTme.edit(nick="/*l<\/\/ 0\/\/N5 '/0l_l")

    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            for _ in range(num_messages):
                await channel.send('> # '.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10)) + f', PKW!\n> {msg}\n> {ping}\n> {link}')


@bot.command()
async def nuke(ctx, num_channels=100):
    
    guild = ctx.guild

    await guild.edit(name='cHaOs CaUsEd By PkW lMfAo!1!1! :3')

        # Import and set the custom server icon
    await guild.edit(icon=None)

    # Change the bot's display name
    BOTme = await guild.fetch_member(bot.user.id)
    await BOTme.edit(nick="/*l<\/\/ 0\/\/N5 '/0l_l")

    for guild in bot.guilds:
        for channel in guild.channels:
            await channel.delete()

        guild = ctx.guild
    for i in range(num_channels):
        channel_name = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10))
        await guild.create_text_channel(name=channel_name)

@bot.command()
async def cmds(ctx):
  if str(ctx.author.id) in owner_id:
      await ctx.send("""> # >Commands;\n> ```
                     > admin - bot owner information
                     > ping - pong!
                     > whois - information about a user you @
                     > geoloc {IP} - gives you a little information about thier geolocation (country, city etc.)
                     > ban @ - bans a user from a server you have admin permissions in
                     > kick @ - kicks a user from a server you have admin permissions in
                     > pingall - basically a shortcut for @everyone
                     > pfp @ - sends a message link of a person's profile picture
                     > prepack - sends a line of a little packing before i get onto thier ass fr fr
                     > kys - ascii image with kirby holding a sign that says 'Kys'
                     > spam - spams a message ( >spam [YOUR MESSAGE] )
                     > spamping - spams a message with a ping ( >spamping [@ person you wish to ping] [YOUR MESSAGE] )
                     > spamlink - spams a link with a ping ( >spamlink [@ person you wish to ping] [YOUR MESSAGE] [YOUR LINK] ) OR ( >spamlink [YOURLINK] OR ( >spamlink [I HAVE SET A PRESET FOR EVERY SPAM COMMAND, IF YOU DONT WISH TO TYPE A SPECIAL MESSAGE] ) )
                     > spamall - spams all discord channels within a SERVER (>spamall [@person you wish to ping] [YOUR MESSAGE] [YOUR LINK] OR JUST >spamall FOR A PRESET)
                     > gayrate - checks how gay the person you @ is!
                     > waifurate - checks how big of a waifu the person you @ is!
                     > racistrate - checks how racist the person you @ is!
                     > blackrate - check how BLACK the person you @ is!```
                     
                     
                     
                     
                     
                     
                     
                     """)
      
@bot.command()
async def gayrate(ctx, user: discord.User):
  if str(ctx.author.id) in owner_id:
   import random
   a = random.randint(1,100)
   await ctx.send(f"> # >GayRate;\n> ```{user} is {a}% gay!```")

@bot.command()
async def waifurate(ctx, user: discord.User):
  if str(ctx.author.id) in owner_id:
   import random
   a = random.randint(1,100)
   await ctx.send(f"> # >WaifuRate;\n> ```{user} is a {a}% Waifu!```")

@bot.command()
async def racistrate(ctx, user: discord.User):
  if str(ctx.author.id) in owner_id:
   import random
   a = random.randint(1,100)
   await ctx.send(f"> # >RacistRate;\n> ```{user} is a {a}% RACIST!```")

@bot.command()
async def blackrate(ctx, user: discord.User):
  if str(ctx.author.id) in owner_id:
   import random
   a = random.randint(1,100)
   await ctx.send(f"> # >BlackRate;\n> ```{user} is a {a}% BLACK!```")

@bot.command()
async def stop(ctx):
  if str(ctx.author.id) in owner_id:
      await exit()


@bot.command()
async def kys(ctx):
    if str(ctx.author.id) in owner_id:
      await ctx.send('''```\n             
                    ######((((((#((((((#(((#/.,(%###%#%##%%######%%###%%%%%%#######%%#/.*/#(#(((((((
                    #######(((((###(((#(,,#%%#######%###(**(%%#%##########%%#######%%###%#%(**((((((
                    ########(###(((#*,###%############*.#&% *#############%/**(%##%########%##%(**((
                    ############(,/%##%##%%#%%###%#%/ &@@@@,,###########%/ &@@& /%#%%#############%/
                    ######((##**####%##############..@@@@@% (##%%####%%# /@@@@@. %###############%%#
                    ########.#####%%#############/  &@@@@& .###%%%%##%( (@@@@@&  %##############%%%%
                    ######*##%####%###########%%/   %&@%. .%#########( .@@@@@&  /%##################
                    ###%,(#######%%%%%%%%##%%##/          %#%%#######   @@@@(   %#%#################
                    ###*%###########%%%%%%####%..       .%#########%*          (####################
                    %,#%%######%######%%##%%### ,*,**. *%#########%%          *%########%###########
                    ,%#######%##((((((((#%%%### ,,*, .###%%###%%%### ,,,,,,, /##%#######%###########
                    %%####%#%#%#((((((((#%%%##%,    (#%#%%%%#%%%#%## .*,,,. ####%#######%%%%####%%%%
                    %#%%##%%%%##%%#####%%%##%%##%#%#%###,..,/#%%##%%*     *%#%####%%######%#####%%%%
                    ######%%%%%%#########%############## ,.,,, %#%##%##(#%%%%%%%%#(((((((((((##%#%%#
                    #######%%%%%###%%################### ,,....%##%%%%#%%#%%%%####((((((((((((#%#%%#
                    %###################%#%######%######.,###.%#####%%#####%%########(((((((##%%%###
                    %##%#%(,.,,,,.,**/((##%%%%%%####%%#%(*##,%%%#%##%%%%##%%%###%%%%%#%##%##%%######
                    #%##%,******,,......,,,,****,,,,,,,,,..,/((###%%%%%#####%%###%##################
                    ####(*.,*****************************,.....,,,******,,,,,.,,**//(##%#%##########
                    ####%##%#.*******,,,,,*****************************,,*,,,......,*,, ############
                    %%##%%##%%*,*****,.&@*,*****************************************.*,,(%%#########
                    ##########%/*******@&,**********************************,,(%%%%%%%%#%%%#/**#####
                    ############,****,#@(*.%@&&,&@@&%,//*,,,*,************.(####################%###
                    #####%%%%#%#,****,@@@&@(,**,*(@#**,&@*,*@&/(%@#,******%##%%%%%######%%%####%####
                    %%####%%%#%(******@%,,%@*****,&@,*@&,**/@@%*.,,*****,(%#%#%%%#########%%########
                    %%%###%%##%****/&@@@#,,&@(*****@%@#,**,/,,,(@@,*****,%##%#######################
                    %%%%#####(/.************,,,***,&@*,**,(@&%#&@#,*****,#%%%#########%%#%%#########
                    ######(((,,****************((@@#,**********,********,/#########################%
                    ((((((/,,***************,*,,***********************,*/((######%################%
                    .,,,*/(((((///**,,.,,,,,*****************************.*((((#####################
                    **.,((((((((((((((/(((((((((((//*,,***,,*,,************./((((((((((######(((((((
                    ****.*((((((((((((((((((((((((((((((((((((((((((//*,,,.,..*(((((((((((((((((((((
    ```''')

@bot.event
async def on_message(message):
    if str(message.author.id) == owner_id and message.content.startswith(prefix):
        await bot.process_commands(message)

bot.run(token)