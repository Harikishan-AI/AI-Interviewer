"""CLI entrypoint that delegates to the modular ai_interview package."""

from __future__ import annotations

import asyncio

from ai_interview.runner import main


if __name__ == "__main__":
    asyncio.run(main())
