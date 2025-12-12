from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

from crew import NewsCrew
crew = NewsCrew().news_crew()

agent_input = {'query' : '엔비디아의 최신 동향에 대해 알려줘.'}
result = crew.kickoff(agent_input)