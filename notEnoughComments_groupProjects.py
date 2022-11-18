"""
Team Not Enough Comments

start date: 10/24/2022
Text based room to room dungeon crawler game
"""

import time
import random
import os

#imports elements for the program to run
#creates a dictionary with all obtainable items, with a starting quantity of zero
#used to display availible items and keep track of which items the player has
items = {
			"Health Potion":0,
			"Strength Potion":0, 
			"Super Health Potion":0,
			"Resistance Potion":0,
			"Rotten Berries":0, #heals 1-2 hp, but also has chance of dealing damage to player by eating
			"Rubber Chicken":0, #burns player turn by saying "Squak", using the item, and once again...waisting the player turn
			
			#loot table idea, random number generation between 1 and 1000
			#if number in range of item giver, u get that item, for chicken has to be ONE number
			}

class ThePlayer:
	#creates a class to store the player
	def __init__(self, name, health, weapon):
		#defines player stats like health and max damage
		self.name = name
		self.hp = health
		self.weapon = weapon
		self.modifier = 0
		self.resist = 0
		#Playername is for refrencing the player in prompts
		#damage is max damage that the player CAN deal, not guarenteed
	def getName(self):
		return self.name
	
	def getHp(self):
		return self.hp
	
	def getMod(self):
		return self.modifier
	
	def setMod(self, newMod):
		self.modifier = newMod
		
	
	def getArmor(self):
		return self.modifier
	
	def setArmor(self, newArmor):
		self.resist = newArmor
	#if weapon then change otherwise change all weapon to damage
	def getWeapon(self):
		return self.weapon
	#Setters to change the remaining hp of player
	#second one sets new damage for the player in case they get a new weapon	
	def setHp(self, newHp):
		self.hp = newHp
	
	def setWeapon(self, newWeapon):
		self.weapon = newWeapon

class Enemy:
	#enemy class, sets up a stat block for any enemy
	def __init__(self, name, health, damage, cr):
		#sets the inputs to the stored variables
		self.name = name
		self.hp = health
		self.damage = damage
		self.cr = cr
		#damage is max damage that CAN be delt by the enemy
	#functions to call for the stats to be used later
	def getName(self):
		return self.name
	def getHp(self):
		return self.hp
	def getDamage(self):
		return self.damage
	def getCr(self):
		return self.cr
	
	def setHp(self, newHp):
		self.hp = newHp
	
	def setDamage(self, newDamage):
		self.damage = newDamage

