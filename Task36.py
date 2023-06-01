def print_operation_table(operation, num_rows=6, num_columns=6):

	array1 = []
	for row in range (1,num_rows+1):
		array2 = []
		for column in range (1,num_columns+1):
			array2.append(str(operation(row, column)))
		array1.append(array2)

	for row in range(num_rows):
		for column in range(num_columns):
			print(array1[row][column], end=" ")
		print()

print_operation_table(lambda x, y: x * y, 9, 5)