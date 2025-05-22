#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
num_cols = len(matrix[0])
start = num_cols // 2 - 1
end = start + 2
the_middle = [[row[i] for i in range(start, end)] for row in matrix]
print("The middle columns of the matrix are: {}".format(the_middle))
