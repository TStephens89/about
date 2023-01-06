import logging
 
# Create and configure logger
logging.basicConfig(filename="freemium.log", level=logging.DEBUG)
 




# class Character:
#   def __init__(self, name, age, moves):
#     self.name = name
#     self.age = age
#     self.moves = moves
#   def chances(self, moves):
#     if moves <= 0:
#       print("You need more moves to continue. Would you like to watch an ad for more moves?")
#       logging.info("Opportunity to get more lives from ads")
photoshop=""

def Start():
  characters = ["green","orange","red"]
  logging.info("Started freemium quest")
  print("Ok " + name + " You have entered the school what will you do?")
  userInput = ""
  while userInput not in characters:
    print("Who will you ask for help: green/orange/red/violet")
    userInput = input()
    if userInput == "green":
      greenHelp()
    elif userInput == "orange":
      orangeHelp()
    elif userInput == "red":
      redHelp()
    elif userInput == "violet":
      print("violet leads you outside where you notice this can't be the right direction.")
      logging.info("Foolishly asked violet for help")
    else: 
      print("You have to ask one of the guys to get to class.")
      logging.info("You made a selection that was not recognized")
def greenHelp():
  characters = ["orange","red"]
  print("I wish I had time to take you but I think orange is heading that way")
  logging.info("You asked green for help")
  userInput = ""
  while userInput not in characters:
    print("Options: orange/violet/back")
    userInput = input()
    if userInput == "orange":
      greensLie()
    elif userInput == "violet":
      print("maybe you should try asking red")
      logging.info("violet did not help you")
    elif userInput == "back":
      Start()
      logging.info("the player went back")
    else:
      print("You have to ask one of the guys to get to class.")
      logging.info("user made incorrect input")
def greensLie():
  characters = ["pay","ad"]
  print("before making it to orange you run into violet")
  print("violet: dude, you actually listened to green he is not trustworthy, I can help you if you watch an ad or pay for premium version")
  logging.info("the user tried to listen to green but ran into violet")
  userInput = ""
  while userInput not in characters:
    print("What will you do?: pay/ad")
    userInput = input()
    if userInput == "pay":
      print("You honestly paid to win this game?")
      print("you made it to class but you paid for a freemium game so did you really win?")
      logging.info("the user paid to win")
      quit()
    elif userInput == "ad":
      print("You wasted 30 seconds on a ad")
      print("Atleast you did not pay for this freemium game")
      logging.info("the user decided to watch an ad to complete the game")
      quit()
    else:
      print("You have to ask one of the guys to get to class.")
      logging.info("user chose an option that is not available")
def redHelp():
  characters = ["right","help","back"]
  print("I can help you but you have to help with my dad, he just needs tree fitty?")
  userInput = ""
  while userInput not in characters:
    print("Options: ignore/help/back")
    userInput = input()
    if userInput == "ignore":
      print("red: Wow, your choice has killed orange. We dont want to help you anymore")
      logging.info("User did not help and indirectly killed orange you have lost the game")
      print("YOU LOSE!!!")
      quit()
    elif userInput == "help":
      print("After paying tree fitty you notice red's dad is a giant crustacean from the paleolithic era ")
      print("Loch Ness Monster: You were tricked into paying tree fitty to make it to home room hope this was fun for you")
      logging.info("you won but only because you paid tree fitty")
      quit()
    elif userInput == "back":
      print("you have already been here")
      logging.info("the user went back")
      Start()
    else:
      print("Follow the prompts!")
      logging.info("user did not pick a valid response")
def orangeHelp():
  characters = ["back","follow","ignore"]
  global photoshop
  print("**in a muffled voice**")
  print("orange: follow me but stay close I know from experience this place is dangerous")
  logging.info("You asked for oranges help")
  userInput = ""
  while userInput not in characters:
    print("Options: ignore/back/follow")
    userInput = input()
    print("You should've followed the prompt try again")
    if userInput == "ignore":
      print("You run into a famous celebrity who is a hobbit")
      print("Celebrity: I think it is great you put in hard work like me! maybe following orange will help you")
      print("As the mysterious celbrity turns around she drops the power of P.C.ness")
      logging.info("the user ignored and ran into a celebrity **who is a hobbit** and acquired the power of P.C.ness")
      photoshop = True
    elif userInput == "back":
      logging.info("the user went back")
      Start()
    elif userInput == "follow":
      orangePath()
    else:
      print("You have to follow the prompts")
      logging.info("the user didnt follow the prompt")
def orangePath():
  actions = ["fight","run"]
  global photoshop
  print("orange Leads you down the hallway where you are met by an Artist a reformed lover of fish sticks")
  print("Artist: I think you took something from my wife I want it back or I am going to lose it ")
  logging.info("you took oranges path and ran into an Artist a reformed lover of fish sticks")
  userInput = ""
  while userInput not in actions:
    print("What will you do: run/fight")
    userInput = input()
    if userInput == "fight":
      if photoshop:
        print("You have defeated an Artist and saved the people from his tweets but you never made it to class")
        print("You did not make it to class but the Artist is banned from social media")
        logging.info("you defeated the Artist and he is now banned from social media but you did notm ake it to class")
        quit()
      else:
        print("orange was killed by a reformed fish stick lover and you missed class")
        logging.info("the user fought the Artist but lost because they did not have P.C.ness")
      quit()
    elif userInput == "run":
      print("violet's voice echoes: wow what a coward!")
      logging.info("the user ran from a fight")
      orangeHelp()
    else:
      print("No silly TRY AGAIN")

if __name__ == "__main__":
  while True:
    print("Welcome to the Freemium terminal game!")
    print("You are new to school and need to make it to class")
    print("You might encounter many unexpected obstacles on this path")
    print("Will you make it to class before the bell rings?")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    
    Start()

