Project Objective

Design a multi-agent reinforcement learning system comparing cooperative and competitive behaviors in a shared GridWorld.

⸻

Phase 1: Environment Design (Initial Prompt)

Prompt:

Create a GridWorld where two agents operate simultaneously with independent actions. Track positions, include obstacles, and define goal states.

Outcome:
	•	Built shared environment (environment.py)
	•	Two agents initialized at different positions
	•	Obstacles and goal states defined

Iteration Insight:
Initially, movement logic did not properly constrain agents within bounds. Adjusted _move() to enforce grid limits.

⸻

Phase 2: Structuring the Codebase

Prompt:

Organize the project into modular files for scalability.

Outcome:
	•	environment.py
	•	cooperative_agent.py
	•	competitive_agent.py
	•	training.py
	•	metrics.py
	•	visualization.py

Insight:
Separating logic improved debugging and allowed independent tuning of cooperative vs competitive strategies.

⸻

Phase 3: Cooperative Agent Design

Prompt:

Design a cooperative agent where both agents receive shared rewards when goals are reached.

Initial Behavior:
	•	Agents struggled to coordinate
	•	High step counts
	•	Negative reward accumulation

Adjustment:
	•	Modified reward structure:
	•	Shared reward only when both agents reach goals
	•	Penalty for delay

Insight:
Cooperation introduces synchronization dependency, making learning slower and less efficient.

⸻

Phase 4: Competitive Agent Design

Prompt:

Modify reward structure so agents compete and maximize individual rewards.

Outcome:
	•	Independent reward signals
	•	Faster convergence
	•	Reduced episode length

Emergent Behavior:
Agents learned direct paths without coordination overhead.

Insight:
Competition simplifies optimization by removing dependency between agents.

⸻

Phase 5: Training & Metrics

Prompt:

Track performance metrics including reward, steps, and agent paths.

Metrics Implemented:
	•	Task completion time (steps)
	•	Strategy efficiency (avg steps)
	•	Reward distribution

Results:
	•	Cooperative:
	•	Avg Reward: -20.29
	•	Avg Steps: 25.26
	•	Competitive:
	•	Avg Reward: 3.07
	•	Avg Steps: 5.44

⸻

Phase 6: Visualization & Analysis

Prompt:

Visualize training curves and agent paths.

Outcome:
	•	Reward curves show slow cooperative learning
	•	Competitive agents converge quickly
	•	Path plots show:
	•	Cooperative → hesitant movement
	•	Competitive → direct movement

⸻

Key Concept: Reward Structure Drives Learning
	•	Cooperative learning:
	•	Requires alignment
	•	Slower convergence
	•	Higher complexity
	•	Competitive learning:
	•	Independent optimization
	•	Faster convergence
	•	Efficient strategies

⸻

Final Reflection (Vibe Coding Insight)

Using Claude Code enabled:
	•	Rapid environment design
	•	Iterative refinement of reward systems
	•	Modular code structure
	•	Efficient debugging across multiple files

The biggest takeaway:

Small changes in reward structure produce fundamentally different agent behaviors.
