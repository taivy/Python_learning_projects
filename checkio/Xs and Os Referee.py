from typing import List


def checkio(game_result):
    result = None
    if (game_result[0][0] == game_result[1][1] == game_result[2][2] or game_result[0][2] == game_result[1][1] ==
        game_result[2][0]) and game_result[1][1] != '.':
        result = game_result[1][1]
    else:
        for i in range(3):
            if game_result[i][0] == game_result[i][1] == game_result[i][2] and game_result[i][1] != '.':
                result = game_result[i][1]
            elif game_result[0][i] == game_result[1][i] == game_result[2][i] and game_result[1][i] != '.':
                result = game_result[1][i]
    if result is None:
        result = 'D'
    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"