def weaponChoice(difficulty):
	
	if difficulty == "Easy" or difficulty == "Medium" or difficulty == "Hard":
		
		print("Choose your starting weapon:")
		print("")
		print("Sword: good average damage")
		print("")
		print("Axe: high max damage")
		print("")
		print("Dagger: cannot deal low damage, but cannot deal high damage")
		print("")
		print("Bow: can do low damage, but also high damage")
		print("")
		#prints out what the player can start with bassed on difficulty selected
		#Presents options only available to the difficulty level
		#still does not ask for the weapon, just prints out the options
		
		
		if difficulty == "Medium" or difficulty == "Hard":
		
			print("Greatsword: High damage, but missing skips your next turn.")
			print("")
			print("Alchemist Spoon: Low damage, but start with extra potions.")
			print("")
			print("Wand of Mystic Power: Low average damage, but chance to deal insane damage")
			print("")
			
			
			#all contained within each other so that it asscends and prints all the previous statements
			if difficulty == "Hard":
				
				print("Gun: Bang bang. High damage, reload every other turn")
				print("")
				print("Lashing Words: Mock your enemies to death! Deals no damage, but chance to one shot enemies.")
				print("")
				print("The Power of errorCodes: E r R o R, kill enemies with your failures")

	while True:	
		weaponChoice = input("You will use this weapon for the rest of the game. Choose wisely: ")
		#Allows player to pick their weapon, double checks that it is available
		
		#checks for valid weapon choice by name and difficulty level
		if (weaponChoice == "Wand of Mystic Power" or weaponChoice == "Alchemist Spoon" or weaponChoice == "Greatsword") and difficulty == "Easy":
			
			print("Weapon not availible for this difficulty.")
			continue
		
		elif (weaponChoice == "Gun" or weaponChoice == "Lashing Words" or weaponChoice == "The Power of errorCodes") and difficulty != "Hard":
			
			print("Weapon not availible for this difficulty.")
			continue
		
		elif weaponChoice == "Sword" or weaponChoice == "Axe" or weaponChoice == "Dagger" or weaponChoice == "Bow" or weaponChoice =="Wand of Mystic Power" or weaponChoice == "Alchemist Spoon" or weaponChoice == "Greatsword" or weaponChoice == "Gun" or weaponChoice == "Lashing Words" or weaponChoice =="The Power of errorCodes":
			
			print(f"You have chosen to wield {weaponChoice}.")
			break
		#if the weapon choise exists, it works, if not, it asks again		
		
		else:
			#asks again by forcing a repeat
			print("Enter weapon choice as written.")
			continue
	
	playerWeapon = ""	

	if weaponChoice == "Sword":
		playerWeapon = "sword"

	elif weaponChoice == "Axe":
		playerWeapon = "axe"

	elif weaponChoice == "Dagger":
		playerWeapon = "dagger"

	elif weaponChoice == "Bow":
		playerWeapon = "bow"
		
	elif weaponChoice == "Greatsword":
		playerWeapon = "greatsword"
	#Sets up the player weapon
	elif weaponChoice == "Alchemist Spoon":
		playerWeapon = "spoon"
	
	elif weaponChoice == "Wand of Mystic Power":
		playerWeapon = "wand"
	
	elif weaponChoice == "Gun":
		playerWeapon = "gun"
	
	elif weaponChoice == "Lashing Words":
		playerWeapon = "words"
	
	elif weaponChoice == "The Power of errorCodes":
		playerWeapon = "error"

	
	
	
	return playerWeapon

def weaponDamage(player, modifier):
	#sets up calculationa and damage of the weapon the player has
	weapon = player.getWeapon()
	dmgDealt = 0
	if weapon == "sword":
		mindmg = 1
		maxdmg = 10
		iterations = 2
			
	elif weapon == "axe":
		mindmg = 1
		maxdmg = 22
		iterations = 1
		
	elif weapon == "dagger":
		mindmg = 5
		maxdmg = 7
		iterations = 1
		
	elif weapon == "bow":
		mindmg = 0
		maxdmg = 6
		iterations = random.randint(2, 4)
	
	elif weapon == "greatsword":
		mindmg = 5
		maxdmg = 20 + modifier
		iterations = 1
	
	elif weapon == "spoon":
		mindmg = 1
		maxdmg = 5 + modifier
		iterations = 1
	
	elif weapon == "wand":
		mindmg = 0
		maxdmg = 15 + modifier
		iterations = 1
		if random.randint(1, 20) == 20:
			mindmg = 25
			maxdmg = 50
	
	elif weapon == "gun":
		mindmg = 5
		maxdmg = 19 + modifier
		iterations = 2
	
	elif weapon == "words":
		mindmg = 0
		maxdmg = 0 + modifier
		iterations = 1
		
		if random.randint(1, 20) == 20:
			mindmg = 1000
			maxdmg = 2000
			print("woah man, you hurt its feelings!")
		
	
	elif weapon == "error":
		mindmg = 1
		maxdmg = 1 + modifier
		iterations = 1
	#etc
	#This also returns the damage based on the weapon variables
	#calculates the attack damage from the player
	for i in range(iterations):
		dmgDealt += random.randint(mindmg, maxdmg)
		print()
		print(f"{dmgDealt}! damage")
	return dmgDealt

