"""
Team Not Enough Comments

start date: 10/24/2022

"""

import time
import random

startTime = time.time()

runName = input("Name this run: ")
playerName = input("Name your character: ")
print("")
print("Difficulty selection:")
print("")
print("Easy: Baby mode. High health, but limited weapon options.")
print("")
print("Medium: Standard. Mid-range health, expanded weapon list.")
print("")
print("Hard: The dark souls of text-based room-to-room dungeon crawlers. All weapons availible.")
print("")
while True:
	difficulty = input("Enter in a difficuly level: ")
	if difficulty != "Hard" or "Easy" or "Medium":
		print("Enter difficulty as written.")
		continue

if difficulty == "Easy":
	
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
	
	
	if difficulty == "Medium":
	
		print("Greatsword: High damage, but missing skips your next turn.")
		print("")
		print("Alchemist Spoon: Low damage, but start with extra potions.")
		print("")
		print("Wand of Mystic Power: Low average damage, but chance to deal insane damage")
		print("")
		
		if difficulty == "Hard":
			
			print("Gun: Bang bang. High damage, reload every other turn")
			print("")
			print("Lashing Words: Mock your enemies to death! Deals no damage, but chance to one shot enemies.")
			print("")
			print("The Power of Friendship: You have no friends. You deal no damage. The ultimate challenge.")

while True:	
	weaponChoice = input("You will use this weapon for the rest of the game. Choose wisely: ")
	
	
	
	if (weaponChoice == "Wand of Mystic Power" or "Alchemist Spoon" or "Greatsword") and difficulty == "Easy":
		
		print("Weapon not availible for this difficulty.")
		continue
	
	elif (weaponChoice == "Gun" or "Lashing Words" or "The Power of Friendship") and difficulty != "Hard":
		
		print("Weapon not availible for this difficulty.")
		continue
	
	elif weaponChoice != "Sword" or "Axe" or "Dagger" or "Bow" or "Wand of Mystic Power" or "Alchemist Spoon" or "Greatsword" or "Gun" or "Lashing Words" or "The Power of Friendship":
		
		print("Enter weapon choice as written.")
		continue	
	
	else:
		
		print(f"You have chosen to wield {weaponChoice}.")
		break
	

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


if difficulty == "Easy":
	
	playerHp = 700

elif difficulty == "Medium":
	
	playerHp = 500

elif difficulty == "Hard":
	
	playerHp = 300

playerWeapon = 15


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
		
	


#creates example enemies                                   
goblin = Enemy("Goblin", 25, 10, 1)
rock = Enemy("Rock Creature", 50, 20, 2)

enemyList = [goblin, rock]


def enemyDifficulty(difficulty, enemyList):
	for foe in enemyList:
		
		if difficulty == "Hard":
			foe.setHp(foe.getHp() * 1.3)
			foe.setDamage(foe.getDamage() * 1.3)
		
		elif difficulty == "Easy":
			foe.setHp(foe.getHp() * 0.7)
			foe.setDamage(foe.getDamage() * 0.7)

class Player:
	#creates a class to store the player
	def __init__(self, name, health, weapon):
		#defines player stats like health and max damage
		self.name = name
		self.hp = health
		self.weapon = weapon
		#Playername is for refrencing the player in prompts
		#damage is max damage that the player CAN deal, not guarenteed
	def getName(self):
		return self.name
	def getHp(self):
		return self.hp
	
	
	#if weapon then change otherwise change all weapon to damage
	def getDamage(self):
		return self.weapon
	#Setters to change the remaining hp of player
	#second one sets new damage for the player in case they get a new weapon	
	def setHp(self, newHp):
		self.hp = newHp
	
	def setWeapon(self, newWeapon):
		self.weapon = newWeapon


player = Player(playerName, playerHp, playerWeapon)
#creates a player



#damage calc concept for weapon concept
def weaponDamage(player):
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
	#etc
	
	for i in range(iterations):
		dmgDealt += random.randint(mindmg, maxdmg)
	return dmgDealt


