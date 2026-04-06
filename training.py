from environment import GridWorldEnv
from cooperative_agent import CooperativeQAgent
from competitive_agent import CompetitiveQAgent


def train_cooperative(episodes=500):
    env = GridWorldEnv(mode="cooperative")
    agent = CooperativeQAgent(actions=env.actions)

    rewards_per_episode = []
    steps_per_episode = []
    paths_last_episode = []

    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0
        step_count = 0
        current_path = [state]

        while not done:
            joint_action = agent.choose_action(state)
            next_state, rewards, done = env.step(joint_action)

            shared_reward = sum(rewards) / 2
            agent.update(state, joint_action, shared_reward, next_state)

            state = next_state
            total_reward += shared_reward
            step_count += 1
            current_path.append(state)

        rewards_per_episode.append(total_reward)
        steps_per_episode.append(step_count)

        if episode == episodes - 1:
            paths_last_episode = current_path

    return rewards_per_episode, steps_per_episode, paths_last_episode


def train_competitive(episodes=500):
    env = GridWorldEnv(mode="competitive")
    agent_0 = CompetitiveQAgent(actions=env.actions)
    agent_1 = CompetitiveQAgent(actions=env.actions)

    rewards_per_episode = []
    steps_per_episode = []
    paths_last_episode = []

    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0
        step_count = 0
        current_path = [state]

        while not done:
            action_0 = agent_0.choose_action(state[0])
            action_1 = agent_1.choose_action(state[1])

            next_state, rewards, done = env.step((action_0, action_1))

            agent_0.update(state[0], action_0, rewards[0], next_state[0])
            agent_1.update(state[1], action_1, rewards[1], next_state[1])

            state = next_state
            total_reward += sum(rewards)
            step_count += 1
            current_path.append(state)

        rewards_per_episode.append(total_reward)
        steps_per_episode.append(step_count)

        if episode == episodes - 1:
            paths_last_episode = current_path

    return rewards_per_episode, steps_per_episode, paths_last_episode