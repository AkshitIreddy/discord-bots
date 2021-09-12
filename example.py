#Few things to note
#this bot will only read and send messages
#to avoid spamming the bot will reply to commands that start with '.'


import discord
import requests
from emoji import emojize


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

#MAKE SURE TO ARRANGE EVERYTHING PROPERLY WHEN YOU ARE FREE.
#The main part of the program
@client.event
async def on_message(message):
  
    #This will generate a list of things it can do when user says .help
    elif ".help" == message.content.lower():
        await message.channel.send(f"""Hello {message.author.name} . I can do the the following tasks:"""
+ '\n'+emojize(':point_right:')+"To see the 2021 cutoffs for MIT Banglore type '.cutoff'"
+ '\n'+emojize(':point_right:')+"To see the course overview and syllabus for any branch in MIT Banglore type '.syllabus'"
+ '\n'+emojize(':point_right:')+"To see the Btech 2021 Counselling Schedule type '.schedule'"
+ '\n'+emojize(':point_right:')+"If you want to know about famous tourist attractions near MIT Banglore type '.tourist' " 
+ '\n'+emojize(':point_right:')+"To find out where MIT Banglore is located type '.location' ")

        
    #This will generate the latest cutoff information when user says .cutoff
    elif ".cutoff" == message.content.lower():
        await message.channel.send(f"{message.author.name}, the 2021 cutoffs are: "
+ '\n'+emojize(':point_right:')+"The round 4 cutoff for Computer Science is 4829"
+ '\n'+emojize(':point_right:')+"The round 4 cutoff for Computer Science & Artifical Intelligence is 6801"
+ '\n'+emojize(':point_right:')+"The round 4 cutoff for Computer Science & Cyber Security is 11499"
+ '\n'+emojize(':point_right:')+"The round 4 cutoff for Information Technology is 12447"
+ '\n'+emojize(':point_right:')+"The round 4 cutoff for Electronics and Communication is 20961")


     #This will generate the syllabus information when user says .syllabus
    elif ".syllabus" == message.content.lower():
        await message.channel.send(f"{message.author.name} select which branch's overview and syllabus you would want to see."
+ '\n'+emojize(':point_right:')+"Type 'cse.syllabus' for Computer Science & Engineering"
+ '\n'+emojize(':point_right:')+"Type 'ai.syllabus' for Computer Science & Engineering - Artificial Intelligence"
+ '\n'+emojize(':point_right:')+"Type 'cyber.syllabus' for Computer Science & Engineering - Cyber Security"
+ '\n'+emojize(':point_right:')+"Type 'it.syllabus' for Information Technology"
+ '\n'+emojize(':point_right:')+"Type 'ece.syllabus' for Electronics and Communication Engineering")

    elif "cse.syllabus" == message.content.lower():
        embed = discord.Embed()
        embed.description = "[Click here for an overview of Computer Science & Engineering along with SYLLABUS PDF](https://manipal.edu/mitblr/program-list/btech/btech-computer-science-engineering.html)"
        await message.channel.send(embed=embed)

    elif "ai.syllabus" == message.content.lower():
        embed = discord.Embed()
        embed.description = "[Click here for an overview of Computer Science & Engineering - Artificial Intelligence along with SYLLABUS PDF](https://manipal.edu/mitblr/program-list/btech/BTech-Computer-Science-and-Engineering-Artificial-Intelligence-and-Machine-Learning.html)"
        await message.channel.send(embed=embed)


    elif "cyber.syllabus" == message.content.lower():
        embed = discord.Embed()
        embed.description = "[Click here for an overview of Computer Science & Engineering - Cyber Security along with SYLLABUS PDF](https://manipal.edu/mitblr/program-list/btech/btech-computer-science-cyber-security.html)"
        await message.channel.send(embed=embed)
        

    elif "ece.syllabus" == message.content.lower():
        embed = discord.Embed()
        embed.description = "[Click here for an overview of Electronics and Communication Engineering along with SYLLABUS PDF](https://manipal.edu/mitblr/program-list/btech/btech-electronics-and-communication-engineering.html)"
        await message.channel.send(embed=embed)

    elif "it.syllabus" == message.content.lower():
        embed = discord.Embed()
        embed.description = "[Click here for an overview of Information Technology along with SYLLABUS PDF](https://manipal.edu/mitblr/program-list/btech/btech-information-technology.html)"
        await message.channel.send(embed=embed)

    #this will give schedule info 
    elif ".schedule" == message.content.lower():
        embed = discord.Embed()
        embed.description = "[Click here to view the Btech 2021 Common Counselling Schedule](https://counseling.manipal.edu/files/2021_Online_BTech_Common_Counseling_Schedule.pdf)"
        await message.channel.send(embed=embed)

    #this gives some info related to tourist spots
    elif ".tourist" == message.content.lower():
        await message.channel.send(f"{message.author.name}, these are a few Tourist attraction near MIT Banglore :"
+ '\n'+emojize(':ocean:')+"Yelahanka Kere : It is one of the largest lakes in the Bangalore North zone. It has two inlets, one outlet, a wet land and an island. Its upstream is linked to lakes like the Puttenahalli and Herohalli while in its downstream, we find the Jakkur lake. It is situated in the Nagawara Hebbal Valley."
+ '\n'+emojize(':hibiscus:')+ "Cubbon Park(from MIT Bangalore 21km) : Spread over an area of 300 acres, Cubbon Park in the city of Bangalore is a major sightseeing attraction rich in green foliage. It is a green belt region of the city and is an ideal place for nature lovers and those seeking a calm atmosphere. Having been laid down by Lord Cubbon, the park is named so in his honour."
+ '\n'+emojize(':rose:')+ "Lalbagh Botanical Garden( from MIT Bangalore 24 km ) : Lalbagh Botanical Garden or shortened Lalbagh, is an old botanical garden in Bengaluru, India."
+ '\n'+emojize(':european_post_office:')+"Bangalore Palace(from MIT Bangalore 20km)) : Bangalore Palace is a royal palace located in Bangalore, Karnataka, India, in an area that was owned by Rev. J. Garrett, the first principal of the Central High School in Bangalore, now famous as Central College. The commencement of the construction of the palace is attributed to him."
 + '\n'+emojize(':small_blue_diamond:')+"ISKCON Temple(from MIT Banglore 23 km) : Sri Radha Krishna-chandra Temple is one of the largest Krishna Hindu temples in the world, affiliated with ISKCON Revival Movement. It is located at Rajajinagar, in North Bangalore in the Indian State of Karnataka."
 + '\n'+emojize(':small_red_triangle:')+" Tipu Sultan's Summer Palace(from MIT Bangalore 25 km) : Tipu Sultan's Summer Palace, in Bangalore, India, is an example of Indo-Islamic architecture and was the summer residence of the Mysorean ruler Tipu Sultan. "                                   
+ '\n'+emojize(':hotel:')+ "Royal Orchid Resort & Convention Centre(from MIT Bangalore 11 km) : Located close to Manyata Tech Park and the Bangalore Airport is the Royal Orchid Resort & Convention Centre. It is spread over 8-acres of green area")

    # this gives location
    elif ".location" == message.content.lower():
        await message.channel.send("The address of MIT Banglore is '4HHR+J2V, BSF Campus, Yelahanka, Govindapura, Karnataka 560064'.")
        embed = discord.Embed()
        embed.description = "[Click here to view the location of MIT Banglore on Google Maps](https://www.google.com/search?q=manipal%20university%20yelahanka&rlz=1C1RXQR_enIN944IN944&oq=manipal+university+yelahanka&aqs=chrome..69i57.10876j0j7&sourceid=chrome&ie=UTF-8&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&rflfq=1&num=10&rldimm=2127589341413396161&lqi=ChxtYW5pcGFsIHVuaXZlcnNpdHkgeWVsYWhhbmthSO666q7NrYCACFooEAAQARgAGAEYAiIcbWFuaXBhbCB1bml2ZXJzaXR5IHllbGFoYW5rYZIBCnVuaXZlcnNpdHmqARoQASoWIhJtYW5pcGFsIHVuaXZlcnNpdHkoAA&ved=2ahUKEwi_9MSGl_byAhVTRkEAHeQjDCkQvS56BAgGEC4&rlst=f#rlfi=hd:;si:2127589341413396161,l,ChxtYW5pcGFsIHVuaXZlcnNpdHkgeWVsYWhhbmthSO666q7NrYCACFooEAAQARgAGAEYAiIcbWFuaXBhbCB1bml2ZXJzaXR5IHllbGFoYW5rYZIBCnVuaXZlcnNpdHmqARoQASoWIhJtYW5pcGFsIHVuaXZlcnNpdHkoAA;mv:[[13.1445332,77.678223],[12.856797499999999,77.5425295]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2)"
        await message.channel.send(embed=embed)
        
client.run(token)
