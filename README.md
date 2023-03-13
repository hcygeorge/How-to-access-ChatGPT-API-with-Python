# How to access ChatGPT API with Python

目前OpenAI已釋出ChatGPT API服務，支援使用Python與ChatGPT對話。
API主要採用字數計費，而一個帳號每月有18USD的免費額度，如有大量需求可自行申請付費方案，以下提供API的使用方法。

## 事前準備

請先安裝OpenAI library
```bash
pip install openai
```

到OpenAI網站申請api-key\
https://platform.openai.com/account/api-keys


## 腳本說明

- 一次性對話請用one_turn.py
- 多輪式對話請用multi_turn.py

## 操作範例
```bash
python3 one_turn.py --key "Your API-key" --prompt "太平天國的勢力範圍有多大?"
```

>You: 太平天國的勢力範圍有多大?
>
>反應時間：6.49 秒\
>ChatGPT:\
>太平天國在中國的勢力範圍遍及華南、華中、華北等地，包括湖南、江西、安徽、浙江、江蘇、河南、河北、山東等省份，並且曾經進攻到了京師（北京）。據估計，太平天國的勢力範圍最大時曾達到占中國一半以上的領土。
>
>本次對話統計:\
>問題字數: 25\
>回答字數: 139\
>總字數: 164\
>對話成本: 0.0003 USD (0.0098 NTD)
