from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SeleniumScrapingTool
from dotenv import load_dotenv
load_dotenv()

@CrewBase
class BuildingASkilledSdetCrewForComprehensiveTestAutomationCrew():
    """BuildingASkilledSdetCrewForComprehensiveTestAutomation crew"""

    @agent
    def test_case_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['test_case_generator'],
            
        )

    @agent
    def script_automation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['script_automation_specialist'],
            
        )

    @agent
    def execution_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['execution_manager'],
            
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'],
            
        )


    @task
    def generate_manual_test_cases(self) -> Task:
        return Task(
            config=self.tasks_config['generate_manual_test_cases'],
            tools=[],
        )

    @task
    def create_automation_scripts(self) -> Task:
        return Task(
            config=self.tasks_config['create_automation_scripts'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def execute_automated_scripts(self) -> Task:
        return Task(
            config=self.tasks_config['execute_automated_scripts'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def generate_execution_report(self) -> Task:
        return Task(
            config=self.tasks_config['generate_execution_report'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the BuildingASkilledSdetCrewForComprehensiveTestAutomation crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
