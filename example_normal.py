import os

from a3rt_talkpy import TalkClient

API_KEY = os.environ.get("TALK_API_KEY")
if API_KEY is None:
    raise ValueError("API_KEY is not set")

client = TalkClient(API_KEY)

def main():
    query = "おはようございます"
    response = client.talk(query)
    print(response.reply)

if __name__ == "__main__":
    main()
