#this bot will only read and send messages


#if you have already pip installed discord then you can import discord.
import discord

#if you remember in step 6.5 in readme i told you to save the bot's token now you can add the token here like this for example token = "Thetokenyoucopied". 
#one thing to note is dont forget to enclose your token in single/double quotes

token = 

#BEFORE RUNNING THIS PROGRAM ADD A TOKEN ABOVE

#Client intialised

client = discord.Client()

#this tells us whether our bot has been intialized or not
@client.event 
async def on_ready():  
    print(f'We have logged in as {client.user}')


#this records the messages of each user and the messsages that they send
@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")


########################## MAIN MAIN MAIN ################################################# 
#The main part of the program
@client.event
async def on_message(message):
    #This will generate a message when user says some command word. You can add whatever you want. for now i will choose 'hi'
    if "hi" == message.content.lower():
        #This will send a message if user says hi. you can change the message to whatever you like just make sure it is under single quotes or double quotes
        await message.channel.send("HI I,m a discord chatbot")
    #This will send a message if user says bye. you can change the message to whatever you like just make sure it is under single quotes or double quotes
    elif "bye" == message.content.lower():
        #you can say bye by using the name of the person who said bye using this '{message.author.name}' just make sure that you put an 'f' before the single/double quote
        await message.channel.send(f"Bye see you soon {message.author.name} " 
    #similarly you add more commands just add more elif statements like below 
    elif "somecommand" == message.content.lower():
        await message.channel.send("Some message")
 
#the below statement will be responsible for running our bot. to run the bot if you are on python idle click on run and then click on  run again.your bot will be running now so go ahead try using you commands with your bot.                                  
client.run(token)
                                   
                                   
                                   
#if you want to see an actual application on a discord bot see example.py in the my github repository from where you downloaded beginner.py it contains an example of a bot that
# provides information regarding cutoff and syllabus and information regarding Manipal University Bangalore. 
        

