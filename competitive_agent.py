import random


class CompetitiveQAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)

        q_values = [self.get_q(state, action) for action in self.actions]
        max_q = max(q_values)
        best_actions = [a for a, q in zip(self.actions, q_values) if q == max_q]
        return random.choice(best_actions)

    def update(self, state, action, reward, next_state):
        current_q = self.get_q(state, action)
        future_q = max([self.get_q(next_state, a) for a in self.actions], default=0.0)

        new_q = current_q + self.alpha * (reward + self.gamma * future_q - current_q)
        self.q_table[(state, action)] = new_q