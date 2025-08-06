from pydantic_ai import Agent

from gpt_oss_artifacts import get_ollama_model, CityLocationFull

def main():

    ollama_model = get_ollama_model()

    agent = Agent(ollama_model, output_type=list[CityLocationFull])

    @agent.tool_plain()
    def get_olympic_special_gift(olympic_year: int) -> str:
        """
        Returns the special gift that was given to all athletes during the Olympics closing ceremony
        for the specified Olympic year, between 2000 and 2024.

        Args:
            olympic_year (int): The year of the Olympic Games (e.g., 2008, 2012, 2016).

        Returns:
            str: The name of the special gift given in the specified year.

        Raises:
            KeyError: If the olympic_year is not in the list of known years (2000–2024).
        """
        gifts = {
            2000: "GPT Credits",
            2004: "OpenAI Tokens",
            2008: "Nike Shoes",
            2012: "Diamond Bracelet",
            2016: "Silver Necklace",
            2020: "Sushi Jar",
            2024: "Eiffel Tower"
        }

        return gifts[olympic_year]

    result = agent.run_sync('Where was the olympics held in 2024 and what special gifts did the athletes receive?')

    print(result.output)

    print(result.usage())

if __name__ == "__main__":
    main()