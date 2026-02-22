from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from dotenv import load_dotenv
from autogen_agentchat.ui import Console
import os
load_dotenv()

api_key = os.getenv("OPEN_ROUTER_API_KEY") 

model_client = OpenAIChatCompletionClient(
base_url="https://openrouter.ai/api/v1",
api_key=api_key,
model="nvidia/nemotron-3-nano-30b-a3b:free",    
model_info={
    "family": "nvidia",
    "vision": False,
    "function_calling": True,
    "json_output": True,
    "structured_output": True,
    "multiple_system_messages": True
    },
)

# Defining our Agent
# 1. Interviewer Agent -> Assistant Agent
# 2. Interviewee Agent -> UserPorxyAgent
# 3. Career Coach Agent -> Assistant Agent
job_position = 'Software Engineer'

interviewer = AssistantAgent(
    name = "Interviewer",
    model_client = model_client,
    description = f'An agent the conducts interviwer for a {job_position} position',
    system_message = f'''
    You are a professional interviewer for a {job_position} position.
    Ask one clear question at a time and wait for user to respond.
    Your Job is to continue and aks questions, don't pay any atention to career coach agent response.
    Make sure to ask question based on candidate's answer and your expertise in the field.
    Ask 3 questions in total covering techincal skills and experience, problem-solving abilities, and cultural fit.
    After asking 3 questions, say, 'TERMINATE' at the end of the interview.
    Make question under 50 words.
    '''
)

candidate= UserProxyAgent(
    name = "Candidate",
    description = f'An agnet that simultes a candidate for a {job_position} position',
    input_func = input
)

career_coch = AssistantAgent(
    name = 'Career_Coach',
    model_client = model_client,
    description = f'An AI agent that provides feedback and advice to candidate for a {job_position} position',
    system_message =f'''
    You are a career coach specializing in preparing candidates for {job_position} interviews.
    Provide constructive feedback on the candidate's reponse and suggest improvements.
    After the Interview, summarize the candidate's performance and provide actionable advice.
    Make it under 100 words.
    '''
)

team =  RoundRobinGroupChat(
    participants=[interviewer, candidate, career_coch],
    termination_condition = TextMentionTermination(text='TERMINATE'),
    max_turns = 20
)

stream = team.run_stream(task='Conducting an interview for a Software Engineer position')

async def main():
    await Console(stream)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())