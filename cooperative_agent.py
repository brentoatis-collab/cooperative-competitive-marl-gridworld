import random


class CooperativeQAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_q(self, state, joint_action):
        return self.q_table.get((state, joint_action), 0.0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return (random.choice(self.actions), random.choice(self.actions))

        best_action = None
        best_value = float("-inf")

        for a0 in self.actions:
            for a1 in self.actions:
                joint_action = (a0, a1)
                q_value = self.get_q(state, joint_action)
                if q_value > best_value:
                    best_value = q_value
                    best_action = joint_action

        if best_action is None:
            return (random.choice(self.actions), random.choice(self.actions))
        return best_action

    def update(self, state, joint_action, reward, next_state):
        current_q = self.get_q(state, joint_action)

        future_q = max(
            [self.get_q(next_state, (a0, a1)) for a0 in self.actions for a1 in self.actions],
            default=0.0
        )

        new_q = current_q + self.alpha * (reward + self.gamma * future_q - current_q)
        self.q_table[(state, joint_action)] = new_q