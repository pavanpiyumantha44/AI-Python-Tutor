from groq import Groq, AuthenticationError, RateLimitError, APIConnectionError
from config import groq_api_key, model

client = Groq(api_key=groq_api_key)

system_prompt = {
                    "role":"system",
                    "content": """
                                You are a Python programming assistant.
                                IMPORTANT : Answer questions only related to Python programming.
                                If a question is unrelated to Python programming, politely explain that you can only assist with Python-related topics.
                            """
                }

conversations = [system_prompt]

def generate_prompts(role:str,message:str)->dict[str,str]:
    return {
        "role":role,
        "content" : message
    }

def generate_response(conversations:list[dict[str, str]])-> str| None:
    try:
        response = client.chat.completions.create(
            messages=conversations,
            model=model
        )
        return response.choices[0].message.content
    
    except AuthenticationError:
        print("Invalid API key!")

    except RateLimitError:
        print("Rate limit exceeded. Try again later.")

    except APIConnectionError:
        print("Unable to connect to Groq.")

    except Exception as e:
        print(f"Unexpected error: {e}")

def run_chatbot():
    user_input=""
    print("""
            =============================Welcome To Python ChatBot=============================\n
            ==========You can ask any question related to python programming language==========\n
            ===================================================================================
        """
        )
    while True:
        user_input = input("You : ").strip()
        if user_input:
            if user_input.lower() == "/bye":
                break
            user_prompt = generate_prompts("user",user_input)
            conversations.append(user_prompt)

            response = generate_response(conversations)
            if not response:
                conversations.pop()
                continue
            print(f"Python Bot : {response}")

            ai_response = generate_prompts("assistant",response)
            conversations.append(ai_response)