import matplotlib.pyplot as plt


def plot_training_curves(coop_rewards, comp_rewards, coop_steps, comp_steps):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(coop_rewards, label="Cooperative Rewards")
    plt.plot(comp_rewards, label="Competitive Rewards")
    plt.title("Reward per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(coop_steps, label="Cooperative Steps")
    plt.plot(comp_steps, label="Competitive Steps")
    plt.title("Steps per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Steps")
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_agent_paths(path_data, title="Agent Paths"):
    plt.figure(figsize=(6, 6))

    agent0_x = [state[0][1] for state in path_data]
    agent0_y = [state[0][0] for state in path_data]

    agent1_x = [state[1][1] for state in path_data]
    agent1_y = [state[1][0] for state in path_data]

    plt.plot(agent0_x, agent0_y, marker="o", label="Agent 0")
    plt.plot(agent1_x, agent1_y, marker="s", label="Agent 1")

    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.title(title)
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.legend()
    plt.show()