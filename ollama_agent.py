from ollama import chat
from pydantic import BaseModel

class Country(BaseModel):
  name: str
  capital: str
  languages: list[str]

def 
response = chat(
  messages=[
    {
      'role': 'user',
      'content': 'Tell me about India.',
    }
  ],
  model='qwen2.5:0.5b',
  format=Country.model_json_schema(),
)

country = Country.model_validate_json(response.message.content)
print(country)