def enemyDifficulty(difficulty, enemyList):
	#creates an encounter for the player to fight
	#it feeds in a list of enemies and randomly gets a value
	#it finds the enemy with the CR(Challange Rating) equal to the random value
	#sets that into a list to feed into an encounter for the player to fight
	for foe in enemyList:
		
		if difficulty == "Hard":
			foe.setHp(foe.getHp() * 1.3)
			foe.setDamage(foe.getDamage() * 1.3)
		
		elif difficulty == "Easy":
			foe.setHp(foe.getHp() * 0.7)
			foe.setDamage(foe.getDamage() * 0.7)
	
def combatEncounter(listEnemy, crCap):
	#calls for a list of all enemies and a challange rating of the encounter
	encounterCr = 0
	encounterList = []
	#Searches for enemies until a list of enemies equal to the cr is found
	while encounterCr < crCap:
		enemyAdded = listEnemy[random.randint(0, (len(listEnemy) - 1))]
		if (enemyAdded.getCr() + encounterCr) > crCap:
			pass
		else:
			encounterList.append(enemyAdded)
			encounterCr += enemyAdded.getCr()
	#returns the enemies to be fed into the player to fight
	return encounterList

def itemDrop(enemy, itemDic):
	#feeds in a list of all items and an enemy dropping the item
	templist = []
	
	chance1 = random.randint(1, 10)
	chance2 = random.randint(1, 75)
	#creates a random chance based on enemy cr to drop an item
	if chance1 == chance2:
		
		randCheck = random.randint(1,1000)
		
		if randCheck < 300:
			templist = ["Rotten Berries"]
			
		elif randCheck < 700:
			templist = ["Health Potion", "Strength Potion", "Resistance Potion"]
		
		elif randCheck <= 999:
			templist = ["Health Potion", "Strength Potion", "Resistance Potion", "Super Health Potion"]
			
		elif randCheck == 1000:
			templist = ["Rubber Chicken"]
			
			
		#randomly picks a new item and gives the player the number of items
		newItem = templist[random.randint(0, len(templist) - 1)]
		plusQ = random.randint(1, 2)
		if randCheck < 100:
			plusQ += 3
		#picks a random number of items between 1 and the max
		itemDic[newItem] += plusQ
		#changes the item value in the dictionary of items the player has by the amount dropped
		if newItem == "Rotten Berries":
			print()
			print(f"{enemy.getName()} dropped {plusQ} {newItem}!")
			print()
			
		else:
			print()
			print(f"{enemy.getName()} dropped {plusQ} {newItem}(s)!")
			print()
		
		#prints out that the player got a new item and then returns that the player did get an item
		return True
	
	else:
		#if they did not drop an item, returns false that the player did not get an item
		return False

def itemRoom(player, itemDic, maxNum):
	templist = []
	#feeds in the player, the dictionary that is their inventory and a max number
	while True:
		#asks if player wants to open a chest
		print("Before you is a chest, open it? y/n")
		checkYes = input("")
		#makes sure that the player gives a valid input
		if checkYes != "y" and checkYes != "n":
			print("Invalid input")
		
		else:
			break
	#now that player has a valid input, sees if the player opens the chest or not
	if checkYes == "y":
		#creates a list of all items that exist in the game
		randCheck = random.randint(1,1000)
		
		if randCheck < 100:
			templist = ["Rotten Berries"]
			
		elif randCheck < 700:
			templist = ["Health Potion", "Strength Potion", "Resistance Potion"]
		
		elif randCheck <= 999:
			templist = ["Health Potion", "Strength Potion", "Resistance Potion", "Super Health Potion"]
			
		elif randCheck == 1000:
			templist = ["Rubber Chicken"]
			
			
		#randomly picks a new item and gives the player the number of items
		newItem = templist[random.randint(0, len(templist) - 1)]
		plusQ = random.randint(1, maxNum)
		if randCheck < 100:
			plusQ += 3
		#picks a random number of items between 1 and the max
		itemDic[newItem] += plusQ
		#adds the items to player inventory and prints out a message saying how many they got
		print()
		print(f"{player.getName()} has picked up {plusQ} {newItem}(s)!")
		print()
		return True
		#returns that they opened the chest
	else:
		#returns that the player did not open the chest
		return False
	
