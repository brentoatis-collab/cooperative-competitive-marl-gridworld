def summarize_metrics(rewards_per_episode, steps_per_episode):
    avg_reward = sum(rewards_per_episode) / len(rewards_per_episode)
    avg_steps = sum(steps_per_episode) / len(steps_per_episode)

    return {
        "average_reward": round(avg_reward, 2),
        "average_steps": round(avg_steps, 2),
        "total_reward": round(sum(rewards_per_episode), 2),
        "best_reward": round(max(rewards_per_episode), 2),
        "worst_reward": round(min(rewards_per_episode), 2),
    }