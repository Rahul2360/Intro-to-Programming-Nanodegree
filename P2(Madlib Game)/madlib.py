# Madlib Game
# The question are in this game are based on scientist or their discoveries
# Levels :- There are three levels in this game which are Easy, Medium and Hard
levels = ["easy","medium","hard"]
# This is for level selection
question = ["The full Name of einstein is _1_ Einstein. He developed the theory of _2_ .He received _3_ prize in 1921. He is best known in popular culture for its mass-equivalence formula E=_4_ . He publised more than _5_ scientific papers",
              "The full Name of Newton is Sir _1_ Newton. He developed _2_ law of motion. He is a mathematican , astronomer and _3_. He derive the _4_ law plantery motion.He also laid the foundations of classical _5_.",
              "The full name of Turing is _1_ turing. He was an English _2_ scientist. He was highly influential in the development of _3_ computer science. Turing was prosecuted in _4_ for homosexual acts.He died in _5_ ",""]
# Above are the question in our game
answers = [['albert','relativity','nobel','mc2','300'],['issac','3','physicist','kepler','mechanics'],['alan','computer','theortical','1952','1954']] # These are the answers of this above questions
# These are the answers of the questions which are declared above
#below we declare some procedure to play our games

# Below there is procedure name replace_string.In this procedure the element are replaced by the true value which are given in the answer.
def replace_string(iteration,element,question):
    question=question.replace("_"+str(element+1)+"_",answers[iteration][element])
    return question

# Below there is another procedure for processing our game. After selecting the level  this procedure  ask some question and of you are wrong then it give you
#"Wrong answer" and if you are right then it will ask you another question
def madlib_process(iteration,question):
    print question
    index=1
    max_index=6
    #index is declared because of loop .By this we can ask a limited question. In this we are asking 5 question
    while index<max_index:
        # data is storing our input of the answer
        data= raw_input("Your answer" + " "+ str(index)).lower()
        # below statement check that our answer is right or not
        if data==answers[iteration][index-1]:
            # if it is true then it call the replace_string procedure and it will replace the answer
           question = replace_string(iteration,index-1,question)
           print question
           index=index+1
            # if The answer is wrong then it print that your answer is wrong
        else:
           print "Wrong answer" +str(index)

# check_level procedure helps to deciding the levels 
def check_level(level,levels):
    length=len(levels) # this statement store the value of length of levels
    iteration=0 # this is used for checking the level
    while iteration<length:
        if levels[iteration]==level: # This statement check the level if the level is in our game then it will run
             madlib_process(iteration,question[iteration])
             iteration+=1 # it increase the value levels

# This procedure helps us to play the game or not              
def input_data():
    inputData=raw_input("Enter yes to play and no for quit the game")
    if inputData=="yes":
        play_madlib_game()
    else:
        print "Thnks for playing"

# Below is the main procedure if our game
def play_madlib_game():
    level = raw_input("Choose your level:").lower() # This statement asks the level from the user 
    check_level(level,levels) # it will go to the check_level preocedure
    input_data() # It will go to the input_data procedure
    
play_madlib_game() # By this we can able to play our game
# this calls the function play_madlib_game and then it go on further
