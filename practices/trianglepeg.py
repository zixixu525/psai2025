def create_triangle(rows, empty_index=None):
    triangle = []
    count = 0
    for i in range(rows):
        row = []
        for j in range(i + 1):
            if empty_index is not None and count == empty_index:
                row.append(0)
            else:
                row.append('#')
            count += 1
        triangle.append(row)
    return triangle

from collections import defaultdict


ALL_MOVES={
    0:(3,1,0),
    1:(0,1,3),
    2:(6,3,1),
    3:(1,3,6),
    4:(10,6,3),
    5:(3,6,10),
    6:(11,7,4),
    7:(4,7,11),
    8:(7,4,2),
    9:(2,4,7),
    10:(12,8,5),
    11:(5,8,12)
}

def print_state(state, rows):
    count = 0
    for i in range(rows):
        row = []
        for j in range(i + 1):
            row.append('#' if state[count] == 1 else '0')
            count += 1
        # Center the row for triangle shape
        print(' '.join(row).center(rows * 2 - 1))

def is_valid_move(move_id,mini_state):
    move=ALL_MOVES[move_id]
    if mini_state[0]==1 and mini_state[1]==1 and mini_state[2]==0:
        return True
    return False

def apply_move(move_id,state):
    new_state=state.copy()
    move=ALL_MOVES[move_id]
    new_state[move[0]]=0
    new_state[move[1]]=0
    new_state[move[2]]=1
    return new_state

def get_successors(state):
    possible_moves = defaultdict(list)
    symmetric_states = [state, rotate120(state), rotate120(state)]
    # get possible moves for each symmetric state
    for move_id, move in ALL_MOVES.items():
        for s_idx, _state in enumerate(symmetric_states):
            mini_state = [state[idx] for idx in move]
            if is_valid_move(move_id, mini_state):
                possible_moves[s_idx].append(move_id)
    # apply possible moves to each symmetric state
    next_states = []
    for s, move_ids in possible_moves.items():
        for move_id in move_ids:
            new_state = apply_move(move_id, state)
            next_states.append(new_state)
    return next_states
             
          

def get_adjacent_pegs(idx):
    pass


def rotate120(a):
    mapping={
        0:14,
        1:9,
        2:13,
        3:5,
        4:8,
        5:12,
        6:2,
        7:4,
        8:7,
        9:11,
        10:0,
        11:1,
        12:3,
        13:6,
        14:10
    }
    a.copy=a.copy()
    a=[0]*len(a)
    for i in range(len(a)):
        a[i]=a_copy[mapping[i]]
    return a

def main_argparse():
    pass

def main_input():
    initial=[0 for _ in range(15)]
    initial[0]=0
    #a=input('pass in all indices that are preppared (space delimited:').strip()
    #a=[int(item.strip()) for item in a.split()]
    #for i in a:
    #    initial[i]=1
   
   

if __name__ == "__main__":
    # main_argparse()
    main_input()