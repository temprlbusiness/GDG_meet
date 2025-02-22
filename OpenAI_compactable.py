from ollama import chat
from pydantic import BaseModel
from langchain_community.tools import DuckDuckGoSearchRun
from openai import OpenAI
from langchain_community.utilities import OpenWeatherMapAPIWrapper

class Identifier(BaseModel):
  is_search: bool
  is_weather: bool

class Weather(BaseModel):
  place: str

client = OpenAI(
    base_url='<OPENAI_BASE_URL>',
    # required but ignored
    api_key='<OPENAI_API_KEY>',
)


WEATHER_PROMPT = """
  You are a agent good in finding places from the user's query.
  User's query: {user_input}
  Place:
"""

IDENTIFIER_PROMPT = """
  User's query: {user_input}

  You are an agent specialized in query classification.
  Your task is to determine if the user's query requires an internet search.
  
  Guidelines:
  - Classify as search true if the query is general knowledge (e.g. "Who is...", "What is...", "When did...")
  - Classify as search if the query asks about facts, history, or current events
  - Do not classify as search if the query is about weather or local conditions
  - Classify as weather if the query asks about temperature, precipitation, or weather conditions
  - Classify as weather if the query mentions forecast, weather, rain, sun, etc.
  - Classify as weather if the query asks about current or future weather conditions for a location
  
  Analyze the query and determine if it requires searching the internet.
"""

#--------------------------------------Functions--------------------------------------
def search(user_input: str):
  search = DuckDuckGoSearchRun()

  search = search.invoke(user_input)
  return search

def weather_call(user_input: str):
  # Importing necessary libraries

  weather = OpenWeatherMapAPIWrapper(openweathermap_api_key="f321902e1472611b6574e8b293b256ad")  

  weather_call = weather.run(user_input)
  return weather_call

#--------------------------------------Completion--------------------------------------
def struct_completion(AgentClass: BaseModel, user_input: str):
    response = client.beta.chat.completions.parse(
        model='deepseek-r1:1.5b',
        messages=[
            {'role': 'user', 'content': user_input}
        ],
        response_format=AgentClass,
    )

    print(response.choices[0].message.content)
    filtered_response = AgentClass.model_validate_json(response.choices[0].message.content)
    return filtered_response
  
def completion(user_input: str):
  response = client.chat.completions.create(
        model='deepseek-r1:1.5b',
        messages=[
            {'role': 'user', 'content': user_input}
        ]
    )
  return response.message.content

#--------------------------------------Main--------------------------------------

user_input = input("Enter your query: ")

identifier = struct_completion(Identifier, IDENTIFIER_PROMPT.format(user_input=user_input))
print(identifier)

if identifier.is_search:
  search_result = search(user_input)
  final_result = completion(f"from the given search result {search_result}, summarize the search result. do not add any other text except the search summary.")
  print(final_result)

if identifier.is_weather:
  print("Weather Agent is working...")
  weather_place = struct_completion(Weather, WEATHER_PROMPT.format(user_input=user_input))
  weather_result = weather_call(weather_place.place)
  print(weather_result)
  final_result = completion(f"The weather in {weather_place.place} is {weather_result}. from the given weather result, summarize the weather in {weather_place.place}. do not add any other text except the weather summary.")

  print(final_result)

