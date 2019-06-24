# Chat Bot Version 0.4.py
# A bot that can talk and do fun stuff.
# June 7th, 2019, Jason Down
# Declare variables, create tables, functions and import modules, basically prepare the bot.

import random

version = "0.4" #The version of the bot, I can change this value as I update it.

bot_greetings = ["Hello!","Hey!","Howdy!","Sup.","Ayo!"] #Ways of saying hello, used in the beginning mostly but might be called in certain circumstances.

answer_yes = ["yes", "y", "yup", "uh huh", "yep", "sure", "alright", "of course", "sounds good",] # a small list of ways of saying yes, can be used in yes/no questions.

answer_no = ["no", "nah", "nope", "nuh uh", "n"] # the same for the list of ways of saying yes.

first_hello = "True" # A variable that will allow the bot to know if it is saying hello for the first time, this will mean it will introduce itself and not when the user says hello again.

user_name = "" # The users name, it starts empty and will be asked if the bot introduces itself

tell_name = ["can i tell you my name", "do you want to know my name", "i will tell you my name", "want my name", "do you want my name", "can i tell you my name", "can i say my name", "want to know my name", "i can give my name"] # A table of questions for asking the bot if they want to tell their name.

empty_text = "" # A variable full of empty text, used in if statements if the bot wants to detect if the user hasnt inputted anything as putting a "" string gives a syntax error and also makes code easier to read.

def ask_name():   # A function for asking the users name, cleaning any un needed characters & storing it in a variable.
    global user_name
    print("What can I call you?")
    while True:
        user_name = str(input("Please enter your name: "))
        user_name = user_name.strip()
        user_name = user_name.lower()
        user_name = user_name.strip('"[]\/!@#$%^&*() -=+_<>,.?|{}')
        user_name = user_name.capitalize()
        if user_name == empty_text:
            print("I cant read that! Enter something!")
        else:
            break

def random_hello():
    print(random.choice(bot_greetings))
    
def bot_introduction(): # A function for when the bot introduces itself, will ask for the name and say hello.
    global first_hello
    random_hello()
    print("I am Pickle Chin Ahh Bot version {}!" .format(version))
    if user_name == "":
        ask_name()
        print(random.choice(bot_greetings) , "{}! Thats an interesting name." .format(user_name)) # Will say a random greeting, followed by the users name e.g Hey! Jason!
    else:
        print(random.choice(bot_greetings) , "{}! I belive you have said your name before." .format(user_name))
    first_hello = "False" # Lets the bot know that the user has introduced itself by making this variable false, if the user says hello to the bot it wont keep introducing itself.

user_greetings = ["hey", "hello", "hi", "sup", "greetings", "yo", "howdy", "hiya", "gday", "ayo", "heyo"] # Ways the user can greet the bot, it uses less formal ways that
# the user is more likely to use?

user_input = "" # Defining the user input variable, it is empty at the moment so that it doesnt trigger anything.

clean_user_input = "" # The user input when it has had punctuation and capital letters removed, empty so that it doesnt trigger anything.

def text_simplify(): # The function removes capital letters, removes spaces and then removes the puncuation from the list.
    global user_input
    global clean_user_input
    clean_user_input = user_input.strip()
    clean_user_input = clean_user_input.lower()
    clean_user_input = clean_user_input.strip('[]\"/!@#$%^&*()-=+_<>, .?|{}')
            
# Will say a random fact from the table, since the facts dont have individual
# responses we can control that within an if statement.

def random_fact():
    print(random.choice(facts))


# Will output a giant smiley face, the user will need to be in full screen for it to work properly.

ask_smile = ["smile", "make a happy face", "happy", "smiley face", "happy face"] # A table of ways the user can ask for a smiley face.
def smile_face():
    print("""\

                        *****************
                   ******               ******
               ****                           ****
            ****                                 ***
          ***                                       ***
         **           ***               ***           **
       **           *******           *******          ***
      **            *******           *******            **
     **             *******           *******             **
     **               ***               ***               **
    **                                                     **
    **       *                                     *       **
    **      **                                     **      **
     **   ****                                     ****   **
     **      **                                   **      **
      **       ***                             ***       **
       ***       ****                       ****       ***
         **         ******             ******         **
          ***            ***************            ***
            ****                                 ****
               ****                           ****
                   ******               ******
                        *****************
                        
    """)

