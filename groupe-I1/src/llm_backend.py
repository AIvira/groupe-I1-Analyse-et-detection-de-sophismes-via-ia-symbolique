"""Configuration du backend LLM (OpenAI distant ou serveur local Ollama).

Le projet parle a un serveur compatible API OpenAI via le SDK `openai`. Deux
cibles possibles, choisies automatiquement :

- **OpenAI distant** : si `OPENAI_API_KEY` est defini (ou si `OPENAI_BASE_URL`
  pointe vers un endpoint distant). Modele par defaut `gpt-4o`.
- **Ollama local** : sinon, on se rabat sur `http://localhost:11434/v1`
  (serveur Ollama) qui expose une API compatible OpenAI. Modele par defaut
  `llama3.2`. Pratique quand l'acces a l'API OpenAI/Anthropic payante n'est pas
  disponible : tout tourne en local, gratuitement.

Variables d'environnement (surchargent les defauts) :
- `LLM_BACKEND`     : force le backend — `ollama`/`local` ou `openai`/`remote`.
                      Pratique pour utiliser Ollama meme si `OPENAI_API_KEY`
                      traine dans l'environnement.
- `OPENAI_BASE_URL` : URL du serveur (ex. `http://localhost:11434/v1`).
- `OPENAI_API_KEY`  : cle API (ignoree par Ollama, mais requise par le SDK).
- `LLM_MODEL` / `OPENAI_MODEL` : nom du modele a utiliser.
"""

from __future__ import annotations

import importlib.util
import os
import socket
from urllib.parse import urlparse

# Defauts pour un serveur Ollama local (API compatible OpenAI).
DEFAULT_OLLAMA_URL = "http://localhost:11434/v1"
DEFAULT_OLLAMA_MODEL = "llama3.2"
DEFAULT_OPENAI_MODEL = "gpt-4o"


def _explicit_base_url() -> str | None:
    return os.environ.get("OPENAI_BASE_URL") or os.environ.get("LLM_BASE_URL")


def _forced_backend() -> str | None:
    """Lit `LLM_BACKEND` : 'ollama'/'local' ou 'openai'/'remote'. Sinon None (auto)."""
    val = os.environ.get("LLM_BACKEND", "").strip().lower()
    if val in {"ollama", "local"}:
        return "ollama"
    if val in {"openai", "remote"}:
        return "openai"
    return None  # auto


def using_local() -> bool:
    """Vrai si l'on cible un serveur local (Ollama) plutot qu'OpenAI distant."""
    forced = _forced_backend()
    if forced is not None:
        return forced == "ollama"
    base = _explicit_base_url()
    if base is not None:
        host = (urlparse(base).hostname or "").lower()
        return host in {"localhost", "127.0.0.1", "::1", "0.0.0.0"}
    # Pas d'URL explicite : on bascule en local des qu'il n'y a pas de cle OpenAI.
    return not os.environ.get("OPENAI_API_KEY")


def resolved_base_url() -> str | None:
    """URL effective du serveur (None => endpoint OpenAI par defaut du SDK)."""
    base = _explicit_base_url()
    if base is not None:
        return base
    return DEFAULT_OLLAMA_URL if using_local() else None


def default_model() -> str:
    explicit = os.environ.get("LLM_MODEL") or os.environ.get("OPENAI_MODEL")
    if explicit:
        return explicit
    return DEFAULT_OLLAMA_MODEL if using_local() else DEFAULT_OPENAI_MODEL


def make_client():
    """Construit un client OpenAI vers la bonne cible (OpenAI ou Ollama local)."""
    from openai import OpenAI

    base_url = resolved_base_url()
    if using_local():
        api_key = os.environ.get("OPENAI_API_KEY") or "ollama"  # Ollama ignore la cle
    else:
        api_key = os.environ.get("OPENAI_API_KEY")
    return OpenAI(base_url=base_url, api_key=api_key)


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
    """Vrai si un backend LLM est utilisable (SDK installe + cible joignable)."""
    if importlib.util.find_spec("openai") is None:
        return False
    if using_local():
        return _server_reachable(resolved_base_url() or DEFAULT_OLLAMA_URL)
    return bool(os.environ.get("OPENAI_API_KEY"))
