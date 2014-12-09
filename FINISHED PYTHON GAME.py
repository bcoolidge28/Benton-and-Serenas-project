#project

#project opener
print 'It was long ago, precisely 45 A.D. King Certifacato sends a knight to go get you. This is where you come in. By the way what is your name?'
print ' '
userInput = raw_input()
print 'Knight: Have you seen a youg man named ' + str(userInput)
print ' '
print str(userInput) + ': That is me'
print ' '
print 'Knight: Oh... Then come with me King Certifacato needs you.'
print ' '
#Going to see the king

print '(You go with the knight to see the king)'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print '(The king sees you walk in and sends his servants that are surrounding him away.)'
print 'King Certifacato: You must be ' + str(userInput)
print ' '
print str(userInput) + ': Yes that`s me your majesty. Why did you need me?'
print ' '
print 'King Certifacato: Did you know your granfather ' + str(userInput)   
print ' '
 
userAnswer1 = raw_input()
if userAnswer1 == str('yes'):
    print 'King Certifacato: Then you knew that your grandfather was a great knight.'
    print ' '
    print str(userInput) + ': Yes, and what does that have to do with me?'
    print ' '
elif userAnswer1 == str('no'):
    print 'King Certifacato: Ok well your grandfather was the greastest knight that has ever fought for this kingdom.'
    print ' ' 
    print str(userInput) + ': Ok why did I need to know that.'
    print ' '

print 'King Certifacato: Well since he was a great knight I figured that you would be to. So I am offering you a chance to become rich.'
print ' '
print str(userInput) + ': Well what is it that I must do to become rich.'
print ' '
print 'King Certifacato: My crown was stolen and I need you to go to the Dark Forest and get it back from Trolly The Terrible.'
print ' '
print str(userInput) + ': Trolly The Terrible! Sorry your majesty but I can`t do it.'
print ' '
print 'King Certifacato: If you do it and bring it back to me then I will pay you 5,000,000 gold pieces.'
print ' '
print str(userInput) + ': Well I do need the money badly so...fine i`ll do it.'
print ' '
print 'King Certifacato: Great, my best knight Sir Buttocks will teach you how to fight.'
print ' '
print '(You go out with Sir Buttocks to the training fields.)'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
#learning how to fight with Sir Buttocks
import random

damageBySquirrel = random.randint(10,20)
damageBySlime = random.randint(12,22)
damageByBear =  random.randint(20,27)
damageByTrollyTheTerrible = random.randint(30,40)
damageByWizard = random.randint(22,28)

playerHealth = 100#
playerHealth2 = 100#
playerHealth3 = 100#
playerHealth4 = 100#
playerHealth5 = 100#
squirrelHealth = 100#
slimeHealth = 100#
trollytheterribleHealth = 100#
bearHealth = 100
wizardHealth = 100
watermelonHealth = 1
punchDmg = random.randint(1,5)
swordDmg = random.randint(15,20)
maceDmg = random.randint(20,35)
lightningspellDmg = random.randint(1,40) 

print 'Sir Buttocks: Okay when fighting you have 3 different attacks, a punch, a sword stab, and a mace hit. The punch is the weakest attack, the sword stab has meduim damage, and the mace has the highest damage. To attack all you have to do is hit 1,2,3. 1 is a punch, 2 is a sword stab, and 3 is a mace hit.'
print ' '
print str(userInput) + ": Okay is there anything that I can practice on?"
print ' '
print 'Sir Buttocks: Oh yeah (grabs a watermelon and puts it on a table). Smash that watermelon.'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
keepGoing = True

while (playerHealth > 0 and watermelonHealth > 0):
    print "Choose an action. 1 will punch, 2 will use the sword, and 3 will use the mace."
    userInput2 = int(raw_input())
    if userInput2 == 1:
        print "You punch the watermelon."
        watermelonHealth = int(watermelonHealth) - punchDmg
    if userInput2 == 2:
        print "You stab the watermelon."
        watermelonHealth = int(watermelonHealth) - swordDmg
    if userInput2 == 3:
        print "You hit the watermelon with your mace."
        watermelonHealth = int(watermelonHealth) - maceDmg

print "Sir Buttocks: You smashed a watermelon now go and get the kings crown back from real monsters that can fight back."
print ' '
print str(userInput) + ': Great.'
print ' '
print '(You put on armour and set out for the dark forest)'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print '(You stand outside the Dark Forest and see a sign that says KEEP OUT,DO NOT ENTER)'
print str(userInput) + ': Well that`s not a good sign.'
print ' '
print '(You enter The Dark Foret)'
print ' '
print '(About an our after entering he Dark Forest a giant man eating squirrel bursts out of the bushes)'
print str(userInput) + ': Wow!'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
  
