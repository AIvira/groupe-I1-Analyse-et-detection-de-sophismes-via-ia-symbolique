"""Configuration du backend LLM local (serveur Ollama).

Le projet parle a un serveur **Ollama local** via le SDK `openai` : Ollama expose
une API compatible OpenAI sur `http://localhost:11434/v1`. Modele par defaut
`llama3.2`. Tout tourne en local, gratuitement (pas d'API payante).

Variables d'environnement (surchargent les defauts) :
- `OPENAI_BASE_URL` / `LLM_BASE_URL` : URL du serveur (defaut : Ollama local).
- `LLM_MODEL` / `OPENAI_MODEL`       : nom du modele a utiliser.
- `OPENAI_API_KEY`                   : ignoree par Ollama (une valeur factice est
                                       utilisee), mais le SDK `openai` en exige une.
"""

from __future__ import annotations

import importlib.util
import os
import socket
from urllib.parse import urlparse

# Defauts pour un serveur Ollama local (API compatible OpenAI).
DEFAULT_OLLAMA_URL = "http://localhost:11434/v1"
DEFAULT_OLLAMA_MODEL = "llama3.2"


def resolved_base_url() -> str:
    """URL du serveur Ollama (surchargeable via OPENAI_BASE_URL / LLM_BASE_URL)."""
    return (
        os.environ.get("OPENAI_BASE_URL")
        or os.environ.get("LLM_BASE_URL")
        or DEFAULT_OLLAMA_URL
    )


def default_model() -> str:
    """Modele a utiliser (surchargeable via LLM_MODEL / OPENAI_MODEL)."""
    return os.environ.get("LLM_MODEL") or os.environ.get("OPENAI_MODEL") or DEFAULT_OLLAMA_MODEL


def using_local() -> bool:
    """Vrai si le backend pointe vers un serveur local (Ollama), faux sinon (OpenAI distant)."""
    host = urlparse(resolved_base_url()).hostname or ""
    return host in ("localhost", "127.0.0.1", "0.0.0.0", "::1")


def make_client():
    """Construit un client OpenAI pointe vers le serveur Ollama local."""
    from openai import OpenAI

    # Ollama ignore la cle, mais le SDK `openai` exige une valeur non vide.
    api_key = os.environ.get("OPENAI_API_KEY") or "ollama"
    return OpenAI(base_url=resolved_base_url(), api_key=api_key)


def _server_reachable(base_url: str, timeout: float = 0.4) -> bool:
    parsed = urlparse(base_url)
    host = parsed.hostname or "localhost"
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def llm_available() -> bool:
    """Vrai si le backend LLM est utilisable (SDK installe + serveur Ollama joignable)."""
    if importlib.util.find_spec("openai") is None:
        return False
    return _server_reachable(resolved_base_url())
