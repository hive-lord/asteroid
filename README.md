# Asteroid Shooter

A minimal, classic **asteroid shooter** built with [Pygame](https://www.pygame.org/). Move your ship, avoid collisions, shoot down asteroids, and monitor real-time game logs.

---

## 📦 Project Structure

```
├─ asteroid.py          # Single asteroid sprite class
├─ asteroidfield.py     # Generates and manages the field of asteroids
├─ circleshape.py       # Base class for circle‑shaped collision sprites
├─ constants.py         # Game configuration and constants
├─ logger.py            # Simple JSONL logger for event/state tracking
├─ main.py              # Entry point – game setup and main loop
├─ player.py            # Player ship logic (movement, rotation, shooting)
└─ shot.py              # Bullet / missile sprite class
```

The game is designed with simplicity in mind: all `pygame.sprite.Sprite` subclasses live in individual modules, with rendering and physics processed via Pygame groups in `main.py`.

---

## 🎮 Gameplay & Controls

| Key | Action |
| :--- | :--- |
| **W** | Move ship forward |
| **S** | Reverse / move ship backward |
| **A** | Rotate ship counter-clockwise (turn left) |
| **D** | Rotate ship clockwise (turn right) |
| **Space** | Fire projectile (with shot cooldown) |

### Objective
Avoid colliding with the floating asteroids. Shoot them to split and destroy them. The game ends instantly if an asteroid collides with your ship.

Press **Esc** or close the game window to exit.

---

## 🚀 Running Locally

This project supports running via traditional virtual environments or [uv](https://github.com/astral-sh/uv).

### Option A: Using `uv` (Recommended)
If you have `uv` installed, it will automatically handle virtual environment creation and package installation for you:
```bash
uv run main.py
```

### Option B: Standard Python Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/asteroid.git
   cd asteroid
   ```
2. **Set up a virtual environment and install dependencies**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install pygame
   ```
3. **Run the game**:
   ```bash
   python main.py
   ```

---

## 👓 Logging & Debugging

The game outputs structured logs in JSON Lines (JSONL) format for analytics or debugging:
- **`game_state.jsonl`**: Saved once per second, tracking the count and coordinates of active sprites.
- **`game_events.jsonl`**: Captures critical events in real time:
  - `player_hit`: Triggered when the ship is hit by an asteroid.
  - `asteroid_shot`: Triggered when a bullet successfully hits an asteroid.

These log files are overwritten or reset on every game launch.

---

## 🛠️ Customization & Balancing

All design and gameplay balancing parameters can be found in `constants.py`. You can adjust them directly:

```python
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_TURN_SPEED = 300          # Degrees per second
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
```

Simply update these values, save the file, and re-launch the game.

---

## 📜 License

This project is licensed under the MIT License.

