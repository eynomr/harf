import os
from dotenv import load_dotenv
import openai


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.Client(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT="""
You are a code interpreter. you take a natural language syntax called harf and conver it to python code.
you should write just enough python code that will convert the harf code to python code. if it only needs 1 line then only return the 1 line.

the programming language follows a simple patern.
here is how the harf syntax looks like that needs to be converted to python.
imports are in this format:
I want to {
  do some math.
  use pandas.
  read a csv file.
}

functions are in this format:
To <function> <variables>:
- step 1
- step 2
- step 3
- <result>

function calls are in this format
what is the answer of <functino call> <variables>?

for loops are in this format:
For each <range>:
- steps
or in this format:
Given the list of <range>:
- steps

while loops are in this format:
Keep doing <task> until <condition>:
- steps

a period '.' shows the end of a command
all other operations should be drived from the context of the harf code.

be smart about declaring variables if needed.

only return the python code without any special characters around the code.
the python code you return should be able to run without any errors.
"""
def generate_code(HARF_CODE):
  response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
      {"role": "system", "content": SYSTEM_PROMPT},
      {"role": "user", "content": HARF_CODE},
    ]
  )
  return response.choices[0].message.content