def part1():
    player_1 = 10
    player_2 = 1

    player_1_rolls = 0
    player_2_rolls = 0

    player_1_score = 0
    player_2_score = 0

    turn_one = True
    dice = 1
    rolls = 0
    turn = 1
    while player_1_score < 1000 and player_2_score < 1000:
        rolls += 3
        spaces = 0

        for i in range(3):
            spaces += dice
            dice += 1
            if dice > 100:
                dice = 1
        print("Turno:", turn, "Tiradas:", dice-3, dice-2, dice-1, "Espacios:", spaces)


        if turn_one:
            player_1 = (player_1 + spaces) % 10
            if player_1 == 0:
                player_1 = 10
            player_1_rolls += 3
            player_1_score += player_1
            print("     Score Player1:", player_1_score)
            turn_one = False
        else:
            player_2 = (player_2 + spaces) % 10
            if player_2 == 0:
                player_2 = 10
            player_2_rolls += 3
            player_2_score += player_2
            print("     Score Player2:", player_2_score)
            turn_one = True
        turn += 1
    print(player_1_score, player_2_score, rolls)
    print(player_2_score, player_2_rolls)
    print(player_2_score * (player_1_rolls+player_2_rolls))


def part2():
    init, goal, won = (10, 1, 0, 0), 21, [0, 0]
    adds = [z + y + x for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)]
    perms = {a: adds.count(a) for a in adds}
    states = {(x, y, z, w): 0 for x in range(1, 11) for y in range(1, 11) for z in range(0, goal) for w in
              range(0, goal)}
    states[init] = 1
    while not max(states.values()) == 0:
        for state, value in states.items():
            if value > 0:
                for p, n in perms.items():  # player 1
                    for q, m in perms.items():  # try player 2 as well
                        pos = [(state[0] + p - 1) % 10 + 1, (state[1] + q - 1) % 10 + 1]
                        new = tuple(pos + [state[2] + pos[0], state[3] + pos[1]])
                        if max(new[2:]) < goal:  # neither player has won
                            states[new] += value * n * m
                        elif new[3] >= goal and new[2] < goal:  # player 2 won
                            won[1] += value * m * n
                    if new[2] >= goal:  # player 1 won before player 2 even played
                        won[0] += value * n
                states[state] = 0
    print(max([won[0], won[1]]))


def parallel_universe(player_1_score, player_2_score, player_1, player_2, turn):
    one_count = 0
    two_count = 0
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                spaces = i + j + k
                if turn:
                    player_1 = (player_1 + spaces) % 10
                    if player_1 == 0:
                        player_1 = 10
                    player_1_score += player_1
                    if player_1_score > 21:
                        one_count = 0
                else:
                    player_2 = (player_2 + spaces) % 10
                    if player_2 == 0:
                        player_2 = 10
                    player_2_score += player_2
                    if player_2_score > 21:
                        return 0, 1
                    else:
                        one, two = next_turn(player_1_score, player_2_score, player_1, player_2, True)

    print()

if __name__ == "__main__":
    part1()
    part2()
