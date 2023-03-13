# How to access ChatGPT API with Python

目前OpenAI已釋出ChatGPT API服務，支援使用Python與ChatGPT對話。
API主要採用字數計費，而一個帳號每月有18USD的免費額度，如有大量需求可自行申請付費方案。

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

## 使用方法
```bash
python3 one_turn.py --key "API key" --prompt "太平天國的勢力範圍有多大?"
```