#creates a dictionary with all obtainable items, with a starting quantity of zero
#used to display availible items and keep track of which items the player has
items = {"Health Potion":0, "Strength Potion":0}

def combatEncounter(listEnemy, crCap):
	encounterCr = 0
	encounterList = []
	while encounterCr <= crCap:
		enemyAdded = listEnemy[random.randint(0, len(listEnemy)-1)]
		if (enemyAdded.getCr() + encounterCr) > crCap:
			continue
		else:
			encounterList.append(enemyAdded)
			encounterCr += enemyAdded.getCr()
	return encounterList
	
def doCombat(encounter, player):
	for enemy in encounter:
		print(f"{player.getName()} is attacked by a {enemy.getName()}!")
		fight(player, enemy)
	
def itemCheck(itemDic):
	for key in itemDic:
		count = 0
		if itemDic[key] > 0:
			count += 1
			print("")
			print(f"You have {itemDic[key]} {key}(s)")
	if count == 0:
		print("")
		print("You have no items, choose a different action.")
		return False
	else:
		return True

def useItem(dic, player):
	while True:
		print("")
		itemChoice = input("Enter the name of the item you would like to use: ")
		if itemChoice in dic.keys():
			if itemChoice == "Health Potion":
				#do hp pot
				break
			elif itemChoice == "Strength Potion":
				#do str pot
				break
		else:
			print("")
			print("Enter item name as seen above.")
		
	return f"{player.getName()} used {itemChoice}."

def dodgeCheck(hitCount):
	upBound = 15
	if hitCount == 0:
		upBound = 15
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
	#sets up stats for the fight
	#all combat is held within the fight function
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
		
		#player turn
		print("")
		action = input(f"What will {player.getName()} do? (attack, item, run): ")
		#asks input from player for their action
		if action == "attack":
			dmgRange = player.getDamage()
		#if an attack is called, it calls the max damage of the player	
			if dodgeCheck(enemyHitCount) == False:	
			#calls a dodge check to see if the enemy dodges
				
				enemyTempHp -= random.randint(1,dmgRange)
				enemyHitCount += 1
				#if the enemy does not, it deals damage and ups hitcount for later dodge checks
				
				if enemyTempHp <= 0:
					print("")
					print(f"The {enemy.getName()} has been slain!")
					enemyAlive = False
				#checks if the enemy has been killed by the attack
				#if yes, produces a kill message, if not, produces a remaining hp message
				
				else:
					print("")
					print(f"The enemy has {enemyTempHp} health left")
				
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
		
		if dodgeCheck(playerHitCount) == False:
			#checks if the player dodges, if failed, goes through the attack
			dmgRange = enemy.getDamage()
			dmgTaken = random.randint(1,dmgRange)
			#calls the damage from the enemy and deals it to player
			
			player.setHp(player.getHp() - dmgTaken)
			
			if player.getHp() <= 0:
				print("")
				print(f"{player.getName()} has been slain!")
				playerAlive = False
				break
				#if player dies, the death message will be produced and it breaks the loop
			
			else:
				print("")
				print(f"{playerName} took {dmgTaken} damage and has {player.getHp()} hp left.")
				#if player is not dead, shows a message with damage taken and remaining hp of player
		
		else:
			print("")
			print(f"{playerName} dodged the {enemy.getName()}'s attack!")
			#prints out if a successful dodge
	
	#fight success
	#if the player is alive (winning the fight) it returns that the player survived
	#else shows the player as dead
	if playerAlive == True:
		return True
	else:
		return False	



#calls a list of enemies in an encounter for a player to fight

	
	
#the actual game is contained within one for loop
#calls different rooms to determine enemy encounters and boss fights
for i in range(1, 9):
	if i == 3:
		pass
	elif i == 5:
		pass
	elif i == 7:
		pass
	elif i == 8:
		pass
	else:
		pass

fight(player, goblin)



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

#outputs time that the game took
print(timeTaken)

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

	runStats.close()
	print("file saved")
	print("")
print("Thanks for playing!")
