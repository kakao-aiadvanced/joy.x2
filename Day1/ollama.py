import requests

system = """
You are a classifier.
For each question, tell me which of the two characters you think will give a better answer to the question.

Here are two characters.
[Math Teacher]
I majored in math in college and now teach high school math.
I can provide logical explanations for all fields of natural science.
On the other hand, I tend to find emotional or philosophical questions difficult.

[History Teacher]
I majored in math in college and now teach history in high school.
I am very knowledgeable about world history, national history, and world geography.

Here are examples.
Question: What is Newton's law?
Answer: Math Teacher would give a better answer. As a math teacher, he must have been exposed to a lot of science as well as math while majoring in math at university. Also, a math teacher would be better at answering this question because Newton was both a scientist and a mathematician.

Question: What flowers bloom most often in summer in Korea?
Answer: I don't think either of these characters would be able to help you with this question. It is unclear whether both characters know much about flowers or not. Also, since I don't know which country the two characters are from, I can't tell if they know much about Korea.
"""

question = "Who is the greatest mathematician in the world?"

res = requests.post('http://localhost:11434/api/generate', json={
  "model": "llama3",
  "system": system,
  "prompt": question,
  "stream": False
}).json()
print (res.get('response'))
