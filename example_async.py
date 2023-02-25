import asyncio
import os

from a3rt_talkpy import AsyncTalkClient

API_KEY = os.environ.get("TALK_API_KEY")

client = AsyncTalkClient(API_KEY)

async def main():
    query = "Is this correctly working?"
    response = await client.talk(query)
    print(response.reply)

if __name__ == "__main__":
    asyncio.run(main())
