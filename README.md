# Twitter AI sentences based on trends

Twitter bot that use Open AI to make sentences from trending words and publish them. Trends are scraped from trends24.in website cuz twitter api is crazy expensive xD.

## Requirements

- python3
- requests
- bs4
- tweepy
- openai

## Usage

1. Setup `settings.json`

```json
{
  "conf1": {
    "OPENAI_KEY": "get from https://platform.openai.com/api-keys",
    "X_CONSUMER_KEY": "get from https://developer.twitter.com/en/portal/dashboard",
    "X_CONSUMER_SECRET": "get from https://developer.twitter.com/en/portal/dashboard",
    "X_ACCESS_TOKEN": "get from https://developer.twitter.com/en/portal/dashboard",
    "X_ACCESS_TOKEN_SECRET": "get from https://developer.twitter.com/en/portal/dashboard",
    "TRENDING_URL": "trends24.in/<Your country>",
    "AI_SYS_PROMPT": "Translate prompt for your language",
    "AI_USR_PROMPT": "Translate prompt for your language"
  }
}
```

2. Run script `python3 app.py <configuration name>` f.e `python3 app.py conf1`

3. \*Setup cron job

## Examples

- [US Version](https://twitter.com/TrendSentenceUS)
- [UK Version](https://twitter.com/TrendSentenceUK)
- [PL Version](https://twitter.com/TrendSentencePL)
