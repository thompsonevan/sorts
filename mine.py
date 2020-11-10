# Trying my own way to sort if it looks liek anyother alogirthim then so be it.
# I think this is just bad selection sort
def sort(list):
	highestNum = 0
	newList = []

	for y in list:
		if y > highestNum:
			highestNum = y		

	while len(newList) == 0 or newList[-1] != highestNum:
		lowestNum = 9999999999

		for x in list:
			if x < lowestNum:
				lowestNum = x

		print(newList)

		list.remove(lowestNum)
		newList.append(lowestNum)
		
	return newList

list = [20, 40, 30, 20, 100, 90, 80, 60, 70, 20, 50, 23, 1, 84, 1, 23, 9]

thing = sort(list)

print(thing)