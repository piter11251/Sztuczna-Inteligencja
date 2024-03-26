from collections import deque

ACTIONS = ['ruszaj w lewo', 'ruszaj w prawo', 'ssać']

def Action(state):
    return ACTIONS

def Result(state, action):
    if action == 'ruszaj w lewo':
        return 'B', action
    elif action == 'ruszaj w prawo':
        return 'A', action
    elif action == 'ssać':
        return state, action

# Stan początkowy
start_state = 'A'

# Stan celu
goal_state = 'clean'

# Funkcja sprawdzająca czy stan jest celem
def is_goal(state):
    return state == goal_state

# Algorytm BFS
def bfs(start_state):
    frontier = deque([start_state])
    explored = set()

    while frontier:
        state = frontier.popleft()
        if is_goal(state):
            return True
        explored.add(state)
        for action in Action(state):
            next_state, action_taken = Result(state, action)
            if next_state not in explored and next_state not in frontier:
                print(f"Akcja: {action_taken}, Stan: {next_state}")
                frontier.append(next_state)
    return False

# Wywołanie algorytmu BFS
bfs(start_state)


import math

# Funkcja reprezentująca stan gry - tutaj dla uproszczenia używamy wartości liczbowych
def game_state():
    return 0

def possible_moves(state):
    return [1, 2, 3]

def game_result(state):
    return state

def max_min_alpha_beta(state, alpha, beta, maximizing_player):
    if game_result(state) != 0 or len(possible_moves(state)) == 0:
        return game_result(state)

    if maximizing_player:
        value = -math.inf
        for move in possible_moves(state):
            value = max(value, max_min_alpha_beta(state + move, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        for move in possible_moves(state):
            value = min(value, max_min_alpha_beta(state + move, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

# Wywołanie algorytmu dla stanu początkowego
optimal_value = max_min_alpha_beta(game_state(), -math.inf, math.inf, True)
print("Optymalna wartość dla MAX:", optimal_value)

from heapq import heappush, heappop

# Stan początkowy i docelowy
start_state = [[None, 1, 3],
               [4, 2, 5],
               [7, 8, 6]]

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, None]]


# Funkcja zwracająca współrzędne danego elementu w stanie
def find_element(state, element):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == element:
                return i, j


# Funkcja obliczająca odległość Manhattan
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Funkcja obliczająca funkcję heurystyczną dla danego stanu
def heuristic(state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] is not None:
                goal_position = find_element(goal_state, state[i][j])
                distance += manhattan_distance((i, j), goal_position)
    return distance


# Implementacja algorytmu A*
def a_star(start_state):
    frontier = [(heuristic(start_state), 0, start_state, [])]
    explored = set()

    while frontier:
        _, cost, current_state, path = heappop(frontier)
        if current_state == goal_state:
            return path
        explored.add(tuple(map(tuple, current_state)))

        empty_position = find_element(current_state, None)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # ruchy: prawo, lewo, dół, góra

        for move in moves:
            new_position = (empty_position[0] + move[0], empty_position[1] + move[1])

            if 0 <= new_position[0] < len(current_state) and 0 <= new_position[1] < len(current_state[0]):
                new_state = [row.copy() for row in current_state]
                new_state[empty_position[0]][empty_position[1]], new_state[new_position[0]][new_position[1]] = \
                    new_state[new_position[0]][new_position[1]], new_state[empty_position[0]][empty_position[1]]

                if tuple(map(tuple, new_state)) not in explored:
                    new_cost = cost + 1
                    heappush(frontier, (new_cost + heuristic(new_state), new_cost, new_state, path + [new_state]))


# Wywołanie algorytmu A* i wydrukowanie sekwencji ruchów
path = a_star(start_state)
if path:
    for i, state in enumerate(path):
        print(f"Krok {i + 1}:")
        for row in state:
            print(row)
        print()
    print("Osiągnięto cel!")
else:
    print("Nie udało się znaleźć rozwiązania.")
