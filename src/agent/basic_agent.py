from agents import Agent, Runner, WebSearchTool
from agents import set_default_openai_key
import src.common.furniture.furniture_prompts as prompts
from src.common.furniture.furniture_details import items
from config import settings

set_default_openai_key(settings.openai_key)


url = items[0]['url']
item_name = item=items[0]['name']
print(url, item_name)

prompt = prompts.get_price.format(url=url, item=item_name)

# print(prompt)

print(f"Approximate Tokens: {len(prompt)/4}")


agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant that finds pricing information on web pages.",
    # model=
    tools = [WebSearchTool()]
    )

result = Runner.run_sync(agent, prompt)
print(result)
print(result.final_output)
usage = result.context_wrapper.usage

print("Requests:", usage.requests)
print("Input tokens:", usage.input_tokens)
print("Output tokens:", usage.output_tokens)
print("Total tokens:", usage.total_tokens)

