There are two basic agents in autogen:
1. UserProxy Agent: This agent acts like a go-between for people. It can ask humans for help or execute code when needed. It can even use LLM to generate responses when it’s not executing code. You can control code execution and LLM usage with settings like code_execution_config and llm_config.
2. Assistant Agent: This agent is like a helpful Strategic AI Team Building assistant. It can write Python code for you to run when you give it a task. It uses a smart program called LLM (like GPT-4) to write the code. It can also check the results and suggest fixes. You can change how it behaves by giving it new instructions. You can also tweak how LLM works with it using the llm_config.
<img width="940" height="669" alt="image" src="https://github.com/user-attachments/assets/f5945dce-220f-44ee-a5d2-c7a936a2049e" />

