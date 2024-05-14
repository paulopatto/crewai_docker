from app.config.llms import GeminiModel
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import tool
import app.settings

@CrewBase
class MyCrew():
    """Multicrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def leia(self) -> Agent:
        """ Léia """
        return Agent(
            config = self.agents_config['leia'],
            verbose = True,
            llm=GeminiModel
        )

    @tool("X-Wing")
    def x_wing():
        """
        Simulação das funcionalidades de uma X-Wing para a missão de destruir a estrela da morte.
        Retorna um texto que indica que a X-Wing está pronta para o ataque final com sistemas de mira ativados.
        """
        return "X-Wing pronto para o ataque final, sistemas de mira ativados. Atacando!"

    @agent
    def luke(self) -> Agent:
        """Luke"""
        return Agent(
            config = self.agents_config['luke'],
            verbose = True,
            tools=[self.x_wing], # Example of custom tool, loaded on the beginning of file
            llm=GeminiModel
        )

    @tool("millennium_falcon")
    def millennium_falcon():
        """
        Simulação das funcionalidades de uma Millennium Falcon para proteger Luke.
        Retorna uma string que indica que a Millennium Falcon está atacando o inimigo e protegendo a rota de Luke.
        """
        return "Millennium Falcon atacando o inimigo, protegendo a rota de Luke na X-Wing."

    @agent
    def han(self) -> Agent:
        """Han Solo"""
        return Agent(
            config = self.agents_config['han'],
            verbose = True,
            tools=[self.millennium_falcon], # Example of custom tool, loaded on the beginning of file
            llm=GeminiModel
        )

    @task
    def cordinate_attack_task(self) -> Task:
        return Task(
            config=self.tasks_config['cordinate_attack_task'],
            agent=self.leia(),
            allow_delegation = True,
            llm=GeminiModel
    )

    @task
    def protect_luke_task(self) -> Task:
        return Task(
            config=self.tasks_config['protect_luke_task'],
            agent=self.han(),
            #output_file='app/report.md',
            llm=GeminiModel
    )

    @task
    def destroy_dead_star_task(self) -> Task:
        return Task(
            config=self.tasks_config['destroy_dead_star_task'],
            agent=self.luke(),
            llm=GeminiModel
    )

    @crew
    def crew(self) -> Crew:
        """Creates the Multicrew crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            # process=Process.sequential,
            process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
            manager_llm=GeminiModel,
            verbose=2,
    )
