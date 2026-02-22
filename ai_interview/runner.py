"""Async orchestration and CLI entry logic for the AI interview app."""

from __future__ import annotations

import asyncio
from typing import Optional

from autogen_agentchat.ui import Console

from .config import InterviewConfig
from .team import build_interview_team


async def run_interview(config: Optional[InterviewConfig] = None) -> None:
    """Run a full interactive interview session using the console UI."""

    if config is None:
        config = InterviewConfig()

    team = build_interview_team(config)
    task = f"Conduct an interview for a {config.job_position} position."

    stream = team.run_stream(task=task)
    await Console(stream)


async def main() -> None:
    """Entry point for launching the interactive interview experience."""

    try:
        job_position = input(
            "Enter the job position for the interview "
            "(press Enter for 'Software Engineer'): "
        ).strip() or "Software Engineer"

        config = InterviewConfig(job_position=job_position)
        await run_interview(config)
    except KeyboardInterrupt:
        print("\nInterview interrupted by user.")
    except Exception as exc:
        print(f"Fatal error while running interview: {exc}")


def run() -> None:
    """Synchronous convenience wrapper to run the main coroutine."""

    asyncio.run(main())

