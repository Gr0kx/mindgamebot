import discord
from discord.ext import commands
import random

description = 'Mindgame begins'
token = "OTk2NTM0NTI1MjM0NTMyNDU0.GH4MST.0WNd9NHrp3frzRPL4temOgybMwLlFoQf5lleZ8"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

famous = ["Courage the Cowardly Lion",
          "Dr. Seuss",
          "Ebenezer Scrooge",
          "Bugs Bunny",
          "James Bond",
          "Amelia Earhart",
          "Andy Warhol ",
          "Jimmy Stewart",
          "Dr. Emmett Brown",
          "John Hancock",
          "Dennis the Menace",
          "Dumbledore",
          "Eleanor Roosevelt",
          "Sirius Black ",
          "Sean Connery",
          "Dracula",
          "Shakespeare",
          "Bruce Willis",
          "Babe Ruth",
          "James Earl Jones",
          "Buzz Lightyear",
          "Spider Man",
          "Albert Einstein",
          "Inigo Montoya",
          "Denzel Washington",
          "Jim Henson",
          "Barbie",
          "James Madison",
          "Sherlock Holmes",
          "Fozzy Bear",
          "Brad Pitt",
          "Buddy Holly",
          "Elizabeth Bennett",
          "Scooby Doo",
          "E.T.",
          "Jackson Pollock",
          "Indiana Jones",
          "Shel Silverstein",
          "Henry Ford",
          "Cap'n Crunch",
          "Dora the Explorer",
          "Abraham Lincoln",
          "Elvis Presley",
          "Stephanie Meyer",
          "Lance Armstrong",
          "Leonardo Da Vinci",
          "C-3P0",
          "Celine Dion",
          "Davy Crockett",
          "ahatma Gandhi",
          "Justin Beiber",
          "Anakin Skywalker",
          "Eli Whitney",
          "Audrey Hepburn",
          "Isaac Newton",
          "Robin Hood",
          "Rocky",
          "Frankenstein",
          "Beethoven",
          "Pocahontas",
          "Celebrities",
          "Kevin Bacon",
          "John Williams",
          "Louis Armstrong",
          "Hannah Montana",
          "David Beckham",
          "Helen Keller",
          "Lucille Ball",
          "Sacajawea",
          "Benjamin Franklin",
          "Captain Kirk",
          "Billy the Kid",
          "Franklin D. Roosevelt",
          "Mario",
          "Han Solo",
          "Mark Twain",
          "C. S. Lewis",
          "Salvador Dali",
          "Captain Hook",
          "Rapunzel",
          "Charles Dickens",
          "Luke Skywalker",
          "Harry Houdini",
          "Santa Claus",
          "Harrison Ford",
          "Batman",
          "George Lucas",
          "Darth Vader",
          "Mufasa",
          "Oprah Winfrey",
          "Garfield",
          "Genghis Khan",
          "Gilligan",
          "Michael Phelps",
          "Michelangelo",
          "Charles Darwin",
          "Betsy Ross",
          "Bill Gates",
          "Walt Disney",
          "Harry Potter",
          "Marty McFly",
          "Hamlet",
          "Mother Teresa",
          "Cleopatra",
          "Mr. Darcy",
          "Clark Kent",
          "Grace Kelly",
          "Thomas Edison",
          "Tony Hawk",
          "Neil Armstrong",
          "Bill Cosby",
          "George Washington",
          "Cinderella",
          "Willy Wonka",
          "Mary Poppins",
          "Peter Pan",
          "Frodo",
          "Neil Diamond",
          "George of the Jungle",
          "Mr. Rogers",
          "Pablo Piccaso",
          "Voldermort",
          "Winnie the Pooh",
          "Christopher Columbus",
          ]


@bot.event
async def on_ready():
    print("ready")


@bot.command()
async def mindgame(ctx, target):
    word1 = random.choice(famous)
    word2 = random.choice(famous)
    await ctx.send(f"Let the mindgame begin"
                   f"\nHeres the hardest part"
                   f"\nREMEMBER TO LOOK AT YOUR PARTNERS WORD AND NOT YOUR OWN!"
                   f"\nIf you break the mind with this rule feel free to play again 🤯"
                   f"\n{ctx.author.mention} This name is magically appearing above your head <||{word1}||>"
                   f"\n{target} This name is magically appearing above your head <||{word2}||>")

bot.run(token)
