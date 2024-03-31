from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def __eq__(self, other):
        return (self.missionaries, self.cannibals, self.boat) == (other.missionaries, other.cannibals, other.boat)

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def is_valid_state(state):
    return 0 <= state.missionaries <= 3 and 0 <= state.cannibals <= 3 and (state.missionaries >= state.cannibals or state.missionaries == 0) and (3 - state.missionaries >= 3 - state.cannibals or state.missionaries == 3)

def generate_next_states(current_state):
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
    next_states = []
    for move in moves:
        if current_state.boat == 'left':
            next_state = State(current_state.missionaries - move[0], current_state.cannibals - move[1], 'right')
        else:
            next_state = State(current_state.missionaries + move[0], current_state.cannibals + move[1], 'left')
        if is_valid_state(next_state):
            next_states.append(next_state)
    return next_states

def solve_missionaries_cannibals():
    initial_state = State(3, 3, 'left')
    goal_state = State(0, 0, 'right')

    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]

        if current_state not in visited:
            visited.add(current_state)
            next_states = generate_next_states(current_state)
            for next_state in next_states:
                queue.append((next_state, path + [current_state]))

    return None

def print_solution(path):
    if path is None:
        print("No solution found.")
        return

    print("Solution path:")
    for state in path:
        print(state.missionaries, state.cannibals, state.boat)

# Solve the problem
solution_path = solve_missionaries_cannibals()
print_solution(solution_path)
