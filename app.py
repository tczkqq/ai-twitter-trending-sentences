import json
import sys
import os

from openai import OpenAI
import tweepy

import scraper
import logger


full_path = os.path.realpath(__file__)
path = os.path.dirname(full_path)
with open(path + "/settings.json", "r") as f:
    settings = json.load(f)

if not len(sys.argv) == 2:
    logger.log("Invalid number of arguments. Usage: python app.py <settings name>")
    sys.exit(1)

if not sys.argv[1] in settings:
    logger.log("Invalid argument")
    sys.exit(1)


configuration = settings[sys.argv[1]]

OPENAI_KEY = configuration["OPENAI_KEY"]
X_CONSUMER_KEY = configuration["X_CONSUMER_KEY"]
X_CONSUMER_SECRET = configuration["X_CONSUMER_SECRET"]
X_ACCESS_TOKEN = configuration["X_ACCESS_TOKEN"]
X_ACCESS_TOKEN_SECRET = configuration["X_ACCESS_TOKEN_SECRET"]
TRENDING_URL = configuration["TRENDING_URL"]
AI_SYS_PROMPT = configuration["AI_SYS_PROMPT"]
AI_USR_PROMPT = configuration["AI_USR_PROMPT"]


ai_client = OpenAI(api_key=OPENAI_KEY)
x_client = tweepy.Client(
    consumer_key=X_CONSUMER_KEY,
    consumer_secret=X_CONSUMER_SECRET,
    access_token=X_ACCESS_TOKEN,
    access_token_secret=X_ACCESS_TOKEN_SECRET,
)

words = scraper.get_trending_keywords(TRENDING_URL)
if len(words) < 2:
    logger.log("No enough words found")
    sys.exit(1)

try:
    response = ai_client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": AI_SYS_PROMPT,
            },
            {"role": "user", "content": f"{AI_USR_PROMPT} {words}"},
        ],
    )
    output = response.choices[0].message.content
except Exception as e:
    logger.log(f"AI fail: {e}")


try:
    x_client.create_tweet(text=output)
    logger.log(f"Tweeted: {output}")
except Exception as e:
    logger.log(f"Tweet fail: {e}")
