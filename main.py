from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompt_setter import prompt, agent_instruction, context
from md_noter import md_noter
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
from pdf_reader import canada_engine

# loading our api keys
load_dotenv()

bitcoin_price = os.path.join("data/BTC.csv")
bitcoin_df = pd.read_csv(bitcoin_price)

bitcoin_query_engine = PandasQueryEngine(df=bitcoin_df, verbose=True, instruction=agent_instruction)

bitcoin_query_engine.update_prompts({"pandas_prompt": prompt})
# print(bitcoin_query_engine.query('what was the highest bitcoing price?')) #testing how query works


tools = [
    md_noter,
    QueryEngineTool(
        query_engine=bitcoin_query_engine,
        metadata=ToolMetadata(
            name="bitcoin_data",
            description="this gives information about bitcoin prices at specific dates",
        ),
    ),

    QueryEngineTool(
        query_engine=canada_engine,
        metadata=ToolMetadata(
            name="ukraine_data",
            description="this gives all information about ukraine",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-0125")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt> ")) != "q":
    result = agent.query(prompt)
    print(result)