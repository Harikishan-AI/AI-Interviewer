"""Model client construction and API key handling for the AI interview app."""

from __future__ import annotations

import os
from typing import Optional

from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv


load_dotenv()


def get_api_key(env_var: str = "OPEN_ROUTER_API_KEY") -> str:
    """Return the OpenRouter API key from environment variables.

    Raises:
        RuntimeError: If the expected environment variable is missing or empty.
    """

    api_key = os.getenv(env_var)
    if not api_key:
        raise RuntimeError(
            f"Missing API key in environment variable '{env_var}'. "
            "Set it in your .env file or OS environment before running the app."
        )
    return api_key


def build_model_client(api_key: Optional[str] = None) -> OpenAIChatCompletionClient:
    """Construct and return a configured OpenAIChatCompletionClient for OpenRouter."""

    if api_key is None:
        api_key = get_api_key()

    return OpenAIChatCompletionClient(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        model="nvidia/nemotron-3-nano-30b-a3b:free",
        model_info={
            "family": "nvidia",
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "structured_output": True,
            "multiple_system_messages": True,
        },
    )