def itemCheck(itemDic):
	#finds what items the player has
	for key in itemDic:
		count = 0
		if itemDic[key] > 0:
			count += 1
			print("")
			print(f"You have {itemDic[key]} {key}(s)")
	#checks if the player has an item or not and how many
	if count == 0:
		print("")
		print("You have no items, choose a different action.")
		return False
	else:
		return True

def useItem(dic, player):
	#calls for the use of an item
	
	while True:
		print("")
		itemChoice = input("Enter the name of the item you would like to use: ")
		if itemChoice in dic.keys():
			if itemChoice == "Health Potion":
				player.setHp(player.getHp() + random.randint(20,40))
				break
			elif itemChoice == "Strength Potion":
				player.setMod(player.getMod() + 5)
				break
			elif itemChoice == "Super Health Potion":	
				player.setHp(player.getHp() + random.randint(60,100))
				break
			elif itemChoice == "Rotten Berries":
				if random.randint(1,4) == random.randint(1,4):
					newHp = player.getHp() + random.randint(1,5)
					player.setHp(newHp)
					print()
					print(f"You eat the berries. They taste off, but you feel slightly better. Healed {newHp}")
				else:
					player.setHp(player.getHp() - random.randint(1,5))
					print()
					print("That was not the best idea. Some hp has been lost.")
				break	
			
			elif itemChoice == "Rubber Chicken":	
				print()
				print("The chicken squawks and dissapears")
				break
				
			elif itemChoice == "Resistance Potion":
				player.setArmor(player.getArmor() + 5)
				print()
				print("A glowing aura surrounds you. You feel safer.")
				break
		else:
			print("")
			print("Enter item name as seen above.")

def dodgeCheck(hitCount):
	upBound = 20
	if hitCount == 0:
		upBound = 20
	#checks if the player has dodged recently
		
	else:
		if hitCount >= 5:
			hitCount = 5
		#makes a check to not run out of bounds
		upBound -= hitCount
	#the dodge recently check changes the upper bound of numbers
	#randomly generates two numbers, if they both come out to the same number
	#if both are equal, that means the player or enemy dodges the attack
	check1 = random.randint(1, 10)
	check2 = random.randint(1, upBound)
	
	#if player or enemy dodges the attack, it returns true so that damage is not dealt
	if check1 == check2:
		return True
	
	else:
		return False

def runCheck(hitCount):
	#works the same as dodgecheck with different values
	
	upBound = 12
	if hitCount == 0:
		upBound = 12
	#checks if the player has been hit recently
		
	else:
		if hitCount >= 5:
			hitCount = 5
		#makes a check to not run out of bounds
		upBound -= hitCount
	#the dodge recently check changes the upper bound of numbers
	#randomly generates two numbers, if they both come out to the same number
	#if both are equal, that means the player runs away
	check1 = random.randint(1, 7)
	check2 = random.randint(1, upBound)
	
	
	if check1 == check2:
		return True
	
	else:
		return False
	
