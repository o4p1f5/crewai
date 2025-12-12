from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff
from tools import naver_news_search, urls_to_context

@CrewBase
class NewsCrew:
    agents_config = 'config/agents.yaml' 
    tasks_config = 'config/tasks.yaml' 

    @before_kickoff
    def before_kickoff_function(self, inputs):
        return inputs # before_kickoff를 구성하여 시작 전에 사용자로부터 쿼리를 받을 수 있도록 구성합니다.
    
    @agent
    def searcher(self) -> Agent:
        return Agent(
            config=self.agents_config['searcher'],
            verbose=True,
            tools=[naver_news_search.get_news_urls],
            llm='gpt-4o-mini'
        ) 
    @agent
    def analyzer(self) -> Agent:
        return Agent(
            config = self.agents_config['analyzer'],
            verbose = True,
            llm = 'gpt-4o-mini',
            tools = [urls_to_context.get_article]
        )
    @agent
    def answerman(self) -> Agent:
        return Agent(
            config = self.agents_config['answerman'],
            verbose = True,
            llm = 'gpt-4o-mini',
        )
    
    @task
    def news_search_task(self) -> Task:
        return Task(
            config = self.tasks_config['news_search_task']
        )
    
    @task
    def news_analyze_task(self) -> Task:
        return Task(
            config = self.tasks_config['news_analyze_task']
        )
    
    @task
    def answer_task(self) -> Task:
        return Task(
            config = self.tasks_config['answer_task']
        )
    
    @crew
    def news_crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # @agent 데코레이터로 감싸진 애들을 자동으로 가져옴
            tasks=self.tasks,    # @task 데코레이터로 감싸진 애들을 자동으로 가져옴
            process=Process.sequential,
            verbose=True,
        )