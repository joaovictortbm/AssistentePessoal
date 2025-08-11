import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain_experimental.utilities import PythonREPL
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain import hub
from langchain_community.utilities import SQLDatabase

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def create_agent():

    model = ChatOpenAI(model_name="gpt-4o-mini")

    # Loading database
    db = SQLDatabase.from_uri("sqlite:///data/northwind.db")

    pythonREPL = PythonREPL()
    python_repl_tool = Tool(
        name="python REPL",
        func=pythonREPL.run,
        description="Um ambiente interativo para executar código Python de forma segura e rápida. Use esta ferramenta para realizar cálculos, manipulação e análise dos dados da empresa, como sumarização, filtragem, cálculos financeiros, transformações, etc. Ideal para quando precisar processar informações complexas ou gerar insights baseados nos dados SQL disponíveis.",
    )

    toolkit = SQLDatabaseToolkit(db=db, llm=model)

    tools = toolkit.get_tools() + [python_repl_tool]
    react_instructions = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=model,
        tools=tools,
        prompt=react_instructions,
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
    )

    return agent_executor
