from tic_tac_toe import TicTacToe
from q_learning_ai import QLearningAgent

def train(agent, episodes=50000):
    game = TicTacToe()
    for episode in range(episodes):
        game.reset()
        current_player = 'X'

        while game.empty_squares():
            state = agent.get_state(game.board)
            action = agent.choose_action(game, current_player)
            game.make_move(action, current_player)
            new_state = agent.get_state(game.board)

            if game.current_winner == current_player:
                reward = 1
                agent.update_q_value(state, action, reward, new_state)
                break
            elif not game.empty_squares():
                reward = 0.5
                agent.update_q_value(state, action, reward, new_state)
                break
            else:
                reward = 0
                agent.update_q_value(state, action, reward, new_state)

            current_player = 'O' if current_player == 'X' else 'X'

        if episode % 1000 == 0:
            print(f"Episode {episode}")
    agent.save()

if __name__ == "__main__":
    agent = QLearningAgent()
    train(agent)
