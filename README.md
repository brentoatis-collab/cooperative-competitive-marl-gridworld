# Multi-Agent Reinforcement Learning in GridWorld  
**Cooperative vs Competitive Agent Design**
Author: Brent Oatis  
Course: CST 643 – Week 3  
Assignment: Multi-Agent Reinforcement Learning
---

## Overview

This project explores how reward structures influence behavior in multi-agent reinforcement learning (MARL). Two agents operate within a shared GridWorld environment under two distinct paradigms:

- **Cooperative Learning** – Agents collaborate to achieve shared success  
- **Competitive Learning** – Agents optimize independently for individual gain  

The objective is to analyze how coordination vs independence affects performance, efficiency, and emergent strategies.

---

## Environment Design

- Grid Size: 5 × 5  
- Agents: 2 (independent movement)  
- Obstacles: Fixed positions  
- Goals: Unique per agent  

### Actions:
- Up  
- Down  
- Left  
- Right  
- Stay  

The environment tracks:
- Agent positions  
- Collisions  
- Goal completion  
- Episode termination  

---

## Agent Architectures

### Cooperative Agent (Multi-Agent Q-Learning)

- Shared reward system  
- Success requires **both agents reaching goals**  
- Encourages coordination and synchronization  

**Key Challenge:**  
Coordination overhead leads to slower convergence and higher step counts.

---

### Competitive Agent (Independent Q-Learning)

- Individual reward signals  
- Agents act independently  
- No dependency between agents  

**Key Advantage:**  
Faster learning and efficient path optimization.

---

## Project Structure
├── environment.py
├── cooperative_agent.py
├── competitive_agent.py
├── training.py
├── metrics.py
├── visualization.py
├── main.py
├── claude_conversation_log.md
├── README.md
├── requirements.txt
---

## Performance Evaluation

### Metrics Used:
- Task Completion Time (steps per episode)  
- Strategy Efficiency (average steps)  
- Reward Distribution (cumulative reward trends)  

---

### Results Summary

| Metric               | Cooperative | Competitive |
|---------------------|------------|-------------|
| Avg Reward          | -20.29     | 3.07        |
| Avg Steps           | 25.26      | 5.44        |
| Convergence Speed   | Slow       | Fast        |
| Strategy Efficiency | Low        | High        |

---

## Key Insights

- **Reward structure drives behavior**
- Cooperation introduces:
  - Coordination complexity  
  - Delayed learning  
  - Lower efficiency  

- Competition leads to:
  - Faster convergence  
  - Direct strategies  
  - Higher rewards  

 Emergent behavior is not explicitly programmed—it is learned.

---

## Visualization

The project generates:
- Reward per episode plots  
- Steps per episode comparison  
- Agent path trajectories  

These visuals highlight the contrast between cooperative hesitation and competitive efficiency.

---

## How to Run

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd week3_marl_assignment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py