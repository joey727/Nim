import random


def train(seed=0):
    random.seed(seed)
    # Q-learning parameters
    alpha = 0.7    # learning rate
    gamma = 0.9    # discount factor
    epsilon = 0.2  # exploration rate

    # Q-table: state (sticks left) -> action (sticks to take) -> value
    Q = {s: {a: 0.0 for a in range(1, 4) if a <= s} for s in range(1, 21)}

    # Train over many simulated games
    for episode in range(100000):
        total = 15
        states_actions = []
        while total > 0:
            # Epsilon-greedy action selection
            if random.random() < epsilon:
                action = random.choice([a for a in range(1, 4) if a <= total])
            else:
                qvals = Q[total]
                max_q = max(qvals.values())
                best_actions = [a for a, v in qvals.items() if v == max_q]
                action = random.choice(best_actions)
            states_actions.append((total, action))
            total -= action
            if total == 0:
                reward = -1  # AI loses
                break
            # Opponent (random)
            opp_action = random.choice([a for a in range(1, 4) if a <= total])
            total -= opp_action
            if total == 0:
                reward = 1  # AI wins
                break
        # Q-learning update
        for i, (state, action) in enumerate(states_actions):
            if i == len(states_actions) - 1:
                Q[state][action] += alpha * (reward - Q[state][action])
            else:
                next_state = states_actions[i + 1][0]
                max_next_q = max(Q[next_state].values())
                Q[state][action] += alpha * \
                    (gamma * max_next_q - Q[state][action])

    def ai_move(remaining):
        qvals = Q[remaining]
        max_q = max(qvals.values())
        best_actions = [a for a, v in qvals.items() if v == max_q]
        return random.choice(best_actions)

    return ai_move
