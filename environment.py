class GridWorldEnv:
    def __init__(self, grid_size=5, max_steps=30, mode="cooperative"):
        self.grid_size = grid_size
        self.max_steps = max_steps
        self.mode = mode  # cooperative or competitive

        self.agent_start_positions = [(0, 0), (4, 4)]
        self.goal_positions = [(4, 0), (0, 4)]
        self.obstacles = {(2, 2), (1, 2), (3, 2)}

        self.actions = ["up", "down", "left", "right", "stay"]
        self.action_to_delta = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
            "stay": (0, 0),
        }

        self.reset()

    def reset(self):
        self.agent_positions = list(self.agent_start_positions)
        self.steps = 0
        return self.get_state()

    def get_state(self):
        return tuple(self.agent_positions)

    def _move(self, pos, action):
        dx, dy = self.action_to_delta[action]
        new_x = max(0, min(self.grid_size - 1, pos[0] + dx))
        new_y = max(0, min(self.grid_size - 1, pos[1] + dy))
        new_pos = (new_x, new_y)

        if new_pos in self.obstacles:
            return pos
        return new_pos

    def step(self, actions):
        self.steps += 1

        proposed_positions = [
            self._move(self.agent_positions[i], actions[i]) for i in range(2)
        ]

        # Collision handling: if both move into same square, both stay
        if proposed_positions[0] == proposed_positions[1]:
            proposed_positions = self.agent_positions.copy()

        self.agent_positions = proposed_positions

        a0_goal = self.agent_positions[0] == self.goal_positions[0]
        a1_goal = self.agent_positions[1] == self.goal_positions[1]
        done = False

        if self.mode == "cooperative":
            if a0_goal and a1_goal:
                rewards = [20, 20]
                done = True
            else:
                rewards = [-1, -1]

        elif self.mode == "competitive":
            rewards = [-1, -1]
            if a0_goal and not a1_goal:
                rewards = [20, -10]
                done = True
            elif a1_goal and not a0_goal:
                rewards = [-10, 20]
                done = True
            elif a0_goal and a1_goal:
                rewards = [10, 10]
                done = True
        else:
            raise ValueError("Mode must be 'cooperative' or 'competitive'")

        if self.steps >= self.max_steps:
            done = True

        return self.get_state(), rewards, done

    def render(self):
        grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for ox, oy in self.obstacles:
            grid[ox][oy] = "#"

        for i, goal in enumerate(self.goal_positions):
            gx, gy = goal
            grid[gx][gy] = f"G{i}"

        for i, pos in enumerate(self.agent_positions):
            x, y = pos
            if grid[x][y].startswith("G"):
                grid[x][y] = f"A{i}/" + grid[x][y]
            else:
                grid[x][y] = f"A{i}"

        for row in grid:
            print(" ".join(f"{cell:>5}" for cell in row))
        print()