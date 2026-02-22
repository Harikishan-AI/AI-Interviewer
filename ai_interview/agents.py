"""Agent construction utilities for the AI interview application."""

from __future__ import annotations

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent

from .config import InterviewConfig
from .model_client import build_model_client


def build_interviewer_agent(
    config: InterviewConfig,
) -> AssistantAgent:
    """Create the interviewer agent that drives the conversation."""

    model_client = build_model_client()
    job_position = config.job_position
    total_questions = config.total_questions

    system_message = (
        f"You are a senior hiring manager interviewing for a {job_position} role.\n"
        f"- Ask one clear, concise question at a time and wait for the candidate to answer.\n"
        f"- Ask exactly {total_questions} questions in total.\n"
        "- Cover: technical depth, problem-solving approach, and team/culture fit.\n"
        "- Adapt each new question based on the candidate's previous answer.\n"
        "- Use professional but friendly tone, and stay focused on the role.\n"
        "- Do not reference or respond to any messages from the career coach agent.\n"
        "- Keep each question under 50 words.\n"
        "- After the final question, append the word 'TERMINATE' to your message."
    )

    return AssistantAgent(
        name="Interviewer",
        model_client=model_client,
        description=(
            f"An AI interviewer that conducts a structured interview for a "
            f"{job_position} position."
        ),
        system_message=system_message,
    )


def build_candidate_agent(config: InterviewConfig) -> UserProxyAgent:
    """Create the candidate agent that proxies user input into the conversation."""

    job_position = config.job_position

    return UserProxyAgent(
        name="Candidate",
        description=(
            f"Represents the human candidate interviewing for a {job_position} role. "
            "Forwards terminal input into the multi-agent conversation."
        ),
        input_func=input,
    )


def build_career_coach_agent(
    config: InterviewConfig,
) -> AssistantAgent:
    """Create the career coach agent that provides feedback and a final summary."""

    model_client = build_model_client()
    job_position = config.job_position

    system_message = (
        f"You are an experienced career coach specializing in {job_position} interviews.\n"
        "- Observe the conversation between the interviewer and candidate.\n"
        "- After each candidate answer, provide brief, constructive feedback.\n"
        "- Focus on clarity, structure, depth, and alignment with the role.\n"
        "- After the interview ends (when you see 'TERMINATE'),\n"
        "  summarize the candidate's overall performance and suggest 2–3 concrete\n"
        "  improvements for future {job_position} interviews.\n"
        "- Keep feedback messages under 100 words."
    )

    return AssistantAgent(
        name="Career_Coach",
        model_client=model_client,
        description=(
            f"An AI career coach that critiques and guides candidates for {job_position} interviews."
        ),
        system_message=system_message,
    )

