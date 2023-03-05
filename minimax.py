from game import Game
from math import inf


game = Game("X", "O")
first_or_not = input("Enter F or first or S for second: ").lower()


def minimax(interface, ismaximising, depth) -> int:
    if (winner := interface.check_winner(not ismaximising)) != 69: # 69 means no winner yet
        return winner, depth

    if not ismaximising:
        best_score = inf
        all_moves = get_all_moves(interface)
        for move in all_moves:
            interface.play_turn(move, ismaximising)
            score, depth = minimax(interface, not ismaximising, depth + 1)
            interface.undo_move(move)
            best_score = min(best_score, score)
        return best_score, depth
    else:
        best_score = -inf
        all_moves = get_all_moves(interface)
        for move in all_moves:
            interface.play_turn(move, ismaximising)
            score, depth = minimax(interface, not ismaximising, depth + 1)
            interface.undo_move(move)
            best_score = max(best_score, score)
        return best_score, depth


def get_all_moves(interface):
    possible_moves = []
    for num, square in interface.board.items():
        if square == " ":
            possible_moves.append(int(num))
    return possible_moves


def get_best_move(interface, player):
    best_move = None
    best_score = inf
    shortest_depth = inf
    for move in get_all_moves(interface):
        interface.play_turn(move, player)
        score, depth = minimax(interface, not player, 0)
        if score <= best_score:
            if depth < shortest_depth: # if the move is the shortest win/draw and its score is good enough (<= score)
                best_score = score
                best_move = move
        # Testing print statement
        # print(f"Move = {move}, Score = {score}, Depth = {depth}")
        interface.undo_move(move)
    return best_move


player = False
if first_or_not == "f":
    player = True
    game.print_board()

while get_all_moves(game):
    if player:
        square = int(input("Enter your Move: "))
    else:
        print("Computer Plays its move")
        square = get_best_move(game, player)
    assert 0 < square < 10  # square is between 1 and 10
    game.play_turn(square, player)
    if (winner := game.check_winner(player)) != 69:  # if 69 then no winner yet
        if winner == 1:
            print("Player wins!")
        elif winner == 0:
            print("Tie!")
        else:
            print("Computer wins!")
        game.print_board()
        break
    player = not player
    game.print_board()
