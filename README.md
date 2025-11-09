# October Learning Challenges

## To Dos
	[ ] Github Actions
		use github actions to:
			[x] add linting and other tests to github so that we can prove that things work before
			they get moved into the codebase deploy the code to w/e we choose (probably containers)
			
			[ ] What do I need to understand:
				[ ] You need to understand exactly what it's for.
				[ ] What we can do with it.
				[x] How to implement using Github runners
				[ ] How to implement using our own runners
				
	[ ] Pre-commit
		[ ] use ruff to make checks and reformat code before it is commited.
		[ ] the precommit should be supported by both the agents and yourself.
		
	implement mcp:
		[ ] to allow an llm to connect to a postgres db
		[ ] to allow an llm to connect to a SQL Server db
		[ ] to interact with an api
		
	deploy an agent:
		to understand how you do that
			[x] watch youtube agent video
			[ ] participate in Kaggle / Google Agent stuff
		

		
	implement a multiple agent architecture

## Get Prices Agent
[ ] Determine which framework to use.
- Google
- OpenAI - tested
- LangChain
- Strands (AWS)
### Single Agent
[x] Find the Price of an item.\
[ ] Update a file with that item.\
[ ] Update a database table with that item.\
[ ] Update a google sheet with that item.
### Multi-Agent
[ ] Find the Price of an item.\
[ ] Update a file with that item.\
[ ] Update a database table with that item.\
[ ] Update a google sheet with that item.

## Reading Items
[ ] [Learn X in Y Minutes](https://learnxinyminutes.com/yaml/)
- This is a pretty handy site that has very concise explanations of different languages
and mark up. I used it to get up to speed on YAML.
	
[x] [OpenAI Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)


[ ] [LangChain Agent Tutorial](https://python.langchain.com/docs/tutorials/agents/#:~:text=LangChain%20supports%20the%20creation%20of,often%20achieved%20via%20tool%2Dcalling.)

[x] [Microsoft Agent Framework](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-get-started)
- This is GUI based and not really my bag.

[ ] [Claude Web Search API](https://www.anthropic.com/news/web-search-api)

[x] [Gemini Web Serch](https://ai.google.dev/gemini-api/docs/google-search#:~:text=While%20the%20google_search%20tool%20is%20recommended%20for,and%201.0%2C%20it%20will%20perform%20a%20search.)

[x] [OpenAI Web Search](https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses)

[x] [Agent2Agent Announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)

### AWS Specific Readings
[ ] [Dev To Agent Tutorials](https://dev.to/aws-builders/tutorial-build-an-agentic-ai-application-with-agents-for-amazon-bedrock-2cpk)

[x] [Building your first production-ready AI agent with Amazon Bedrock AgentCore](https://m.youtube.com/watch?v=wzIQDPFQx30)

[ ] [Amazon Bedrock Agents](https://github.com/build-on-aws/amazon-bedrock-agents-quickstart)

[ ] [Bedrock Samples and Tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples)

[ ] [How I came in first on ARC-AGI-Pub](https://jeremyberman.substack.com/p/how-i-got-a-record-536-on-arc-agi)

[ ] [How I got the highest score on ARC-AGI again](https://jeremyberman.substack.com/p/how-i-got-the-highest-score-on-arc-agi-again)

### Model Evaluation
I want to determinine which models make sense to use from an API standpoint. I'd like to try all of the ones that I can out and API is going to be my first stab at this. Down the road I'll try this with an OpenSource Model that does not have an API.

I am looking for models which allow search in the API and that have memory if at all possible. Does search cost more money than no search?

### [Gemini]()
[x] Has Search

### [OpenAI]()
[x] Has Search

### [Claude]()
[x] Has Serch
