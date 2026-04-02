# AGENTS.md - Development Guide for AI Agents

This document provides guidelines for AI agents working in this codebase.

## Project Overview

This is a simple Hangman (Ahorcado) game written in Python. It consists of three modules:
- `ahorcado.py` - Main game logic and CLI interface
- `estados_graficos.py` - ASCII art for hangman drawing states
- `palabras.py` - Word list for the game

## Running the Project

```bash
python ahorcado.py
```

## Testing

This project does not currently have a test suite. When adding tests:

```bash
# Run all tests
pytest

# Run a single test file
pytest tests/test_ahorcado.py

# Run a single test function
pytest tests/test_ahorcado.py::test_funcion_name -v
```

To add testing to this project:
```bash
pip install pytest
pytest --init  # Create pytest.ini configuration
```

## Linting and Code Quality

Recommended tools for this Python project:

```bash
# Install linting tools
pip install ruff flake8 mypy

# Run ruff linter
ruff check .

# Run ruff with auto-fix
ruff check . --fix

# Run type checker
mypy .

# Run all checks
ruff check . && mypy .
```

## Code Style Guidelines

### Imports

- Group imports in the following order (separated by blank lines):
  1. Standard library imports (`random`, `sys`, etc.)
  2. Third-party imports (`numpy`, `pandas`, etc.)
  3. Local application imports (`from palabras import ...`)
- Use absolute imports, not relative imports
- Do not use wildcard imports (`from module import *`)

```python
# Correct
import random
import sys
from typing import List, Optional

from palabras import elegir_palabra
from estados_graficos import mostrar_estado, MAX_INTENTOS

# Incorrect
from .palabras import *
import random, sys
```

### Formatting

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use blank lines sparingly to separate logical sections
- No trailing whitespace
- Use snake_case for file names

### Types

- Add type hints for function parameters and return values
- Use `Optional[T]` instead of `Union[T, None]`
- Use `List`, `Dict`, `Tuple` from `typing` (or use lowercase `list`, `dict`, `tuple` for Python 3.9+)

```python
# Good
def elegir_palabra() -> str:
    palabra_secreta: str = elegir_palabra().lower()
    letras_usadas: set[str] = set()
    palabra_oculta: list[str] = ["_"] * len(palabra_secreta)

def mostrar_estado(
    intentos_fallidos: int,
    palabra_oculta: list[str],
    letras_usadas: set[str]
) -> None:
```

### Naming Conventions

- **Variables/Functions**: `snake_case` (e.g., `palabra_secreta`, `elegir_palabra`)
- **Constants**: `SCREAMING_SNAKE_CASE` (e.g., `MAX_INTENTOS`, `PALABRAS`)
- **Classes**: `PascalCase` (e.g., `GameState`)
- **Modules**: `snake_case` (e.g., `estados_graficos.py`)
- Use descriptive, Spanish-language names matching the existing codebase
- Avoid single-letter variables except in loops (`i`, `j`, `k`)

### Functions

- Keep functions small and focused on a single task
- Use docstrings for all public functions
- Add type hints to all parameters and return values

```python
def elegir_palabra() -> str:
    """Devuelve una palabra aleatoria de la lista de palabras."""
    return random.choice(PALABRAS)
```

### Error Handling

- Use exceptions for unexpected errors
- Validate user input early and provide clear error messages
- Avoid catching bare `Exception` - catch specific exceptions

```python
# Input validation example
entrada = input("Adivina una letra: ").lower().strip()
if not entrada or len(entrada) != 1 or not entrada.isalpha():
    print("Entrada inválida. Por favor, ingresa una sola letra.\n")
    continue
```

### Constants

- Place constants at the module level in `SCREAMING_SNAKE_CASE`
- Group related constants
- Add docstrings for module-level constants

```python
AHORCADO = [
    """...""",
    # ... ASCII art states
]

MAX_INTENTOS = len(AHORCADO) - 1
```

### Comments

- Use comments sparingly - prefer self-documenting code
- Write comments in Spanish to match the codebase
- Keep comments up-to-date with code changes

### Strings

- Use f-strings for string formatting (Python 3.6+)
- Use triple quotes for multi-line strings

```python
# Good
print(f"Intentos restantes: {MAX_INTENTOS - intentos_fallidos}")
print("\nPalabra: " + " ".join(palabra_oculta))

# Avoid
print("Intentos restantes: " + str(MAX_INTENTOS - intentos_fallidos))
```

### Best Practices

- Follow PEP 8 style guide
- Use `__main__` guard for executable scripts
- Keep functions under 30 lines
- Avoid global variables; pass state explicitly
- Use list/dict comprehensions when appropriate
- Test edge cases (empty input, repeated letters, etc.)

## File Structure

```
Juego del Ahorcado/
├── ahorcado.py          # Main game logic
├── estados_graficos.py  # ASCII art states
├── palabras.py         # Word list
├── tests/              # Test files (to be added)
│   └── test_ahorcado.py
├── AGENTS.md           # This file
└── README.md
```

## Common Tasks

### Adding New Words

Edit `palabras.py` and add new strings to the `PALABRAS` list:

```python
PALABRAS = [
    "python",
    "programacion",
    # Add new words here
]
```

### Adding New Hangman States

Edit `estados_graficos.py` and add new ASCII art to the `AHORCADO` list. Update `MAX_INTENTOS` will automatically adjust.

### Running a Single Test

```bash
pytest tests/test_ahorcado.py::test_name -v
```
