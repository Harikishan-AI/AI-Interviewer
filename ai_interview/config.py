"""Configuration objects for the AI interview application."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class InterviewConfig:
    """Configuration for an interview session.

    Attributes:
        job_position: Role being interviewed for, used to specialize prompts.
        max_turns: Hard cap on total conversation turns across all agents.
        total_questions: Number of questions the interviewer should ask.
    """

    job_position: str = "Software Engineer"
    max_turns: int = 20
    total_questions: int = 3

