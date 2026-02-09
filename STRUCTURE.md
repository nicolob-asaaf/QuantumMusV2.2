# Quantum Mus - Repository Structure

This document describes the cleaned and organized structure of the Quantum Mus repository.

## Overview

Quantum Mus is a multiplayer card game that combines traditional Mus rules with quantum mechanics concepts (superposition, entanglement). The project is split into frontend (HTML/CSS/JS) and backend (Python/Flask/Socket.IO).

## Directory Structure

```
QuantumMusV2.2/
│
├── frontend/                      # Frontend application (browser-based)
│   ├── index.html                 # Main entry point - game screens
│   ├── game.js                    # Core game logic and mechanics
│   ├── navigation.js              # Screen navigation and UI flow
│   ├── insp.js                    # Inspection and debugging utilities
│   ├── styles.css                 # Main stylesheet
│   ├── config.js                  # Default configuration
│   ├── config.override.js         # Local config overrides (not in git)
│   ├── assets/
│   │   ├── generate-cards.js      # Card graphics generation
│   │   └── stiles.ccs             # Additional card styles
│   └── css/
│       └── navigation-styles.css  # Navigation-specific styles
│
├── backend/                       # Backend server (Python)
│   ├── server.py                  # Main Flask + Socket.IO server
│   ├── game_logic.py              # Game state and logic orchestration
│   ├── game_manager.py            # Active game instance management
│   ├── room_manager.py            # Room/lobby management
│   ├── round_handlers.py          # Round-specific logic (MUS, GRANDE, etc.)
│   ├── card_deck.py               # Card and deck management
│   ├── quantum_collapse.py        # Quantum state collapse logic
│   ├── entanglement_system.py     # Card entanglement mechanics
│   ├── generic_betting_handler.py # Generic betting phase logic
│   ├── grande_betting_handler.py  # GRANDE phase betting
│   ├── models.py                  # Database models (SQLAlchemy)
│   ├── config.py                  # Backend configuration
│   ├── requirements.txt           # Python dependencies
│   ├── run.sh                     # Linux/Mac startup script
│   ├── run.bat                    # Windows startup script
│   ├── .env.example               # Example environment variables
│   ├── .gitignore                 # Backend-specific gitignore
│   ├── README.md                  # Backend documentation
│   │
│   ├── Logica_cuantica/           # Quantum mechanics implementation (Qiskit)
│   │   ├── baraja.py              # Quantum deck (40 Spanish cards)
│   │   ├── cartas.py              # Quantum card class (6 qubits)
│   │   ├── dealer.py              # Dealer logic with quantum rules
│   │   ├── efecto_tunel.py        # Quantum tunnel effect
│   │   └── jugador.py             # Player class
│   │
│   ├── instance/                  # Runtime data (not in git)
│   │   └── quantum_mus.db         # SQLite database
│   │
│   └── test_*.py                  # Test files
│
├── instance/                      # Additional runtime data
│   └── quantum_mus.db             # Database (duplicate, can be removed)
│
├── .gitignore                     # Root gitignore (Python, DBs, configs)
├── .nojekyll                      # GitHub Pages config
├── Procfile                       # Deployment config (Render/Heroku)
├── README.md                      # Main documentation
└── DEPLOYMENT.md                  # Deployment guide

```

## What Was Cleaned Up

### 1. Removed Duplicate Folders
- **`backend/Logica cuantica/`** (with space) - REMOVED
- **`backend/Logica_cuantica/`** (with underscore) - KEPT (Python standard)
  - This folder had duplicate class definitions and broken imports
  - Fixed `cartas.py` which had duplicate QuantumCard class definition

### 2. Removed Duplicate Assets
- **`backend/assets/`** - REMOVED
  - Contained `generate-cards.js` and `stiles.ccs`
  - These are frontend-only files, now only in `frontend/assets/`

### 3. Removed Deprecated Files
- **`backend/Requisements.py`** - REMOVED
  - Was marked as deprecated
  - `backend/requirements.txt` is the correct file to use

### 4. Fixed Dependency Issues
- **`requirements.txt`** - Fixed duplicate `eventlet==0.33.3` entry

### 5. Added Missing Files
- **`.gitignore`** at root - Added to prevent committing:
  - Python cache files (`__pycache__/`, `*.pyc`)
  - Virtual environments (`venv/`, `env/`)
  - Database files (`*.db`, `*.sqlite3`, `instance/`)
  - IDE files (`.vscode/`, `.idea/`)
  - Local config overrides (`config.override.js`)
  - Temporary files

## Key Architecture Components

### Frontend (Browser)
- **Vanilla JavaScript** - No frameworks
- **Socket.IO Client** - Real-time WebSocket communication
- **Canvas/SVG** - Card rendering with quantum visualizations
- **CSS Variables** - Quantum-themed color palette

### Backend (Server)
- **Flask** - Web framework
- **Flask-SocketIO** - WebSocket support
- **SQLAlchemy** - Database ORM
- **Qiskit** - Quantum circuit simulation for card mechanics
- **eventlet** - Async worker for Socket.IO

### Quantum Mechanics
- **6 qubits per card**: 2 for suit (palo), 4 for value (valor)
- **Entanglement**: King-Jack pairs can be entangled by suit
- **Collapse**: Cards collapse to classical state when measured
- **Superposition**: Cards can exist in multiple states before measurement

## Running the Project

### Frontend Only (Local)
```bash
cd frontend
python -m http.server 8000
# Open http://localhost:8000
```

### Full Stack (Local)
```bash
cd backend
./run.sh  # or run.bat on Windows
# Server starts on http://localhost:5000
```

### Production (Render/Heroku)
- Uses `Procfile` for deployment
- Set environment variables: `PORT`, `FRONTEND_URL`, `ALLOWED_ORIGINS`
- `gunicorn` with `eventlet` worker for WebSocket support

## Database Schema

### Players Table
- `id`, `username`, `games_played`, `games_won`, `total_points`, `created_at`

### Games Table
- `id`, `room_id`, `game_mode`, `status`, `winner_team`, `team_scores`, `current_round`, `created_at`

### GameHistory Table
- `id`, `game_id`, `event_type`, `player_id`, `event_data`, `timestamp`

## Game Flow

1. **Portada** (Cover) - Landing screen
2. **Menu** - Create or join room
3. **Lobby** - 4 players, character selection, ready up
4. **Game** - MUS, GRANDE, CHICA, PARES, JUEGO rounds
5. **Scoring** - First team to 40 points wins

## Configuration

### Frontend Config
- `config.js` - Default settings (in git)
- `config.override.js` - Local overrides (not in git)
  - Set `QUANTUM_MUS_SERVER_URL` for custom backend URL

### Backend Config
- `.env` - Environment variables (not in git)
- See `.env.example` for required variables

## Next Steps

To continue development:
1. ✅ Structure is cleaned and organized
2. ✅ Documentation is updated
3. ✅ Imports are fixed
4. ⬜ Test full game flow locally
5. ⬜ Test deployment to production
6. ⬜ Add more game features (PARES, JUEGO rounds)

## Notes

- The `instance/` folder at root is a duplicate of `backend/instance/` and can be removed
- All Python code follows PEP 8 naming conventions
- Frontend uses ES6+ JavaScript features
- Database is SQLite by default, can be changed to PostgreSQL for production
