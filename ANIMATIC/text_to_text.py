import requests
import json


def text_to_text(question):

    prompt = {
        "modelUri": "gpt://b1gm3v3q26f844h37rod/yandexgpt-lite",#b1gtqld3kg7to2drbhru
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },

        "messages": [
            {
                "role": "system",
                "text": "Your name is Peter, you are a voice assistant located in the terminal of Pulkovo airport in St. Petersburg"
            },
            {
                "role": "assistant",
                "text": "Explain to the person at his request how to get to a bus stop, metro or any point in St. Petersburg. Answer completely in English. Answer briefly so that it won't be boring to listen to you"
            },
            {
                "role": "user",
                "text": question
            }
        ]

        # "messages": [
        #     {
        #         "role": "system",
        #         "text": "Привет, я искусственный интеллект, зовут Пётр. Помогаю туристам в аэропорту Пулково в городе Санкт-Петербург, адаптируюсь к вашему языку. Объяснять туристу ты должен как ребёнку, чтобы ему было понятно.Ответ должен быть полным"
        #     },
        #     {
        #         "role": "assistant",
        #         "text": "Сгенерируй текст с помощью туристу на его вопрос. Твой ответ должен быть сплошным тестом до 200 симолов, текст должен быть голым, для простого его распознавания. Удали из текста все ссылки. Путь нужно описать точно и коротко"
        #     },
        #     {
        #         "role": "user",
        #         "text": question
        #     }
        # ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNz0ez4D8Eh8QnUUzgnGdPGn5b7fJzZBGRztFC"# AQVN0m68cAC6dKMy4nlpUYbzyYMlZYitACpHykHG
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    # print(result)
    return result["result"]["alternatives"][0]["message"]["text"]


# print(text_to_text("приветик"))