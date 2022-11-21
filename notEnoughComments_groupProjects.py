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

statsDic = {
				"Difficulty:": "",
				"Weapon:": "",
				"Damage Taken:":0,
				"Health Healed:":0,
				"Remaining Hp:": 0,
				"Damage Dealt:":0,
				"Enemies Slain:":0,
				"Items Used:":0,
				"Rooms Cleared:":0,
				"Boss defeated?":"No"
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
		self.reload = False
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
	
	def	reloading(self):
		return self.reload
		
	def setReload(self, torf):
		self.reload = torf
	
	def getArmor(self):
		return self.resist
	
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
	print()
	print()
	time.sleep(1)
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
	statsDic["Weapon:"] = weaponChoice
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
	totalDmg = 0
	if weapon == "sword":
		mindmg = 1
		maxdmg = 15
		iterations = 2
			
	elif weapon == "axe":
		mindmg = 1
		maxdmg = 30
		iterations = 1
		
	elif weapon == "dagger":
		mindmg = 7
		maxdmg = 10
		iterations = 1
		
	elif weapon == "bow":
		mindmg = 0
		maxdmg = 10
		iterations = random.randint(2, 4)
	
	elif weapon == "greatsword":
		mindmg = 10
		maxdmg = 20 + modifier
		iterations = 1
	
	elif weapon == "spoon":
		mindmg = 1
		maxdmg = 5 + modifier
		iterations = 4
	
	elif weapon == "wand":
		mindmg = 0
		maxdmg = 15 + modifier
		iterations = 1
		if random.randint(1, 10) == 10:
			mindmg = 30
			maxdmg = 60
	
	elif weapon == "gun":
		mindmg = 5
		maxdmg = 30 + modifier
		iterations = 2
		player.setReload(True)
	
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
		dmgDealt = random.randint(mindmg, maxdmg)
		print()
		print(f"{dmgDealt}! damage")
		totalDmg += dmgDealt
		time.sleep(1)
	return totalDmg

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
	chance2 = random.randint(1, 10)
	#creates a random chance based on enemy cr to drop an item
	if chance1 == chance2:
		
		randCheck = random.randint(1,1000)
		
		if randCheck < 500:
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
	items = False
	for key in itemDic:
		if itemDic[key] > 0:
			items = True
			print("")
			print(f"You have {itemDic[key]} {key}")
	#checks if the player has an item or not and how many
	if items == False:
		print("")
		print("You have no items, choose a different action.")
	return items

def useItem(dic, player):
	#calls for the use of an item
	
	while True:
		print("")
		itemChoice = input("Enter the name of the item you would like to use: ")
		if itemChoice in dic.keys():
			statsDic["Items Used:"] += 1
			if itemChoice == "Health Potion":
				hpHealed = random.randint(20,40)
				player.setHp(player.getHp() + hpHealed)
				print()
				print("Your wounds close, you feel slightly better")
				statsDic["Health Healed:"] += hpHealed
				break
			elif itemChoice == "Strength Potion":
				player.setMod(player.getMod() + 5)
				print()
				print("A red haze covers your vision. You feel stronger.")
				break
			elif itemChoice == "Super Health Potion":	
				player.setHp(player.getHp() + random.randint(60,100))
				print()
				print("Your wounds close, you feel much better.")
				break
			elif itemChoice == "Rotten Berries":
				if random.randint(1,4) == random.randint(1,4):
					newHp = player.getHp() + random.randint(1,5)
					player.setHp(newHp)
					print()
					print(f"You eat the berries. They taste off, but you feel less terrible. Healed {newHp}")
				else:
					hpLost = player.getHp() - random.randint(1,5)
					player.setHp(hpLost)
					statsDic["Damage Taken:"] += hpLost
					print()
					print("That was not the best idea. Some hp has been lost.")
					break
			elif itemChoice == "Rubber Chicken":	
				print()
				print("The chicken squawks and dissapears")
				if random.randint(1, 100) > 95:
					player.setMod(player.getMod() + 2)
					print()
					print("You feel happy.")
				
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
		if not player.reloading():
			modifier = player.getMod()
			#player turn
			print("")
			action = input(f"What will {player.getName()} do? (attack, item, run): ")
			#asks input from player for their action
			if action == "attack":
				
				
				if dodgeCheck(enemyHitCount) == False:	
				#calls a dodge check to see if the enemy dodges
					
					hitDmg= weaponDamage(player, modifier)
					enemyTempHp -= hitDmg
					enemyHitCount += 1
					statsDic["Damage Dealt:"] += hitDmg
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
						print(f"The {enemy.getName()} has {enemyTempHp} health left")
					if player.getWeapon() != "error":
						player.setMod(0)
				#result of dodge check being True means they dodged
				else:
					#resets hitcount to make dodges harder again
					enemyHitCount = 0
					print("")
					print("The enemy dodged the attack")
					if player.getWeapon() == "error":
						player.setMod(player.getMod() + 2)
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
					if player.getWeapon() == "error":
						player.setMod(player.getMod() + 2)
				
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
		else:
			print()
			print("Reloading")
			player.setReload(False)
			time.sleep(2)
			print()
		
		#enemy turn
		if enemyTempHp > 0:
			if dodgeCheck(playerHitCount) == False:
				#checks if the player dodges, if failed, goes through the attack
				dmgRange = enemy.getDamage()
				dmgTaken = random.randint(1,dmgRange) - player.getArmor()
				if dmgTaken < 0:
					dmgTaken = 0
				#calls the damage from the enemy and deals it to player
				
				
					
				player.setHp(player.getHp() - dmgTaken)
				statsDic["Damage Taken:"] += dmgTaken
				
				if player.getHp() <= 0:
					print("")
					print(f"{player.getName()} has been slain!")
					playerAlive = False
					break
					#if player dies, the death message will be produced and it breaks the loop
				
				else:
					print("")
					print(f"{enemy.getName()} dealt {dmgTaken} damage. {player.getName()} has {player.getHp()} hp left.")
					
					if player.getWeapon() == "error":
						player.setMod(player.getMod() + 2)
					
					if player.getArmor() > 0:
						print("")
						print("The defense aura sputters and fades.")
					#if player is not dead, shows a message with damage taken and remaining hp of player
				player.setArmor(0)
			
			else:
				print("")
				print(f"{player.getName()} dodged the {enemy.getName()}'s attack!")
				#prints out if a successful dodge
		else:
			statsDic["Enemies Slain:"] += 1
	
	#fight success
	#if the player is alive (winning the fight) it returns that the player survived
	#else shows the player as dead
	return playerAlive

def doCombat(encounter, aPlayer):
	#calls for every enemy in the encounter to be fought back to back
	playerAlive = True
	for aEnemy in encounter:
		print(f"{aPlayer.getName()} is attacked by a {aEnemy.getName()}!")
		if fight(aPlayer, aEnemy) == False:
			playerAlive = False
			break
		else:
			pass
	return playerAlive

def bossFight(player, difficulty):
	
	charging = False
	playerAlive = True
	playerHitCount = 0
	bossAlive = True
	bossHitCount = 0
	bossHp = 0
	
	if difficulty == "Hard":
		
		bossHp = 600
	
	elif difficulty == "Medium":
		
		bossHp = 400

	elif difficulty == "Easy":
		
		bossHp = 200
	
	print()
	print("You are attacked by the incredibly powerful Matthew Priem!")
	print()
		
	while bossAlive:
		
		if not player.reloading():
		
			modifier = player.getMod()
			action = input(f"What will {player.getName()} do? (attack, item, run): ")
			#asks input from player for their action
			if action == "attack":
				
				
				if dodgeCheck(bossHitCount) == False:	
				#calls a dodge check to see if the enemy dodges
					
					hitDmg= weaponDamage(player, modifier)
					bossHp -= hitDmg
					bossHitCount += 1
					statsDic["Damage Dealt:"] += hitDmg
					#if the boss does not, it deals damage and ups hitcount for later dodge checks
					
					if bossHp <= 0:
						print("")
						print(f"You have defeated Matthew Priem!")
						statsDic["Boss defeated?"] = "Yes"
						if bossHp < 0:
							bossHp = 0
						bossAlive = False

					#checks if the boss has been killed by the attack
					#if yes, produces a kill message, if not, produces a remaining hp message
					
					else:
						print("")
						print(f"Matthew Priem has {bossHp} health left")
					
					player.setMod(0)
				#result of dodge check being True means they dodged
				else:
					#resets hitcount to make dodges harder again
					bossHitCount = 0
					print("")
					print("Matthew Priem dodged the attack")
					if player.getWeapon() == "error":
						player.setMod(player.getMod() + 2)
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
				print()
				print("You cannot escape.")
				if player.getWeapon() == "error":
					player.setMod(player.getMod() + 2)
				continue
			
			else:
				#resets to ask player action again if the player inputs something that is not expected
				print("")
				print("Please enter a valid input.")
				print("")
				continue
		
		else:
			print()
			print("Reloading")
			player.setReload(False)
			time.sleep(2)
			print()
		
		if bossHp > 0:
			decision = random.randint(1, 100)
			if charging:
				decision = 50
			tempDmg = 0
			if decision < 20:
				
				print()
				print("Priem makes fun of your handwriting.")
				
				tempDmg = random.randint(10, 30)
			
			elif decision < 70:
				if charging:
					
					print()
					print("You have been randomly selected to complete step 8.")
					
					tempDmg = random.randint(30, 100)
					
					charging = False
				
				else:
					
					print()
					print("Priem is charging up a powerful attack!")
					charging = True
			
			elif decision < 90:
				
				print()
				print("Priem has failed your exam.")
				
				tempDmg = random.randint(25, 40)
			
			else:
				
				print()
				print("Priem urges you to do the supplemental homework.")
				
			if dodgeCheck(playerHitCount) == False:
				#checks if the player dodges, if failed, goes through the attack
				
				dmgTaken = tempDmg - player.getArmor()
				
				if dmgTaken < 0:
					dmgTaken = 0
				#calls the damage from the enemy and deals it to player
				
				
					
				player.setHp(player.getHp() - dmgTaken)
				statsDic["Damage Taken:"] += dmgTaken
				
				if player.getHp() <= 0:
					print("")
					print(f"{player.getName()} has died at the hands of Priem.")
					playerAlive = False
					break
					#if player dies, the death message will be produced and it breaks the loop
				
				else:
					print("")
					print(f"Priem dealt {dmgTaken} damage. {player.getName()} has {player.getHp()} hp left.")
					
					if player.getWeapon() == "error":
						player.setMod(player.getMod() + 2)
					
					if player.getArmor() > 0:
						print("")
						print("The defense aura sputters and fades.")
					#if player is not dead, shows a message with damage taken and remaining hp of player
				player.setArmor(0)
			
			else:
				print("")
				print(f"{player.getName()} dodged Priem's attack!")
				#prints out if a successful dodge
			
			time.sleep(1)
	
	statsDic["Remaining Boss Hp:"] = bossHp
	return playerAlive

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
			
	statsDic["Difficulty:"] = difficulty
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
	

	
	
	#creates a player
	player = ThePlayer(playerName, playerHp, playerWeapon)
	
	
	#creates example enemies                                   
	goblin = Enemy("Goblin", 20, 10, 1)
	rock = Enemy("Rock Creature", 50, 20, 2)
	syntax = Enemy("Syntax Error", 30, 30, 2)
	golem = Enemy("Golem", 60, 10, 3)
	lego = Enemy("A single lego brick", 10, 100, 5)
	runTime = Enemy("Runtime Error", 100, 40, 8)
	

	enemyList = [goblin, rock, syntax, golem, lego, runTime]

	
	crCap = 2
	
	#the actual game is contained within one for loop
	#calls different rooms to determine enemy encounters and boss fights
	playerAlive = True
	for i in range(1, 9):
		if i == 3:
			itemRoom(player, items, 2)
			#sets up special rooms (for loot or a bossfight)
		elif i == 5:
			itemRoom(player, items, 4)
		elif i == 7:
			itemRoom(player, items, 6)
		elif i == 8:
			if not bossFight(player, difficulty):
				playerAlive = False
				break
			else:
				pass
		else:
			#if not a special room, it sets up a normal encounter room.
			combatList = combatEncounter(enemyList, crCap) 
			crCap += 2
			if not doCombat(combatList, player):
				playerAlive = False
				break
			else:
				pass
			
		
		statsDic["Rooms Cleared:"] += 1
		
		input("Press enter to continue to the next room")
		
		#clears terminal on windows
		os.system('cls')
		#clears terminal on mac and linux, commented out as most folks use windows
		#os.system('clear')
	
	print()	
	if not playerAlive:
		print("Better luck next time!")
	else:
		print("Congratulations! You have beaten the world's hardest(allegedly) text-based room-to-room dungeon crawler written in python!")
		print("This game was co-written by Owen Heuschele and Mason Schierts over a time period of just under one month.")
		print("This was pretty fun to make.")
		
	endTime = time.time()
	timeTaken = timeInMinutes(startTime, endTime)
	print("")
	checkFile = input("Save stats as file? y/n: ")
	print("")
	if checkFile == "y":
		
		if player.getHp() < 0:
			player.setHp(0)
		
		statsDic["Remaining Hp:"] = player.getHp()
		
		#record various stats
		#enemies slain, hp lost, hp gained, damage dealt, encounters survived, etc.
		runStats = open(f"{runName}.txt", "w")

		runStats.write(f"____________{runName}____________" + "\n")
		
		runStats.write("\n")
		runStats.write("{:20s} {:<6s}".format("Character Name:", player.getName()) + "\n")
		runStats.write("{:20s} {:<6s}".format("Time taken:", timeTaken) + "\n")
		
		for key in statsDic:
			
			try:
				runStats.write("{:<20s} {:<6d}".format(key, statsDic[key]) + "\n")
			except:
				runStats.write("{:<20s} {:<6s}".format(key, statsDic[key]) + "\n")
				
		runStats.close()
		print("file saved")
		print("")
	print("Thanks for playing!")

if __name__ == "__main__":
	#runs the main game
	__main__()


#this is run on python 3.10.6
#the code is written in Geany 1.38


