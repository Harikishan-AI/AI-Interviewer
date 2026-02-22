"""Team assembly for the AI interview multi-agent conversation."""

from __future__ import annotations

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat

from .agents import (
    build_candidate_agent,
    build_career_coach_agent,
    build_interviewer_agent,
)
from .config import InterviewConfig


def build_interview_team(config: InterviewConfig) -> RoundRobinGroupChat:
    """Create the round-robin group chat coordinating interviewer, candidate, and coach."""

    interviewer = build_interviewer_agent(config)
    candidate = build_candidate_agent(config)
    career_coach = build_career_coach_agent(config)

    return RoundRobinGroupChat(
        participants=[interviewer, candidate, career_coach],
        termination_condition=TextMentionTermination(text="TERMINATE"),
        max_turns=config.max_turns,
    )

