import os
import openai
openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_KEY")

status = openai.Model.list()

print(status)