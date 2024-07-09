import numpy as np
import random

ACTIONS = ["R", "P", "S"]
STATE_SIZE = 3  # Number of opponent's past actions to consider as the state
LEARNING_RATE = 0.1
GAMMA = 0.3
EPSILON_START = 0.8
EPSILON_END = 0.1
EPSILON_DECAY = 0.1
LAST_ACTION = None

Q_table = {}


def get_action_index(action):
    return ACTIONS.index(action)


def reward_function(agent_action, opponent_action):
    if agent_action == opponent_action:
        return 0  # Tie
    elif (
        (agent_action == "R" and opponent_action == "S")
        or (agent_action == "S" and opponent_action == "P")
        or (agent_action == "P" and opponent_action == "R")
    ):
        return 5  # Win
    else:
        return -3  # Lose


def get_state(opponent_history):
    if len(opponent_history) < STATE_SIZE:
        state = tuple(
            random.choices(ACTIONS, k=STATE_SIZE - len(opponent_history))
            + opponent_history
        )
    else:
        state = tuple(opponent_history[-STATE_SIZE:])
    return state


def update_q_table(state, action, reward, next_state):
    if state not in Q_table:
        Q_table[state] = np.zeros(len(ACTIONS))
    if next_state not in Q_table:
        Q_table[next_state] = np.zeros(len(ACTIONS))

    Q_table[state][action] += LEARNING_RATE * (
        reward + GAMMA * np.max(Q_table[next_state]) - Q_table[state][action]
    )


def player(prev_play, opponent_history=[]):
    global LAST_ACTION, LAST_STATE, Q_table, EPSILON_START

    epsilon = max(EPSILON_END, EPSILON_START * EPSILON_DECAY)

    if prev_play:
        opponent_history.append(prev_play)

    state = get_state(opponent_history)

    if random.uniform(0, 1) < epsilon:
        action = random.choice(ACTIONS)
    else:
        if state not in Q_table:
            Q_table[state] = np.zeros(len(ACTIONS))
        action = ACTIONS[np.argmax(Q_table[state])]

    if LAST_ACTION is not None and prev_play:
        next_state = get_state(opponent_history)
        reward = reward_function(ACTIONS[LAST_ACTION], prev_play)
        update_q_table(LAST_STATE, LAST_ACTION, reward, next_state)

    LAST_ACTION = get_action_index(action)
    LAST_STATE = state

    return action
