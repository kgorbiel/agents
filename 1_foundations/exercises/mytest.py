from dotenv import load_dotenv
from openai import OpenAI
from openai import Client
import os

load_dotenv(override=True)

# openai = OpenAI()


# messages = [{"role": "user", "content": "Pick a business area that might be worth exploring for an Agentic AI opportunity."}]

client = OpenAI()
response = client.responses.create(model="gpt-4.1-mini", input="Propose an AI agentic solution for the development team in insurance industry working on solutions related to claims processing.")
print(response.output_text)


# response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)

# business_idea = response.choices[0].message.content
# print(f"Business idea: {business_idea}")

# messages = [{"role": "user", "content": f"Present a pain-point in the {business_idea} industry - something challenging that might be ripe for an Agentic solution."}]
# response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)

# pain_point = response.choices[0].message.content
# print(f"Pain point: {pain_point}")

# messages = [{"role": "user", "content": f"Propose a solution to the pain-point: {pain_point} in the {business_idea} industry."}]

# response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)

# solution = response.choices[0].message.content
# print(f"Solution: {solution}")
