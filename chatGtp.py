import datetime
import os
import openai

# OpenAI API key
openai.api_key = "YOU API KEY"


# The function of working with ChatGTP
def get_response_chatgtp(msg):
    engine = "text-davinci-003"
    response = openai.Completion.create(
        engine=engine,
        prompt=msg,
        max_tokens=1024,
        n=1,
        stop=None,
    )
    return response


# Log file recording function
def write_log(msg):
    LOGS_DIR = "logs"
    os.makedirs(LOGS_DIR, exist_ok=True)
    today = datetime.date.today()
    filename = f"{today.strftime('%Y-%m-%d')}.log"
    filepath = os.path.join(LOGS_DIR, filename)
    with open(filepath, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {msg}\n")

# Main
while True:
    user_input = input("\033[;32mI: \033[;0m")
    write_log(f'I: {user_input}')
    response = get_response_chatgtp(user_input)
    print(f"\033[;32mChatGTP:\033[;36m\n{response ['choices'] [0] ['text']}\033[;0m")
    write_log(f'ChatGtp: {response.choices [0].text}')
