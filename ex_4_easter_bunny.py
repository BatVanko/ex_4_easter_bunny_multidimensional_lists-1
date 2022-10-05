import sys


def moving_directions(bunny_row, bunny_col):
    possible_positions = {
        'up': [bunny_row - 1, bunny_col],
        'down': [bunny_row + 1, bunny_col],
        'left': [bunny_row, bunny_col - 1],
        'right': [bunny_row, bunny_col + 1],
    }
    return possible_positions


size = int(input())

matrix = []
bunny_row = 0
bunny_col = 0
trap_row = 0
trap_col = 0
traps = []
for i in range(size):
    matrix.append([])
    row = input().split()
    for j in range(size):
        matrix[i].append(row[j])
        if matrix[i][j] == 'B':
            bunny_row = i
            bunny_col = j
        elif matrix[i][j] == 'X':
            trap_row = i
            trap_col = j
            traps.append([trap_row, trap_col])
directions = []
max_direction = None
max_name_of_direct = ''
max_sum = -sys.maxsize
max_coordinates = []
for direction in moving_directions(bunny_row, bunny_col):
    current_direction = []
    current_coordinates = []
    current_row = bunny_row
    current_col = bunny_col
    while True:
        ro, co = moving_directions(current_row, current_col)[direction]
        if 0 <= ro < len(matrix) and 0 <= co < len(matrix[0]) and matrix[ro][co] != 'X':
            current_num =  int(matrix[ro][co])

            if int(current_num) >= 0:
                current_direction.append(current_num)
                current_coordinates.append([ro,co])



        else:
            break
        current_row = ro
        current_col = co
    sum_current_direction = sum([int(x) for x in current_direction])
    if sum_current_direction > max_sum and sum_current_direction > 0:
        max_sum = sum_current_direction
        max_direction = current_direction
        max_name_of_direct = direction
        max_coordinates = current_coordinates

print(max_name_of_direct)
print(*max_coordinates, sep='\n')
print(max_sum)