facts = ["In Switzerland it is illegal to own just one guinea pig.",
         "Pteronophobia is the fear of being tickled by feathers.",
         "Snakes can help predict earthquakes.",
         "A flock of crows is known as a murder.",
         "So far, two diseases have successfully been eradicated: smallpox and rinderpest.",
         "Cherophobia is an irrational fear of fun or happiness.",
         "7% of American adults believe that chocolate milk comes from brown cows."
         "If you lift a kangaroo’s tail off the ground it can’t hop.",
         "Bananas are curved because they grow towards the sun.",
         "Billy goats urinate on their own heads to smell more attractive to females.",
         "The inventor of the Frisbee was cremated and made into a Frisbee after he died.",
         "During your lifetime, you will produce enough saliva to fill two swimming pools.",
         "If Pinocchio says “My Nose Will Grow Now”, it would cause a paradox.",
         "An eagle can kill a young deer and fly away with it",
         "In 2017 more people were killed from injuries caused by taking a selfie than by shark attacks.",
         "There is a species of spider called the Hobo Spider.",
         "A lion’s roar can be heard from 5 miles away.",
         "A baby spider is called a spiderling.",
         "The following can be read forward and backwards: Do geese see God?",
         "In Uganda, around 48% of the population is under 15 years of age.",
         "In the 16th Century, Arab women could initiate a divorce if their husbands didn’t pour coffee for them.",
         "Recycling one glass jar saves enough energy to watch television for 3 hours.",
         "Approximately 10-20% of U.S. power outages are caused by squirrels.",
         "A small child could swim through the veins of a blue whale.",
         "Bin Laden’s death was announced on 1st May 2011. Hitler’s death was announced on 1st May 1945.",
         "A woman once tried to commit suicide by jumping off the Empire State Building. She jumped from the 86th floor but was blown back onto the 85th floor by a gust of wind.",
         "The Twitter bird actually has a name – Larry.",
         "Octopuses have four pairs of arms.",
         "It snowed in the Sahara desert for 30 minutes on the 18th February 1979.",
         "Birds don’t urinate.",
         "The 20th of March is Snowman Burning Day.",
         "An apple, potato, and onion all taste the same if you eat them with your nose plugged.",
         "Nutella was invented during WWII, when hazelnuts were mixed into chocolate to extend chocolate rations.",
         "In 2011, more than 1 in 3 divorce filings in the U.S. contained the word “Facebook.”",
         "Tears contain a natural pain killer which reduces pain and improves your mood.",
         "Millions of birds a year die from smashing into windows in the U.S. alone.",
         "In total, there are 205 bones in the skeleton of a horse.",
         "In 1998, Sony accidentally sold 700,000 camcorders that had the technology to see through people’s clothes.",
         "You can fire a gun in space.",
         ]
# A long table of facts used to keep the user hooked or interested in the conversation.


question_name = ["whats my name", "my name", "what do you call me", "what do you refer to me as", "what should you call me"] # A table for ways the user can ask for their name.

bot_confused = ["Uhh.. repeat that?", "I don't know what that means!", "What?", "Ay?", "Come again?", "Excuse me?", "What did you say?", "Huh?"] # Some words the bot can use if the user inputs something it cant understand.
         


print("Welcome to the PICKLE CHINNN AHH BOT version {} !".format(version))#Startup message,
#says the name of the bot and the version, will show when everything is prepared.

while True: # Put the user input inside a loop so that if something is typed wrong or the user needs to input again.
    user_input = str(input("what would you like to say to me?: ")) # This is the input that will be used to communicate with the bot from now on.
    
    text_simplify() # Clean the input of capital letters, spaces and punctuation so that text can be read easier.

    # Let the list of if statements begin!

    if clean_user_input in user_greetings: # If the user has put something from a table of expected greetings, run the next code.
        if first_hello == "True":  # If the user has not said hello to the bot before, it will introduce itself and ask for the users name etc.
            bot_introduction()
        else:
            random_hello()  # Otherwise the bot will respond with a random hello from a list.

    elif clean_user_input in question_name: # If the user hasn't triggered the if statement above and the user asks what their name is the bot will run the following code.
        if user_name == "": # If the username is empty as the user hasnt given a name before, the bot will inform the user that they dont know their name and run the following code in order to obatin it.
            print("You havent told me your name...")
            print("Do you want me to ask your name?")
            user_input = str(input("Please enter an answer, Y/N: "))  # A yes or no question on wether the user would like to give their name or not.
            if user_input in answer_yes: # decides if the user has said yes or no by comparing their input to 2 tables of various ways of saying yes & no.
                ask_name()  # If the user says yes they will input their name and have it printed to them,
                print("Your name is {}!" .format(user_name))
            elif user_input in answer_no: # If they say no however, they will end this interaction.
                print("Very well.")
        else:
            print("Your name is {}!" .format(user_name)) # This links to the first if statement that checks if they have a name, this will say their name if the name variable isnt empty.


    elif clean_user_input in tell_name:  # If the user has asked to tell the bot their name, execute the following code.
        if user_name is not "": # If the user actually has a name it will execute the following code
            print("But your name is {}, want to change your name anyway?" .format(user_name))  # Says the users current name and asks if they want to change it followed by boolean question
            user_input = str(input("Want to change your name? Y/N: "))  # Yes or No for if the user wants to change their name
            while True:
                if user_input in answer_yes:  # Following code if user wants to change name
                    ask_name()
                    print("{} {}, Thats a cool name!" .format(random.choice(bot_greetings), user_name))
                    break
                elif user_input in answer_no: # Following code if user doesnt.
                    print("Very well.")
                    break
                else:
                    print(random.choice(bot_confused))
                    user_input = str(input("I dont know what that means.. Still want to change your name? Y/N: "))  # If the user says something differnt other than yes or no the bot will tell the user and allow them to enter another answer
        else:
            ask_name()
            print("{} {}, Thats a cool name!" .format(random.choice(bot_greetings), user_name))

    elif clean_user_input in ask_smile:
        smile_face()
                                     
        

    else:  # This will trigger if any of the if statements above arent triggered by the users input, in most cases this is because the user has inputted something the bot doesn't recognize.
        print(random.choice(bot_confused))
        print("Want to know something interesting?")
        random_fact() # Will say a random fact to keep the conversation going.

            
        
        
    



