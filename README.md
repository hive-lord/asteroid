# Asteroid Shooter

A minimal classic **asteroid shooter** built with [Pygame](https://www.pygame.org/).  Copy the code, hit *Space* and you'll ram mines to death.

---
## 📦 Project structure
```
├─ asteroid.py          # Single asteroid sprite
├─ asteroidfield.py     # Generates a field of asteroids
├─ circleshape.py       # Base class for circle‑shaped sprites
├─ constants.py         # Game configuration values
├─ logger.py            # Very small JSONL logger
├─ main.py              # Entry point – game loop & setup
├─ player.py            # Ship logic (movement, rotation, shooting)
└─ shot.py              # Bullet / missile sprite
```
The game is intentionally small: all `pygame.sprite.Sprite` subclasses live in individual files and the rendering/physics are handled by their respective update methods.

---
## 🎮 Gameplay – How to play
| Key | Action |
|-----|--------|
| **W** | Move ship forward |
| **S** | Reverse ship |
| **A** | Turn left |
| **D** | Turn right |
| **Space** | Fire missile (with a short cooldown) |

The objective is simple: avoid colliding with asteroids while shooting them down before they hit you.

Press *Esc* or close the window to exit.

---
## 🚀 Running locally
1. **Clone the repo**.
   ```bash
   git clone https://github.com/your‑repo/asteroid.git
   cd asteroid
   ```
2. **Install dependencies** (the project only needs Pygame).
   ```bash
   pip install pygame
   ```
3. **Run the game**.
   ```bash
   python main.py
   ```
The window starts automatically; no additional assets are required.

---
## 👓 Logging (developer interest)
- **State snapshots** (`game_state.jsonl`) are written once per second and contain counts/snapshots of each sprite group.  They can be useful for debugging physics or visualising state over time.
- **Events** (`game_events.jsonl`) capture key moments such as:
  - `player_hit`
  - `asteroid_shot`

Both files are simple JSON‑lines and reset on every new run.

---
## 🛠️ Extending the game
The project structure is deliberately straightforward; just edit or add a module and import it in `main.py`.

### Change the control scheme
Open `player.py`: modify the key checks under `update()` → `keys = pg.key.get_pressed()`.

### Tweak gameplay balance
Values live in **constants.py**:
```python
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_TURN_SPEED = 300          # Degrees per second
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
```
Values are unitless constants – update them, re‑run and test.

### Add a new sprite class
A new `pygame.sprite.Sprite` subclass can be instantiated just like `Asteroid` or `Shot`.  Import it in `main.py` and add it to an appropriate sprite group.

---
## 🧪 Testing & CI (future work)
No test suite is provided yet.  If you wish to add one, write unit tests against the logic in e.g. `player.py` or `AsteroidField` and run them with any test runner you prefer.

---
## 📜 License
This project is released under the MIT license.
