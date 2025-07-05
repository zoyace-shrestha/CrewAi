from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class EngineeringTeam():
    """EngineeringTeam crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def engineering_lead(self) -> Agent:
        """Engineering lead agent"""
        return Agent(
            config=self.agents_config['engineering_lead'],
            verbose=True,
        )
    
    @agent
    def backend_engineer(self) -> Agent:
        """Backend engineer agent"""
        return Agent(
            config=self.agents_config['backend_engineer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode='safe',
            max_execution_time=240,
            max_retry_limit=5,
        )
  
    @agent
    def frontend_engineer(self) -> Agent:
        """Frontend engineer agent"""
        return Agent(
            config=self.agents_config['frontend_engineer'],
            verbose=True,
        )
    
    @agent
    def test_engineer(self) -> Agent:
        """Test engineer agent"""
        return Agent(
            config=self.agents_config['test_engineer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode='safe',
            max_execution_time=240,
            max_retry_limit=5,
        )
    
    @task
    def design_task(self) -> Task:
        """Design task"""
        return Task(
            config=self.tasks_config['design_task']
        )
    
    @task
    def code_task(self) -> Task:
        """Code task"""
        return Task(
            config=self.tasks_config['code_task']
        )
    
    @task
    def frontend_task(self) -> Task:
        """Frontend task"""
        return Task(    
            config=self.tasks_config['frontend_task']
        )
    
    @task
    def test_task(self) -> Task:
        """Test task"""
        return Task(
            config=self.tasks_config['test_task']
        )
    
    @crew
    def crew(self) -> Crew:
        """Engineering team crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            max_concurrency=10,
            process=Process.sequential,
        )
    
    