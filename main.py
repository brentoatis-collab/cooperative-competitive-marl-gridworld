from training import train_cooperative, train_competitive
from metrics import summarize_metrics
from visualization import plot_training_curves, plot_agent_paths


def main():
    print("Starting Multi-Agent RL Simulation...\n")

    coop_rewards, coop_steps, coop_paths = train_cooperative(episodes=300)
    comp_rewards, comp_steps, comp_paths = train_competitive(episodes=300)

    coop_summary = summarize_metrics(coop_rewards, coop_steps)
    comp_summary = summarize_metrics(comp_rewards, comp_steps)

    print("Cooperative Summary")
    print(coop_summary)
    print()

    print("Competitive Summary")
    print(comp_summary)
    print()

    plot_training_curves(coop_rewards, comp_rewards, coop_steps, comp_steps)
    plot_agent_paths(coop_paths, title="Cooperative Agent Paths")
    plot_agent_paths(comp_paths, title="Competitive Agent Paths")


if __name__ == "__main__":
    main()