#first fight
while (playerHealth > 0 and squirrelHealth > 0):
    print "Choose an action. 1 will punch, 2 will use the sword, and 3 will use the mace."
    userInput2 = int(raw_input())
    if userInput2 == 1:
        print "You punch the squirrel."
        squirrelHealth = int(squirrelHealth) - punchDmg
        print "The squirrel struck back"
        playerHealth = playerHealth - damageBySquirrel
        print 'Your health is ' + str(playerHealth)
        print 'The giant man eating squirrel`s health is ' + str(squirrelHealth)
    if userInput2 == 2:
        print "You stab the squirrel."
        squirrelHealth = int(squirrelHealth) - swordDmg
        print "The squirrel struck back"
        playerHealth = playerHealth - damageBySquirrel
        print 'Your health is ' + str(playerHealth)
        print 'The giant man eating squirrel`s health is ' + str(squirrelHealth)
    if userInput2 == 3:
        print "You hit the squirrel with your mace."
        squirrelHealth = int(squirrelHealth) - maceDmg
        print "The squirrel struck back"
        playerHealth = playerHealth - damageBySquirrel
        print 'Your health is ' + str(playerHealth)
        print 'The giant man eating squirrel`s health is ' + str(squirrelHealth)
    if (playerHealth > 0 and squirrelHealth < 0):
        print 'You killed the giant man eating squirrel!'
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print '(You start running down the path in the forest)'
        print ' '
        print '(You stop in front of a tree when all of a sudden a slime ball comes out from behind the tree and fights you)'
        #second fight
        while (playerHealth2 > 0 and slimeHealth > 0):
            print "Choose an action. 1 will punch, 2 will use the sword, and 3 will use the mace."
            userInput3 = int(raw_input())
            if userInput3 == 1:
                print "You punch the slime."
                slimeHealth = int(slimeHealth) - punchDmg
                print "The Slime struck back"
                playerHealth2 = playerHealth2 - damageBySlime
                print 'Your health is ' + str(playerHealth2)
                print 'The slime`s health is ' + str(slimeHealth)
            if userInput3 == 2:
                print "You stab the slime."
                slimeHealth = int(slimeHealth) - swordDmg
                print "The Slime struck back"
                playerHealth2 = playerHealth2 - damageBySlime
                print 'Your health is ' + str(playerHealth2)
                print 'The slime`s health is ' + str(slimeHealth)
            if userInput3 == 3:
                print "You hit the slime with your mace."
                slimeHealth = int(slimeHealth) - maceDmg
                print "The Slime struck back"
                playerHealth2 = playerHealth2 - damageBySlime
                print 'Your health is ' + str(playerHealth2)
                print 'The slimes health is ' + str(slimeHealth)
            if (playerHealth2 > 0 and slimeHealth < 0): 
                print 'You slayed the slime and start moving down the path once more.'
                print '(You dig a hole in the ground for safety through the night but you are awokened by the roar of a bear.)' 
                print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                #third fight
                while (playerHealth3 > 0 and bearHealth > 0):
                    print "Choose an action. 1 will punch, 2 will use the sword, and 3 will use the mace."
                    userInput4 = int(raw_input())
                    if userInput4 == 1:
                        print "You punch the bear."
                        bearHealth = int(bearHealth) - punchDmg
                        print "The bear struck back"
                        playerHealth3 = playerHealth3 - damageByBear
                        print 'Your health is ' + str(playerHealth3)
                        print 'The bear`s health is ' + str(bearHealth)
                    if userInput4 == 2:
                        print "You stab the bear."
                        bearHealth = int(bearHealth) - swordDmg
                        print "The bear struck back"
                        playerHealth3 = playerHealth3 - damageByBear
                        print 'Your health is ' + str(playerHealth3)
                        print 'The bear`s health is ' + str(bearHealth)
                    if userInput4 == 3:
                        print "You hit the bear with your mace."
                        bearHealth = int(bearHealth) - maceDmg
                        print "The bear struck back"
                        playerHealth3 = playerHealth3 - damageByBear
                        print 'Your health is ' + str(playerHealth3)
                        print 'The bears`s health is ' + str(bearHealth)
                    if (playerHealth > 0 and bearHealth < 0):
                        print 'You killed the bear!'
                        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'      
                        print ' '
                        print '(You start running when you come upon a house inside of a tree, you walk up to it and knock on the door. A wizard appears and says...'
                        print ' '
                        print 'Wizard: Let me guess you came upon my house on your journey to Trolly the Terrible.'
                        print str(userInput) + ': Uh yeah how did you know?'
                        print ' '
                        print 'Wizard: You are not the first knight that King Certifacto has sent on a task to defeat Trooly the Terrible.'
                        print 'I`ll make a deal with you, if I give you a lightning spell to defeat Trolly the Terrible you have to tell the king to never send anyone out here again.'
                        print ' '
                        print str(userInput) + ': Fine it`s a deal as long as I get the potion.'
                        print ' '
                        print '(The wizard suddenly pulls out a wand to figh you.)'
                        print ' '
                        print 'Wizard: You didn`t think that I would just give you a spell potion did you. HAHA. If you defeat me then you`ll be abble to get the spell.'
                        print str(userInput) + ': Oh no.'
                        print'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                        while (playerHealth4 > 0 and wizardHealth > 0):
                            print "Choose an action. 1 will punch, 2 will use the sword, and 3 will use the mace."
                            userInput5 = int(raw_input())
                            if userInput5 == 1:
                                print "You punch the wizard."
                                wizardHealth = int(wizardHealth) - punchDmg
                                print "The wizard struck back"
                                playerHealth4 = playerHealth4 - damageByWizard
                                print 'Your health is ' + str(playerHealth4)
                                print 'The wizards`s health is ' + str(wizardHealth)
                            if userInput5 == 2:
                                print "You stab the wizard."
                                wizardHealth = int(wizardHealth) - swordDmg
                                print "The wizard struck back"
                                playerHealth4 = playerHealth4 - damageByWizard
                                print 'Your health is ' + str(playerHealth4)
                                print 'The wizard`s health is ' + str(wizardHealth)
                            if userInput5 == 3:
                                print "You hit the wizard with your mace."
                                wizardHealth = int(wizardHealth) - maceDmg
                                print "The wizard struck back"
                                playerHealth4 = playerHealth4 - damageByWizard
                                print 'Your health is ' + str(playerHealth4)
                                print 'The wizards is ' + str(wizardHealth)
                            if (playerHealth > 0 and wizardHealth < 0):
                                print 'You killed the wizard!'
                                print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'      
                                print ' '
                                print 'You walk into the wizards house and grab the scroll with how to use the lightning spell and you read it.)'
                                print ' '
                                print 'YOU KNOW CAN USE THE LIGHTNING SPELL!!!!!!!!!!!!!!!!!'
                                print ' '
                                print '(You walk through the woods along teh path for about an hour and you see the other side of the forest and you sprint through the edge and into the open.)'
                                print ' '
                                print '(You look forward and see Trolly`s village so you walk into the village and walk up to Trolly.)'
                                print ' '
                                print str(userInput) + ': Are you Trolly the Terrible?'
                                print 'Trolly: Yes, and who are you you HUMAN!'
                                print str(userInput) + ': I`m the guy that is going to kill you and get back the kings crown!'
                                print 'Trolly: OH LETS SEE ABOUT THAT!'
                                print '(Trolly jumps from his throne and pulls out his bone sword to fight you.)'
                                while (playerHealth5 > 0 and trollytheterribleHealth > 0):
                                    print "Choose an action. 1 will punch, 2 will use the sword, and 3 will use the mace, and 4 will use the lightning spell."
                                    userInput6 = int(raw_input())                      
                                    if userInput6 == 1:
                                        print "You punch Trolly."
                                        trollytheterribleHealth = int(trollytheterribleHealth) - punchDmg
                                        print "Trolly struck back"
                                        playerHealth5 = playerHealth5 - damageByTrollyTheTerrible
                                        print 'Your health is ' + str(playerHealth5)
                                        print 'The Trollys`s health is ' + str(trollytheterribleHealth)
                                    if userInput6 == 2:
                                        print "You stab Trolly."
                                        trollytheterribleHealth = int(trollytheterribleHealth) - swordDmg
                                        print "Trolly struck back"
                                        playerHealth5 = playerHealth5 - damageByTrollyTheTerrible
                                        print 'Your health is ' + str(playerHealth4)
                                        print 'The Trolly`s health is ' + str(trollytheterribleHealth)
                                    if userInput6 == 3:
                                        print "You hit Trolly with your mace."
                                        trollytheterribleHealth = int(trollytheterribleHealth) - maceDmg
                                        print "Trolly struck back"
                                        playerHealth5 = playerHealth5 - damageByTrollyTheTerrible
                                        print 'Your health is ' + str(playerHealth4)
                                        print 'Trolly`s is ' + str(trollytheterribleHealth)
                                    if userInput6 == 4:
                                        print "You cast the lightning spell on Trolly."
                                        trollytheterribleHealth = int(trollytheterribleHealth) - lightningspellDmg
                                        print "Trolly struck back"
                                        playerHealth5 = playerHealth5 - damageByTrollyTheTerrible
                                        print 'Your health is ' + str(playerHealth5)
                                        print 'Trolly`s is ' + str(trollytheterribleHealth)                            
                                    if (playerHealth > 0 and trollytheterribleHealth < 0):
                                        print 'You killed Trolly the Terrible!'
                                        print '(You go into Trolly`s tent and get King Certifacato`s crown.)'
                                        print '(You go back to the kingdom and give the king his crown back.)'
                                        print '(The king thenn gives you 5,000,000 gold pieces and you lie happily ever after until he came back to life.)'
                                        print 'YOU WIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                                    if (playerHealth < 0 and trollytheterribleHealth >= 0): 
                                        print 'Trolly the Terrible demolidhed you.'   
                                        print 'GAME OVER' 
                            if (playerHealth < 0 and wizardHealth >= 0): 
                                print 'The wizard zapped you to death.'   
                                print 'GAME OVER' 
                    if (playerHealth <= 0 and bearHealth >= 0): 
                        print 'The bear mauled you to death.'   
                        print 'GAME OVER'
            if (playerHealth <= 0 and slimeHealth >= 0): 
                print 'The slime absorbed you.'   
                print 'GAME OVER'    
        if (playerHealth <= 0 and squirrelHealth >= 0): 
            print 'The Giant Man Eating squirrel ate you.'   
            print 'GAME OVER'

keepGoing = False

       
