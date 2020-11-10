# Selection Sort
# Needed for max number
import sys

def sort(list):
	# The highest number in list
	highestNum = 0
	# The output list
	newList = []

	# Find the highest number in the list so we have a stopping point
	# Loop through the list
	for y in list:
		# If the current spot in the list is greater than the previous greater number
		if y > highestNum:
			# Set the highest number as the current spot
			highestNum = y		

	# Loop through the list while the highest number isnt in the last position, which means we havent gone through the whole list and sorted it
	# For the first loop there is no last position so we have to have the 0 check so it doesnt error, list index out of range
	while len(newList) == 0 or newList[-1] != highestNum:
		# Get the highest integer possible
		lowestNum = sys.maxsize

		# Find the lowest number in the list
		# Loop through the list
		for x in list:
			# If the current spot in the list is less than the previous lowest number
			if x < lowestNum:
				# Set the current lowest number to the current position in the list
				lowestNum = x

		# Remove the lowest number from the current list so it isnt used again
		list.remove(lowestNum)
		# Append the lowest number to the end of the output list
		newList.append(lowestNum)
		
	# Return the output list
	return newList

# Sort
print(sort([2, 3, 1, 8, 6, 7, 5, 4]))