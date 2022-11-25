# Import pycord to acces the discord api
import discord
from discord import option
from discord.ui import Select, View

# Import the ShortAPI class from the duolingo.py file
from src.duolingo import ShortAPI
from src.utils import name_to_code, code_to_name, emoji

# Import the os module to access the environment variables
import os

# Import the dotenv module to access the .env file
from dotenv import load_dotenv
load_dotenv()

# Get the discord info from the .env file
TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG_GUILD = os.getenv('DEBUG_GUILD')

# Set "bot" to the discord client
bot = discord.Bot(debug_guilds=[DEBUG_GUILD])
bot_version = "1.0"

# '''Interaction classes'''
# The interaction class for the /course command
# class SelectCourse(discord.ui.View, username=None):
#     @discord.ui.select( # the decorator that lets you specify the properties of the select menu
#         placeholder = "Select a course to see more information about it", # the placeholder text that will be displayed if nothing is selected
#         min_values = 1, # the minimum number of values that must be selected by the users
#         max_values = 1, # the maximum number of values that can be selected by the users
#         options = []
#         for course in ShortAPI("").get_courses():
            
#     )
#     async def select_callback(self, select, interaction): # the function called when the user is done selecting options
#         await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")

# When the bot is ready, print a message to the console, count the guilds and print the number of guilds
@bot.event
async def on_ready():
	print('We have logged in as {0.user} v{1}'.format(bot, bot_version))
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("DuoBot is in " + str(guild_count) + " guilds.")

@bot.slash_command(name='duoprofile', description='Show the duolingo profile of the specified username')
@option("username", description="The username of the user you want to get the profile of")
async def duoprofile(ctx, username: str):
    sapi = ShortAPI(username)
    embed=discord.Embed(title=f"{username}'s profile", description="", color=0x58cc02)
    embed.add_field(name="Current streak", value=f"<:streak:1045256936150544404> {sapi.streak()}")
    embed.add_field(name="Total crowns", value=f"<:duocrown:1045256934758039623> {sapi.total_crowns()}")
    embed.add_field(name="Total XP", value=f"{sapi.total_xp():,}".replace(',', ' '))
    embed.add_field(name="Full name", value=f"{sapi.name()}")
    embed.add_field(name="Has Plus", value="{0}".format(":x:" if sapi.has_plus() == False else ":white_check_mark:"))
    embed.add_field(name="Profile country", value=f":flag_{(sapi.profile_country()).lower()}:")
    embed.add_field(name="Active course", value=f"{sapi.activecourse.title()} from {code_to_name(sapi.activecourse.from_language())}")
    embed.add_field(name="Profile link", value=f"https://www.duolingo.com/profile/{username}")
    embed.set_footer(text="This bot is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Duolingo, or any of its subsidiaries or its affiliates. The name Duolingo as well as related names, marks, emblems and images are registered trademarks of their respective owners.")
    await ctx.respond(embed=embed)

@bot.slash_command(name='course', description='Show the information of a specified course of a user')
@option("username", description="The username of the user you want to see the course of")
async def course(ctx, username: str):
    sapi = ShortAPI(username)
    optionlist = []
    optionlist2 = []
    i=0
    for course in sapi.courses.list_raw():
        if i > 24:
            optionlist2.append(discord.SelectOption(label=f"{course['title']} (from {code_to_name(course['fromLanguage'])})", description=f"Show info on the {course['title']} from {code_to_name(course['fromLanguage'])} course",value=str(i), emoji=emoji(course['learningLanguage'])))
        else:
            optionlist.append(discord.SelectOption(label=f"{course['title']} (from {code_to_name(course['fromLanguage'])})", description=f"Show info on the {course['title']} from {code_to_name(course['fromLanguage'])} course",value=str(i), emoji=emoji(course['learningLanguage'])))
        i+=1

    select = Select(options=optionlist)

    view = View()
    view.add_item(select)
    if i > 24:
        select2 = Select(options=optionlist2)
        view.add_item(select2)

    async def show_course(interaction):
        if int(interaction.data['values'][0]) > 24:
            course = sapi.courses.list_raw()[int(interaction.data['values'][0])]
        else:
            course = sapi.courses.list_raw()[int(interaction.data['values'][0])]
        # print(interaction.data['values'][0])
        await interaction.response.send_message(f"Awesome! You selected {course['title']} which has {course['crowns']} crowns and {course['xp']} XP")
    select.callback = show_course
    select2.callback = show_course
    
    await ctx.respond("Select a course to see more information about it", view=view)


bot.run(TOKEN)