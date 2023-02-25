from a3rt_talkpy import TalkClient
import os

API_KEY = os.environ.get("TALK_API_KEY")

client = TalkClient(API_KEY)

def main():
    query = "Is this correctly working?"
    response = client.talk(query)
    print(response.reply)

if __name__ == "__main__":
    main()
