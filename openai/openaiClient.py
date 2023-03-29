import os
import openai

openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_KEY")

# get models
# status = openai.Model.list()
# for el in status.data:
#     print(el.id)


res = openai.Completion.create(
    model="text-davinci-003",
    prompt="can you give a summary of rfc 7950",
    temperature=0.2,
    echo=True,
)

res2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "can you give me a summary of rfc 7950",
        }
    ],
    temperature=0.2,
)

print(res)
print(res2)

# import aiohttp
# import asyncio

# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, 'https://www.example.com')
#         print(html)

# asyncio.run(main())
