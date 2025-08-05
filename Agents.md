There are two basic agents in autogen:
1. UserProxy Agent: This agent acts like a go-between for people. It can ask humans for help or execute code when needed. It can even use LLM to generate responses when it’s not executing code. You can control code execution and LLM usage with settings like code_execution_config and llm_config.
2. Assistant Agent: This agent is like a helpful Strategic AI Team Building assistant. It can write Python code for you to run when you give it a task. It uses a smart program called LLM (like GPT-4) to write the code. It can also check the results and suggest fixes. You can change how it behaves by giving it new instructions. You can also tweak how LLM works with it using the llm_config.
<img width="940" height="669" alt="image" src="https://github.com/user-attachments/assets/f5945dce-220f-44ee-a5d2-c7a936a2049e" />

#1
 interviewer = AssistantAgent(
        name="Interviewer",
        model_client=model_client,
        description=f"An AI agent that conducts interviews for a {job_position} position.",
        system_message=f'''
        You are a professional interviewer for a {job_position} position.
        Ask one clear question at a time and Wait for user to respond. 
        Your job. is to continue and ask questions, don't pay any attention to career coach response. 
        Make sure to ask question based on Candidate's answer and your expertise in the field.
        Ask 3 questions in total covering technical skills and experience, problem-solving abilities, and cultural fit.
        After asking 3 questions, say 'TERMINATE' at the end of the interview.
        Make question under 50 words.
    '''
    )
   
#2
    candidate = UserProxyAgent(
        name = "candidate",
        description=f"An agent that simulates a candidate for a {job_position} position.",
        input_func=input
    )

#3
    career_coach = AssistantAgent(
        name="Career_Coach",
        model_client=model_client,
        description=f"An AI agent that provides feedback and advice to candidates for a {job_position} position.",
        system_message=f'''
        You are a career coach specializing in preparing candidates for {job_position} interviews.
        Provide constructive feedback on the candidate's responses and suggest improvements.
        After the interview, summarize the candidate's performance and provide actionable advice.
        Make it under 100 words.
    '''
    )
