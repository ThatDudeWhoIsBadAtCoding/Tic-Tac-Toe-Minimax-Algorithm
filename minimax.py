from game import Game
from math import inf


game = Game("X", "O")
first_or_not = input("Enter F or first or S for second: ").lower()


def minimax(interface: Game, ismaximising: bool, depth: int) -> int:
    if (winner := interface.check_winner(not ismaximising)) != 69:
        return winner, depth
    # toggle best score depending on if its maxmising players turn
    best_score = -inf if ismaximising else inf
    all_moves = get_all_moves(interface)
    for move in all_moves:
        interface.play_turn(move, ismaximising)
        score, depth = minimax(interface, not ismaximising, depth + 1)
        interface.undo_move(move)
        best_score = max(best_score, score) if ismaximising else min(best_score, score)
    return best_score, depth


def get_all_moves(interface: Game) -> list[int]:
    possible_moves = []
    for num, square in interface.board.items():
        if square == " ":
            possible_moves.append(int(num))
    return possible_moves


def get_best_move(interface: Game, player: bool) -> int:
    best_move = None
    best_score = inf
    shortest_depth = inf
    for move in get_all_moves(interface):
        interface.play_turn(move, player)
        score, depth = minimax(interface, not player, 0)
        if score <= best_score:
            if depth < shortest_depth:
                best_score = score
                best_move = move
        print(f"Move = {move}, Score = {score}, Depth = {depth}")
        interface.undo_move(move)
    return best_move


player = False  # False = computer plays first, else human plays first

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
            print("Human wins!")
        elif winner == -1:
            print("Computer wins!")
        else:
            print("Draw!")
        game.print_board()
        break
    player = not player  # if True then make it false, vice versa
    game.print_board()
