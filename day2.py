GAME_OUTCOMES = {
        ('A', 'R'): 1 + 3,
        ('A', 'P'): 2 + 6,
        ('A', 'S'): 3 + 0,
        ('B', 'R'): 1 + 0,
        ('B', 'P'): 2 + 3,
        ('B', 'S'): 3 + 6,
        ('C', 'R'): 1 + 6,
        ('C', 'P'): 2 + 0,
        ('C', 'S'): 3 + 3,
    }

LOSS = {'A': 'S', 'B': 'R', 'C': 'P'}
WIN = {'A': 'P', 'B': 'S', 'C': 'R'}
TIE = {'A': 'R', 'B': 'P', 'C': 'S'}

def parse_inputs(filename):
    with open(filename) as f:
        return [line.split() for line in f]


def play_the_game(inputs):
    points = 0
    for play in inputs:
        points += game(play)
    return points


def game(plays):
    them = plays[0]
    me = plays[1]
    
    if me == 'X':
        me = LOSS[them]
    elif me == 'Y':
        me = TIE[them]
    else:
        me = WIN[them]

    game = (them, me)

    if game in GAME_OUTCOMES:
        points = GAME_OUTCOMES[game]
    else:
        points = None

    return points