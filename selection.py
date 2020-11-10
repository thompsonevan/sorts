# Selection Sort
# Needed for max number
import sys

def sort(list):
	# The output list
	newList = []
	# Get the original list length for checking if sort is done
	originalListLength = len(list)

	# Loop through the sort until the new list is equal to the original in length
	while len(newList) != originalListLength:
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
print(sort([0 ,2, 3, 1, 8, 6, 7, 5, 4]))