def fight(player, enemy):
	print()
	#sets up stats for the fight
	#all combat is held within the fight function
	enemyName = enemy.getName()
	print("An enemy " + enemyName + " approaches")
	enemyAlive = True
	playerAlive = True
	enemyTempHp = enemy.getHp()
	enemyHitCount = 0
	playerHitCount = 0
	
	#sets hitcounts for dodge checks
	#gets hp of enemy stat block, but does not edit the enemy
	#this is done so that multiple enemies can be fed into an encounter
	#with multiple enemies, that is more storage and slower runtime, by feeding an enemy class
	#-we can pull a stat block of an enemy type and use that to feed into the fight encounter
	while enemyAlive:
		#used to break when the enemy dies to end the fight
		
		modifier = player.getMod()
		#player turn
		print("")
		action = input(f"What will {player.getName()} do? (attack, item, run): ")
		#asks input from player for their action
		if action == "attack":
			
			
			if dodgeCheck(enemyHitCount) == False:	
			#calls a dodge check to see if the enemy dodges
				
				enemyTempHp -= weaponDamage(player, modifier)
				enemyHitCount += 1
				#if the enemy does not, it deals damage and ups hitcount for later dodge checks
				
				if enemyTempHp <= 0:
					print("")
					print(f"The {enemy.getName()} has been slain!")
					itemDrop(enemy, items)
					enemyAlive = False

				#checks if the enemy has been killed by the attack
				#if yes, produces a kill message, if not, produces a remaining hp message
				
				else:
					print("")
					print(f"The enemy has {enemyTempHp} health left")
				
				player.setMod(0)
			#result of dodge check being True means they dodged
			else:
				#resets hitcount to make dodges harder again
				enemyHitCount = 0
				print("")
				print("The enemy dodged the attack")
				#makes an output statement to notify player that the enemy dodged
		
		elif action == "item":
			#make a thing to use items here
			#dictionary of items, check if player has(if key in dic.keys()), tell player what they have
			#create function with all items as input.
			
			if itemCheck(items) == False:
				continue
			
			else:
				useItem(items, player)
			
			
		
		elif action == "run":
			#run check time(run away)
			if runCheck(playerHitCount) == False:
				print("")
				print(f"{player.getName()} tried to run, but could not escape.")
			
			else:
				print("")
				print(f"The {enemy.getName()} got bored, and decided to leave {player.getName()} alone.")
				break
		
		else:
			#resets to ask player action again if the player inputs something that is not expected
			print("")
			print("Please enter a valid input.")
			print("")
			continue
		
		#enemy turn
		if enemyTempHp > 0:
			if dodgeCheck(playerHitCount) == False:
				#checks if the player dodges, if failed, goes through the attack
				dmgRange = enemy.getDamage()
				dmgTaken = random.randint(1,dmgRange) - player.getArmor()
				if dmgTaken < 0:
					dmgTaken = 0
				#calls the damage from the enemy and deals it to player
				
				if player.getArmor() > 0:
					print()
					print("The defense aura sputters and fades.")
					
				player.setHp(player.getHp() - dmgTaken)
				
				if player.getHp() <= 0:
					print("")
					print(f"{player.getName()} has been slain!")
					playerAlive = False
					break
					#if player dies, the death message will be produced and it breaks the loop
				
				else:
					print("")
					print(f"{player.getName()} took {dmgTaken} damage and has {player.getHp()} hp left.")
					#if player is not dead, shows a message with damage taken and remaining hp of player
				player.setArmor(0)
			
			else:
				print("")
				print(f"{player.getName()} dodged the {enemy.getName()}'s attack!")
				#prints out if a successful dodge
	
	#fight success
	#if the player is alive (winning the fight) it returns that the player survived
	#else shows the player as dead
	return playerAlive

def doCombat(encounter, aPlayer):
	#calls for every enemy in the encounter to be fought back to back
	for aEnemy in encounter:
		print(f"{aPlayer.getName()} is attacked by a {aEnemy.getName()}!")
		fight(aPlayer, aEnemy)

def bossFight(player):
	pass

