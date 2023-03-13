import openai
import time

# 填寫你的API key
openai.api_key = "attach your api key here"

# 定義函數
def get_content(response, sep='\n'):
    """從API response取得回答內容，並依據sep分割字串"""
    return dict(dict(dict(response)['choices'][0])['message'])['content'].split(sep)

def billing(response, price=0.002, tokens=1000, rate=30):
    """計算一次ChatGPT API對話成本(按字數計費)
    
    對話成本 = ((問題+回答字數) * price) * rate / tokens
    """
    usage = dict(dict(response)['usage'])
    cost = (usage['total_tokens'] * price) / tokens
    
    print('\n本次對話統計:')
    print('問題字數: {}'.format(usage['prompt_tokens']))
    print('回答字數: {}'.format(usage['completion_tokens']))
    print('總字數: {}'.format(usage['total_tokens']))
    print(f'對話成本: {cost:.4f} USD ({cost*rate:.4f} NTD)')

def timing_decorator(func):
    """計算函數執行時間"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} 函數執行時間：{execution_time:.2f} 秒")
        return result
    return wrapper

@timing_decorator
def call_chatgpt(messages, temperature=1):
    """呼叫ChatGPT API"""
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature
    )

def print_answer(response):
    """列印ChatGPT回答"""
    print('\nChatGPT:')
    for sen in get_content(response):
        if sen == '':
            continue
        print(sen)

if __name__ == '__main__':
    # 提示(給ChatGPT的命令)
    propmt = [
        {"role": "user", "content": "請問澳洲有多少人?"},
        {"role": "user", "content": "請分別用繁體中文和英文回答"},
        ]

    response = call_chatgpt(propmt)
    billing(response)
    print_answer(response)