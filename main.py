import openai
import os, time

# 设置OpenAI API密钥
openai.api_key = os.environ["OPENAI_API_KEY"]

# 发送请求并获取响应
def generate_response(prompt):
    # 调用OpenAI GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    conversation_id = response["id"]
    print("Conversation ID:",conversation_id)
    return response.choices[0].text.strip(), conversation_id

# 测试
prompt = "你好，請用繁體中文自我介紹"
response = generate_response(prompt)
print(response[0])

while True:
    # 获取用户输入
    user_input = input("You: ")

    # 发送用户输入到OpenAI API
    response = openai.Conversation.append(
        conversation_id=response[1],
        engine="text-davinci-002",
        prompt=user_input,
        temperature=0.5,
    )

    # 输出OpenAI API的生成结果
    print("AI: " + response.choices[0].text)

    # 暂停1秒
    time.sleep(1)




