import csv

# CHANGE THIS TO THE CSV YOU WANT TO ANALYZE
csv_path_in = "C:/Users/Matthieu/Desktop/CarlsenStats.csv"
Carlsen_moves = [["1.d4 Nf6 2.Nf3 d5 3.Bf4 c5", 0], ["1.c4 c5 2.g3 g6 3.Bg2 Bg7", 0], ["1.c4 Nf6 2.Nc3 e5 3.g3 Bb4", 1],
                 ["1.d4 Nf6 2.Bg5 d5 3.e3 c5", 1], ["1.e4 c5 2.Nf3 d6 3.d4 cxd4,", -1], ["1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6", 0],
                 ["1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6", 0], ["1.c4 Nf6 2.Nc3 e5 3.Nf3 Nc6", 1], ["1.d4 Nf6 2.c4 e6 3.Nf3 d5", 0],
                 ["1.e4 e5 2.Nf3 Nc6 3.Bb5 a6", 1], ["1.e4 c5 2.Nf3 d6 3.d4 cxd4", 1], ["1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6", 0],
                 ["1.c4 Nf6 2.Nc3 e6 3.e4 d5", 0], ["1.c4 e6 2.Nc3 d5 3.d4 Nf6", 1], ["1.c4 c5 2.g3 g6 3.Bg2 Bg7", 1],
                 ["1.d4 Nf6 2.c4 e6 3.Nf3 d5", 1], ["1.c4 e5 2.g3 Nf6 3.Nc3 Bb4", 0], ["1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6", 1],
                 ["1.e4 e5 2.Nf3 Nf6 3.Bb5 Nf6", 1], ["1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6", 1], ]

# sample :
# moves = [["1.e4 e5 2.Nf3 Nf6 3.Bb5 Nf6", 1], ["1.e4 e5 2.Nf3 Nf6 3.Bb5 Nf6", 1]]


def clean_move(movement):
    movement = movement.split(".")
    movement = movement[1:]
    for x in range(len(movement)):
        if x != len(movement) - 1:
            movement[x] = movement[x][:-2]
    player_moves = " "
    for x in range(len(movement)):
        player_moves = player_moves + movement[x].split(" ")[0] + ' '
    player_moves = player_moves[:-1]
    return player_moves


def get_move_index(movement, list_of_moves):
    index = 0
    for x in range(len(list_of_moves)):
        if movement[0] == list_of_moves[x][0]:
            index = x
    return index


def move_is_in_list(movement, list_of_moves):
    is_true = False
    for movement_of_list in list_of_moves:
        if movement[0] == movement_of_list[0]:
            is_true = True
            break
    return is_true


# list moves sample : moves, number of wins, number of defeats, number of draws
# e4Nf3Nc3, 1, 0, 2
def analyse_moves(moves):
    list_moves = []
    for move in moves:
        move[0] = clean_move(move[0])
        move[0] = move[0][1:]
        if not move_is_in_list(move, list_moves):
            if move[1] == 0:
                list_moves.append([move[0], 0, 0, 1])
            elif move[1] == 1:
                list_moves.append([move[0], 1, 0, 0])
            elif move[1] == -1:
                list_moves.append([move[0], 0, 1, 0])
        else:
            move_index = get_move_index(move, list_moves)
            if move[1] == 0:
                list_moves[move_index][3] = list_moves[move_index][3] + 1
            elif move[1] == 1:
                list_moves[move_index][1] = list_moves[move_index][1] + 1
            elif move[1] == -1:
                list_moves[move_index][2] = list_moves[move_index][2] + 1

    return list_moves


def create_csv_for_games():
    with open("C:/Users/Matthieu/Desktop/game_results.csv", "w") as csv_file:
        fieldnames = ["game_id", "player1 ID", "player2 ID", "winner", "list_moves", "points for P1", "points for P2"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
    csv_file.close()


def open_csv(csv_path):
    rows = []

    with open(csv_path, 'r') as csv_file:
        csv_file.__next__()
        reader = csv.reader(csv_file)
        for row in reader:
            rows.append(row)
    return rows
# csv format :
# ID, PLAYER1_NAME, PLAYER2_NAME, WINNER, LIST_OF_THREE_FIRST_MOVES


def list_to_move_and_result(list_of_moves):
    new_line_of_moves = []
    for line in list_of_moves:
        new_line_of_moves.append([line[4], int(line[3])])
    return new_line_of_moves


def get_best_start(list_of_moves):
    maximum = 0
    best_start = ""
    for line in list_of_moves:
        if line[1] > maximum:
            best_start = line[0]
            maximum = line[1]

    return best_start


def get_worse_start(list_of_moves):
    maximum = 0
    worse_start = ""
    for line in list_of_moves:
        if line[2] > maximum:
            worse_start = line[0]
            maximum = line[2]

    return worse_start


def get_start_most_draws(list_of_moves):
    maximum = 0
    drawed_start = ""
    for line in list_of_moves:
        if line[3] > maximum:
            drawed_start = line[0]
            maximum = line[3]

    return drawed_start


def get_most_used_start(list_of_moves):
    maximum = 0
    most_used_start = ""
    for line in list_of_moves:
        if (line[1] + line[2] + line[3]) > maximum:
            most_used_start = line[0]
            maximum = (line[1] + line[2] + line[3])

    return most_used_start


the_list_of_moves = open_csv(csv_path_in)
the_list_of_moves = list_to_move_and_result(the_list_of_moves)
the_list_of_moves = analyse_moves(the_list_of_moves)
print(the_list_of_moves)
print("Best start :", get_best_start(the_list_of_moves))
print("Most draws start :", get_start_most_draws(the_list_of_moves))
print("Worse start :", get_worse_start(the_list_of_moves))
print("Most used start :", get_most_used_start(the_list_of_moves))
