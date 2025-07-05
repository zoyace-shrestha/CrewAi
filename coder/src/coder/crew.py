from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Coder():
    """Coder crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def coder(self) -> Agent:
        """Coder agent"""
        return Agent(
            config=self.agents_config['coder'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode='safe',
            max_execution_time=30,
        )

    @task
    def coding_task(self) -> Task:
        """Coding task"""
        return Task(
            config=self.tasks_config['coding_task'],
        )
    

    @crew
    def crew(self) -> Crew:
        """Coder crew"""
        return Crew(
            agents= self.agents,
            tasks= self.tasks,
            verbose=True,
            process= Process.sequential,
        )
    
