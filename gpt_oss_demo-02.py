from pydantic_ai import Agent

from gpt_oss_artifacts import get_ollama_model, CityLocationYear


def main():

    ollama_model = get_ollama_model()

    agent = Agent(ollama_model, output_type=list[CityLocationYear])

    result = agent.run_sync('Where were the olympics held in 2008, 2012 and 2016?')

    print(result.output)

    print(result.usage())

if __name__ == "__main__":
    main()