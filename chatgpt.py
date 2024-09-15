import openai
#https://platform.openai.com/account/api-keys
#pip install openai
#pip3 install openai
openai.api_key = 'TUA_CHAVE_API'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="babbage-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
print("\033c\033[40;37m")
while True:
    user_input = input("you: ")
    if user_input.lower() == "out":
        break
    response = chat_with_gpt(user_input)
    print("ChatGPT: " + response)
