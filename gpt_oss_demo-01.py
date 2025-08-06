from pydantic_ai import Agent

from gpt_oss_artifacts import get_ollama_model, CityLocation

def main():

    ollama_model = get_ollama_model()

    agent = Agent(ollama_model, output_type=CityLocation)

    result = agent.run_sync('Where were the olympics held in 2012?')

    print(result.output)

    print(result.usage())

if __name__ == "__main__":
    main()