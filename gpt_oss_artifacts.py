from typing_extensions import Literal
from pydantic import BaseModel

from pydantic_ai.models.openai import OpenAIModel, OpenAIResponsesModelSettings
from pydantic_ai.providers.openai import OpenAIProvider

SpecialModelName = Literal['gpt-oss:20b', 'gpt-oss:120b']

class CityLocation(BaseModel):
    city: str
    country: str

class CityLocationYear(BaseModel):
    city: str
    country: str
    year: int

class CityLocationFull(BaseModel):
    city: str
    country: str
    year: int
    special_gift: str

def get_ollama_model() -> OpenAIModel:

    ollama_endpoint = "http://192.168.86.43:11434/v1"
    ollama_settings = OpenAIResponsesModelSettings(openai_reasoning_effort='low', openai_reasoning_generate_summary='detailed')
    ollama_model_name: SpecialModelName = 'gpt-oss:20b'
    ollama_provider = OpenAIProvider(base_url=ollama_endpoint)
    ollama_model = OpenAIModel(model_name=ollama_model_name, provider=ollama_provider, settings=ollama_settings)

    return ollama_model