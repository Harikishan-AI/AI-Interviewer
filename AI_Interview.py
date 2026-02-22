from autogen_agentchat.agent import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPEN_ROUTER_API_KEY") 

model_client = OpenAIChatCompletionClient(
base_url="https://openrouter.ai/api/v1",
api_key=api_key,
model="arcee-ai/trinity-large-preview:free",    
model_info={
    "family": "arcee-ai",
    "vision": False,
    "function_calling": True,
    "json_output": True,
    "structured_output": True,
    "multiple_system_messages": True
    },
)

# Defining our Agent
# 1. Interviewer Agent
# 2. Interviewee Agent
# 3. Career Coach Agent
