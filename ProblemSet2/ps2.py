#File Name: ps1.py
#Author: Chaitra Kothari
#Date: Oct 28th, 2015
#Description: This program solves Diophantine equation to find max number of nuggets that cannot be bought given 3 different package sizes

#=========================Problem1==============================
posPackageSolutions = []
numNuggets = [50, 51, 52, 53, 54, 55]

for nuggets in numNuggets:
	for numTwentyPacks in range(5):
		for numNinePacks in range(7):
			for numSixPacks in range(7):
				if (6 * numSixPacks + 9 * numNinePacks + 20 * numTwentyPacks == nuggets):
					posPackageSolutions.append((numSixPacks, numNinePacks, numTwentyPacks, nuggets))

print posPackageSolutions


#=========================Problem2==============================
To prove: If it is possible to buy x, x+1,…, x+5 sets of McNuggets, for some x, then it is possible to buy any number of McNuggets >= x, 
given that McNuggets come in 6, 9 and 20 packs.

Proof: Given that it is possible to buy x, x+1,…, x+5 sets of McNuggets, for some x with some combination of (numSixPacks, numNinePacks, numTwentyPacks)
If we want to buy x+6 nuggets, we just need to buy one additional package of 6pack nuggets that was needed to buy x nuggets.
Similary, if we want to buy x+7 nuggets, we just need to buy one additional package of 6pack nuggets that was needed to buy x+1 nuggets. 
Similary, if we want to buy x+8 nuggets, we just need to buy one additional package of 6pack nuggets that was needed to buy x+2 nuggets. 
And this pattern continues. This is due to the fact that if we can buy x nuggets, we can buy x+6 nuggets by just buying one additional number of 6pack nuggets.

For example, we know that we can buy 50, 51, 52, 53, 54 and 55 nuggets. We want to prove that given this case, we can also buy 56, 57, 58, 59, 60 and 61 number of 
nuggets. Consider the subtracting one row of values from another in the following computation

Number of nuggets | 56 | 57 | 58 | 59 | 60 | 61 |
Number of nuggets | 50 | 51 | 52 | 53 | 54 | 55 |
==================================================
Difference        | 6  | 6  | 6  | 6  | 6  | 6  |

So, if we can buy 50 nuggets with say 5 packs of 6nugget packages and 1 pack of 20nugget package, we can also buy 56 nuggets by buying 6packs of 6nugget packages
and 1 pack of 20nugget package. Similary, once we can buy 6 consecutive number of nuggets, we can buy any number of nuggets above that by just adding 6nugget package. 

Number of nuggets | 62 | 63 | 64 | 65 | 66 | 67 |
Number of nuggets | 56 | 57 | 58 | 59 | 60 | 61 |
==================================================
Difference        | 6  | 6  | 6  | 6  | 6  | 6  |

Again, given a combination of packages to buy 56 nuggets; we just need to buy one additional 6pack nuggets in order to be able to buy 62 nuggets and this chain 
continues

#=========================Problem3==============================
canBeBought = []
n = []

def solve():
	for numNuggets in range(1, 150):
		n.append(numNuggets)
		for numTwentyPacks in range(7):
			for numNinePacks in range(11):
				for numSixPacks in range(11):
					if 6 * numSixPacks + 9 * numNinePacks + 20 * numTwentyPacks == numNuggets:
						canBeBought.append(numNuggets)
	
	cannotBeBought = list(set(n) - set(canBeBought))
	return cannotBeBought

cannotBeBought = solve()
print 'Largest number of McNuggets that cannot be bought in exact quantity is:', max(cannotBeBought)


#==========================Problem4===================================
def solve(packages):
	canBeBought = []
	for numNuggets in range(1, 150):
		n.append(numNuggets)
		for i in range(11):
			for j in range(11):
				for k in range(11):
					if packages[0] * k + packages[1] * j + packages[2] * i == numNuggets:
						canBeBought.append(numNuggets)
	
	cannotBeBought = list(set(n) - set(canBeBought))
	return cannotBeBought

packages = (6, 9, 20)
cannotBeBought = solve(packages)
print 'Given package sizes', packages[0], packages[1], 'and,', packages[2],', the largest number of McNuggets that cannot be bought in exact quantity is:', max(cannotBeBought)

packages = (3, 6, 15)
cannotBeBought = solve(packages)
print 'Given package sizes', packages[0], packages[1], 'and,', packages[2],', the largest number of McNuggets that cannot be bought in exact quantity is:', max(cannotBeBought)


