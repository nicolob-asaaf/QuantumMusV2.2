# Quantum Mus

**Juego de cartas para 4 jugadores** que combina las reglas del Mus con conceptos de física cuántica: superposición, entrelazamiento y notación de Dirac.

---

## Descripción

Quantum Mus es una versión del clásico juego español Mus en la que las cartas pueden estar en **estado superpuesto** o **entrelazadas** con las de tu compañero. Cada jugador elige un personaje inspirado en pioneros de la información cuántica (Preskill, Cirac, Zoller, Deutsch) y juega en equipos de dos. La interfaz usa una estética de “circuito cuántico” y notación |ψ⟩ en las cartas.

---

## Características

- **Portada** con referencia visual a lo cuántico (esfera tipo Bloch, ondas, partículas).
- **Flujo de partida**: nombre → menú (Crear partida / Unirse) → lobby con código de sala.
- **Lobby**: elección de personaje (cada uno solo una vez), modo 4 u 8 reyes, lista de jugadores.
- **Modo demo**: botón para añadir 3 jugadores de prueba y jugar en solitario.
- **Orientación por personaje**: tú siempre en la parte inferior; compañero arriba; oponentes a los lados.
- **Cartas**: visibles solo las tuyas; las del compañero muestran solo el **brillo en el borde** cuando están entrelazadas con las tuyas (no se ve la carta).
- **Modo 4 reyes**: A y K entrelazados por palo.
- **Modo 8 reyes**: además, 2 y 3 entrelazados por palo.
- **Animación de reparto** de cartas al inicio de la partida.
- **Estilo**: paleta teal, violeta, coral y dorado; fondos tipo “blueprint” y puertas cuánticas (H, CNOT, M).

---

## Cómo ejecutar

### Solo frontend (sin backend)

1. Abre la carpeta del proyecto.
2. Abre `frontend/index.html` en un navegador (doble clic o arrastrar al navegador).

O sirve la carpeta con un servidor local, por ejemplo:

```bash
cd frontend
npx serve .
# o: python -m http.server 8000
```

Luego entra en `http://localhost:3000` (o el puerto que indique).

### Con backend (completo)

La carpeta `backend/` contiene el servidor Flask + Socket.IO para juego multijugador en tiempo real.

**Requisitos:**
- Python 3.8 o superior
- pip

**Instalación y ejecución:**

```bash
cd backend

# Linux/Mac
./run.sh

# Windows
run.bat

# O manualmente:
pip install -r requirements.txt
python server.py
```

El servidor se iniciará en `http://localhost:5000`

**En producción (Render):**
- El `Procfile` configura el servidor para despliegue
- Variables de entorno necesarias: `PORT`, `FRONTEND_URL`, `ALLOWED_ORIGINS`

---

## Estructura del proyecto

```
QuantumMusV2.2/
├── frontend/
│   ├── index.html             # Punto de entrada; pantallas (portada, menú, lobby, partida)
│   ├── styles.css             # Estilos principales y animaciones
│   ├── game.js                # Lógica del juego, cartas, reparto, entrelazamiento
│   ├── navigation.js          # Navegación entre pantallas, lobby, personajes
│   ├── insp.js                # Funciones de inspección y debugging
│   ├── config.js              # Configuración del juego
│   ├── config.override.js     # Configuración local (no se sube a git)
│   ├── assets/
│   │   ├── generate-cards.js  # Generación de gráficos de cartas
│   │   └── stiles.ccs         # Estilos adicionales de cartas
│   └── css/
│       └── navigation-styles.css  # Estilos de navegación
├── backend/
│   ├── server.py              # Servidor Flask + Socket.IO
│   ├── game_logic.py          # Lógica principal del juego
│   ├── room_manager.py        # Gestión de salas
│   ├── card_deck.py           # Manejo de barajas
│   ├── Logica_cuantica/       # Mecánicas cuánticas (Qiskit)
│   │   ├── baraja.py          # Baraja cuántica
│   │   ├── cartas.py          # Cartas cuánticas
│   │   ├── dealer.py          # Repartidor
│   │   ├── efecto_tunel.py    # Efecto túnel cuántico
│   │   └── jugador.py         # Clase jugador
│   ├── models.py              # Modelos de base de datos
│   └── requirements.txt       # Dependencias Python
└── README.md
```

---

## Flujo de juego

1. **Portada** → Pulsar *JUGAR*.
2. **Nombre** → Introducir nombre y continuar.
3. **Menú** → *Crear partida* (eres host) o *Unirse a partida* (código de 4 caracteres).
4. **Lobby**  
   - Host: elige 4 u 8 reyes; todos eligen personaje (sin repetir).  
   - Opción *Demo: añadir jugadores de prueba* para jugar solo.  
   - *Iniciar partida* cuando haya 4 jugadores listos.
5. **Partida** → Reparto animado; tú abajo, compañero arriba; solo ves tus cartas y el brillo entrelazado del compañero.

---

## Tecnologías

- **Frontend**: HTML5, CSS3, JavaScript (vanilla).
- **Estilo**: variables CSS, gradientes, animaciones y keyframes.
- **Backend** (opcional): Python.

---

## Documentación adicional

- **Entrelazamiento y modos**: ver `Frontend/ENTANGLEMENT_GUIDE.md` para 4 reyes, 8 reyes y mecánicas cuánticas en el juego.

---

## Créditos

Proyecto desarrollado en el contexto UCM FISICA / CESGA. Personajes inspirados en figuras de la información e informática cuántica (Preskill, Cirac, Zoller, Deutsch).
