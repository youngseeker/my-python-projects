import random

def player(prev_play, opponent_history=[]):
    # Initialize a dictionary to keep track of opponent's most common moves
    opponent_moves = {'R': 0, 'P': 0, 'S': 0}
    
    # Update opponent's move history
    if prev_play:
        opponent_moves[prev_play] += 1
    
    # Define our strategies based on opponent's history
    if len(opponent_history) < 20:
        # Start with random moves
        return random.choice(['R', 'P', 'S'])
    else:
        # Determine opponent's most common move
        common_move = max(opponent_moves, key=opponent_moves.get)
        
        # Counter-strategy: Play the move that beats opponent's most common move
        if common_move == 'R':
            return 'P'
        elif common_move == 'P':
            return 'S'
        else:
            return 'R'
