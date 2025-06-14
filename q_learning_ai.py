import random
import pickle

class QLearningAgent:
    def __init__(self, alpha=0.3, gamma=0.9, epsilon=0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_state(self, board):
        return tuple(board)

    def choose_action(self, game, player):
        state = self.get_state(game.board)
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(game.available_moves())
        else:
            q_values = [self.q_table.get((state, a), 0) for a in game.available_moves()]
            max_q = max(q_values)
            max_actions = [a for a in game.available_moves() if self.q_table.get((state, a), 0) == max_q]
            return random.choice(max_actions)

    def update_q_value(self, old_state, action, reward, new_state):
        old_q = self.q_table.get((old_state, action), 0)
        future_q = max([self.q_table.get((new_state, a), 0) for a in range(9)], default=0)
        self.q_table[(old_state, action)] = old_q + self.alpha * (reward + self.gamma * future_q - old_q)

    def save(self, filename='q_table.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load(self, filename='q_table.pkl'):
        with open(filename, 'rb') as f:
            self.q_table = pickle.load(f)
