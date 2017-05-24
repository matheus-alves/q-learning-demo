import random
from enum import Enum

from gui import gridinfo


# Enum to hold all possible actions
class Actions(Enum):
    up = 1
    down = 2
    left = 3
    right = 4


# State representation class
class State():
    def __init__(self, row, col):
        self.row = row
        self.col = col


# Dictionary to store the Q-learning values
_q_values = dict()

# List to store the best path found
_results = list()

# Constants
_NUM_OF_EPISODES = 250
_EPSILON = 0.05
_ALPHA = 0.1
_GAMMA = 0.9


def setup_q_learning():
    """
    Sets the algorithm up, setting the default values for each Q-state
    """
    for row in range(0, gridinfo.NUM_OF_ROWS):
        for col in range(0, gridinfo.NUM_OF_COLUMNS):
            state = State(row, col)

            for action in Actions:
                q = (state.row, state.col, action)
                _q_values[q] = 0


def validate_results(temp_results):
    """
    Validates the latest results
    """
    global _results

    if len(_results) > 0:
        # Checks if this solution contains the goal
        if (_results[-1][0] == gridinfo.GOAL[0]) and \
                (_results[-1][1] == gridinfo.GOAL[1]):
            if (temp_results[-1][0] == gridinfo.GOAL[0]) and \
                    (temp_results[-1][1] == gridinfo.GOAL[1]):
                if len(temp_results) < len(_results):
                    # Found a better solution up to the goal
                    _results = temp_results

        # Since the oldest solution didn't have the goal,
        # simply update if the new one has or if it is bigger
        elif (temp_results[-1][0] == gridinfo.GOAL[0]) and \
                (temp_results[-1][1] == gridinfo.GOAL[1]):
            _results = temp_results
        elif len(temp_results) > len(_results):
            _results = temp_results
    else:
        _results = temp_results


def explore(curr_state):
    """
    Defines the next action to take
    """
    rand = random.random()

    # Checks if should select randomly or using the q-values
    if rand <= _EPSILON:
        return random.choice(list(Actions))
    else:
        best = list()

        best_action = Actions.up  # init as any action
        best_value = -10000000  # very low value to init

        for action in Actions:
            q = (curr_state.row, curr_state.col, action)

            if _q_values[q] > best_value:
                best_action = action
                best_value = _q_values[q]

        best.append(best_action)

        # Checks for duplicates
        for action in Actions:
            q = (curr_state.row, curr_state.col, action)

            if action != best_action:
                if _q_values[q] == best_value:
                    best.append(action)

        return random.choice(best)


def move(curr_state, action):
    """
    Moves the agent and returns its new state
    """
    new_state = State(curr_state.row, curr_state.col)

    # Checks for the borders
    if action == Actions.up:
        if (new_state.row - 1) >= 0:
            new_state.row -= 1
    elif action == Actions.down:
        if (new_state.row + 1) <= (gridinfo.NUM_OF_ROWS - 1):
            new_state.row += 1
    elif action == Actions.left:
        if (new_state.col - 1) >= 0:
            new_state.col -= 1
    elif action == Actions.right:
        if (new_state.col + 1) <= (gridinfo.NUM_OF_COLUMNS - 1):
            new_state.col += 1

    return new_state


def update(curr_state, last_action):
    """
    Updates the q_learning values and the state
    """
    q = (curr_state.row, curr_state.col, last_action)

    new_state = move(curr_state, last_action)
    position = (new_state.row, new_state.col)

    reward = -1
    if position == gridinfo.GOAL:
        reward = 0
    elif position in gridinfo.PENALTY:
        reward = -100

    # Updates Q
    old_value = _q_values[q]
    max_new = \
        max([_q_values[(new_state.row, new_state.col, a)] for a in Actions])
    _q_values[q] = old_value + _ALPHA * \
        (reward + (_GAMMA * max_new) - old_value)

    # Moves to the new state
    curr_state.row = new_state.row
    curr_state.col = new_state.col


def find_results():
    """
    Starts the result finding loop
    """
    temp_results = list()
    curr_state = State(gridinfo.START[0], gridinfo.START[1])

    ended = False
    while not ended:
        last_action = explore(curr_state)
        q = (curr_state.row, curr_state.col, last_action)
        temp_results.append(q)

        update(curr_state, last_action)
        position = (curr_state.row, curr_state.col)

        if (position[0] == gridinfo.GOAL[0]) and \
                (position[1] == gridinfo.GOAL[1]):
            q = (curr_state.row, curr_state.col, last_action)
            temp_results.append(q)
            ended = True
        else:
            for penalty in gridinfo.PENALTY:
                if (position[0] == penalty[0]) and \
                        (position[1] == penalty[1]):
                    q = (curr_state.row, curr_state.col, last_action)
                    temp_results.append(q)
                    ended = True
                    break

    return temp_results


def get_q_values():
    """
    Helper method to access the calculated q-values
    """
    return _q_values


def apply_q_learning(num_of_episodes):
    """
    Calculates Q-learning using the provided number of episodes
    """
    print('Applying Q-learning')
    global _NUM_OF_EPISODES

    # Checks if the user has set the number of episodes
    if num_of_episodes > 0:
        _NUM_OF_EPISODES = num_of_episodes

    setup_q_learning()

    print('Number of episodes: ' + str(_NUM_OF_EPISODES))

    # Q-learning loop
    while _NUM_OF_EPISODES > 0:
        validate_results(find_results())
        _NUM_OF_EPISODES -= 1

    return _results
