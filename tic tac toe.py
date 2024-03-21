array = [['.','.','.'], ['.','.','.'], ['.','.','.']]
def show_game(array):
    for r in array:
        for c in r:
            print(c + ' ', end = '')
        print()

show_game(array)
print()
for i in range(5):
    for j in range(2):
        if i == 4 and j == 1:
            break
        if j == 0:
            print('User A! Your Turn')
            print()
            while True:
                while True:
                    try:
                        userA_row = int(input('Which row you want to select: '))
                        break
                    except:
                        print('You should give an integer')
                if userA_row < 1 or userA_row > 3:
                    print('You should give the correct row')
                    continue
                while True:
                    try:
                        userA_column = int(input('Which column you want to select: '))
                        break
                    except:
                        print('You should give an integer')
                print()
                if userA_column < 1 or userA_column > 3:
                    print('You should give the correct column')
                    continue
                if array[userA_row-1][userA_column-1] == '.':
                    array[userA_row-1][userA_column-1] = 'A'
                    print()
                    show_game(array)
                    print()
                    break
                if array[userA_row-1][userA_column-1] != '.':
                    print('The row and column you provided is already filled! Please give another row and column')
                    continue
        if (array[0][0] == 'A' and  array[0][1] == 'A' and array[0][2] == 'A') or (array[1][0] == 'A' and array[1][1] == 'A' and array[1][2] == 'A') or (array[2][0] == 'A' and  array[2][1] == 'A' and array[2][2] == 'A') or (array[0][0] == 'A' and  array[1][1] == 'A' and array[2][2] == 'A') or (array[0][2] == 'A' and  array[1][1] == 'A' and array[2][0] == 'A'):
            break
                
        if j == 1:
            print('User B! Your Turn')
            print()
            while True:
                while True:
                    try:
                        userB_row = int(input('Which row you want to select: '))
                        break
                    except:
                        print('You should give an integer')
                if userB_row < 1 or userB_row > 3:
                    print('You should give the correct row')
                    continue
                while True:
                    try:
                        userB_column = int(input('Which column you want to select: '))
                        break
                    except:
                        print('You should give an integer')
                print()
                if userB_column < 1 or userB_column > 3:
                    print('You should give the correct column')
                    continue
                if array[userB_row-1][userB_column-1] == '.':
                    array[userB_row-1][userB_column-1] = 'B'
                    show_game(array)
                    print()
                    break
                if array[userB_row-1][userB_column-1] != '.':
                    print('The row and column you provided is already filled! Please give another row and column')
                    continue
        if (array[0][0] == 'B' and  array[0][1] == 'B' and array[0][2] == 'B') or (array[1][0] == 'B' and array[1][1] == 'B' and array[1][2] == 'B') or (array[2][0] == 'B' and  array[2][1] == 'B' and array[2][2] == 'B') or (array[0][0] == 'B' and  array[1][1] == 'B' and array[2][2] == 'B') or (array[0][2] == 'B' and  array[1][1] == 'B' and array[2][0] == 'B'):
            break
            
    if (array[0][0] == 'A' and  array[0][1] == 'A' and array[0][2] == 'A') or (array[1][0] == 'A' and array[1][1] == 'A' and array[1][2] == 'A') or (array[2][0] == 'A' and  array[2][1] == 'A' and array[2][2] == 'A') or (array[0][0] == 'A' and  array[1][1] == 'A' and array[2][2] == 'A') or (array[0][2] == 'A' and  array[1][1] == 'A' and array[2][0] == 'A'):
        print('User A won the match')
        break
    
    if (array[0][0] == 'B' and  array[0][1] == 'B' and array[0][2] == 'B') or (array[1][0] == 'B' and array[1][1] == 'B' and array[1][2] == 'B') or (array[2][0] == 'B' and  array[2][1] == 'B' and array[2][2] == 'B') or (array[0][0] == 'B' and  array[1][1] == 'B' and array[2][2] == 'B') or (array[0][2] == 'B' and  array[1][1] == 'B' and array[2][0] == 'B'):
        print('User B won the match')
        break

else:
    print('The match has tie')