def timeInMinutes(start, end):
	#a clock, finds the time player took to play game
	timeInSeconds = end - start
	
	minutes = int(timeInSeconds//60)
	#finds out the runtime in minutes and seconds
	seconds = round(timeInSeconds - (minutes * 60))
	#returns it for a stat page
	return f"{minutes}:{seconds}"

	#calls for a time check when game ends
	endTime = time.time()
	timeTaken = timeInMinutes(startTime, endTime)

def __main__():
	
	startTime = time.time()

	#Begins running the game
	#player settings for personalization
	runName = input("Name this run: ")
	playerName = input("Name your character: ")
	difficulty = ""
	
	print("")
	print("Difficulty selection:")
	print("")
	print("Easy: Baby mode. High health, but limited weapon options.")
	print("")
	print("Medium: Standard. Mid-range health, expanded weapon list.")
	print("")
	print("Hard: The dark souls of text-based room-to-room dungeon crawlers. All weapons availible.")
	print("")
	
	#print statements to ask player what difficulty level they wish to use
	while True:
		
		difficulty = input("Enter in a difficuly level: ")
		
		if difficulty == "Hard" or difficulty == "Easy" or difficulty == "Medium":
			
			print("You have selected " + difficulty)
			#if the player picks a valid option, it breaks out of the loop
			#valid options are only the words for the difficulty level, description is not included
			break
		
		else:
			
			print("Please enter the name as written")
			#if an invalid option is met, it says so and asks again
			#continues asking until an option is chosen
			
	
	#sets up the player hp based on level
	#this makes the game more difficlt as the player has to survive on less health
	#the boss will also get more health with a higher level
	#most of the difficulty comes from these two factors
	if difficulty == "Easy":
		
		playerHp = 700

	elif difficulty == "Medium":
		
		playerHp = 500

	elif difficulty == "Hard":
		
		playerHp = 300
	
	#calls a function for the player to choose their weapon
	playerWeapon = weaponChoice(difficulty)
	
	if playerWeapon == "spoon":
		spoonPotions = ["Health Potion", "Strength Potion", "Resistance Potion"]
		for i in range(2):
			items[spoonPotions[random.randint(0, len(spoonPotions) - 1)]] += 1
	
	statsDic = {
				"Enemies Slain:":0,
				"Damage Dealt:":0,
				"Items Used:":0,
				"Damage Taken:":0,
				"Rooms Cleared:":0,
				"Boss defeated?":"No"
				}
	
	
	#creates a player
	player = ThePlayer(playerName, playerHp, playerWeapon)
	
	
	#creates example enemies                                   
	goblin = Enemy("Goblin", 25, 10, 1)
	rock = Enemy("Rock Creature", 50, 20, 2)
	syntax = Enemy("Syntax Error", 35, 30, 2)
	golem = Enemy("Golem", 60, 10, 3)
	lego = Enemy("A single lego brick", 10, 100, 5)
	runTime = Enemy("Runtime Error", 100, 40, 8)
	

	enemyList = [goblin, rock, syntax, golem, lego, runTime]

	
	crCap = 2
	
	#the actual game is contained within one for loop
	#calls different rooms to determine enemy encounters and boss fights
	for i in range(1, 9):
		if i == 3:
			itemRoom(player, items, 2)
			#sets up special rooms (for loot or a bossfight)
		elif i == 5:
			itemRoom(player, items, 4)
		elif i == 7:
			itemRoom(player, items, 6)
		elif i == 8:
			pass
		else:
			#if not a special room, it sets up a normal encounter room.
			combatList = combatEncounter(enemyList, crCap) 
			crCap += 3
			doCombat(combatList, player) 
		
		totalRoomsDone += 1
		
		input("Press enter to continue to the next room")
		os.system('cls')
		
	endTime = time.time()
	timeTaken = endTime - startTime	
	print("")
	checkFile = input("Save stats as file? y/n: ")
	print("")
	if checkFile == "y":
		#record various stats
		#enemies slain, hp lost, hp gained, damage dealt, encounters survived, etc.
		runStats = open(f"{runName}.txt", "w")

		runStats.write(runName)
		runStats.write("")
		runStats.write(f"Time taken: {timeTaken}")
		for key in statsDic:
			runStats.write("{:20s} {:4f}".format(key, statsDic[key]))

		runStats.close()
		print("file saved")
		print("")
	print("Thanks for playing!")

if __name__ == "__main__":
	#runs the main game
	__main__()


#this is run on python 3.10.6
#the code is written in Geany 1.38


