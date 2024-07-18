
import os
import re
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# Define our examples
examples = [
    {"description": "A young orphan joins a group of wizards as he discovers his magical powers and fights against the dark forces that threaten the wizarding world.", "genre": "Fantasy"},
    {"description": "A group of superheroes must come together to save the world from an alien invasion that threatens to destroy humanity.", "genre": "Action"},
    {"description": "Two strangers meet on a train and develop a romantic relationship as they travel across Europe, exploring different cities and cultures.", "genre": "Romance"},
    {"description": "A brilliant detective and his loyal friend investigate a series of mysterious murders in Victorian London, uncovering a complex conspiracy.", "genre": "Mystery"},
    {"description": "In a post-apocalyptic world, survivors must navigate dangerous terrain and fight off zombies while searching for a safe haven.", "genre": "Horror"}
]

def get_user_input():
    """
    Prompts the user to enter a movie description and returns it.
    """
    while True:
        description = input("Please enter a short movie description (or 'quit' to exit): ").strip()
        if description.lower() == 'quit':
            return None
        if len(description) > 0:
            return description
        print("Please enter a valid description.")

def parse_genre(response):
    """
    Parses the model's response to extract the predicted genre.
    """
    # Remove any punctuation and convert to lowercase
    cleaned_response = re.sub(r'[^\w\s]', '', response.lower())
    
    # Split the response into words and take the first word as the genre
    words = cleaned_response.split()
    if words:
        return words[0].capitalize()
    return None

def classify_movie_genre(description, chain):
    """
    Classifies the genre of a movie based on its description using the LLMChain.
    """
    try:
        result = chain.run(input=description)
        parsed_genre = parse_genre(result.strip())
        return parsed_genre if parsed_genre else "Unknown"
    except Exception as e:
        print(f"An error occurred while classifying the movie genre: {e}")
        return "Unknown"

def create_chain():
    """
    Creates and returns the LLMChain for movie genre classification.
    """
    # Initialize the language model
    llm = ChatOpenAI(temperature=0)

    # Create the prompt template
    system_template = """You are a movie genre classifier. Your task is to classify the genre of a movie based on its description.
Here are some examples:

{examples}

Please classify the following movie description into a single genre. Respond with only the genre name."""

    human_template = "{input}"

    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    # Create an LLMChain using the chat prompt and the language model
    return LLMChain(llm=llm, prompt=chat_prompt)

def main():
    # Check if the OpenAI API key is set
    if "OPENAI_API_KEY" not in os.environ:
        print("Please set your OpenAI API key as an environment variable named OPENAI_API_KEY.")
        return

    # Create the LLMChain
    chain = create_chain()

    # Format the examples as a string
    examples_str = "\n".join([f"Description: {ex['description']}\nGenre: {ex['genre']}" for ex in examples])

    # Set the examples in the chain's memory
    chain.prompt.format(examples=examples_str)

    print("Welcome to the Movie Genre Classifier!")
    print("This program uses AI to predict the genre of a movie based on a short description.")
    
    while True:
        description = get_user_input()
        if description is None:
            break

        genre = classify_movie_genre(description, chain)
        print(f"\nMovie description: {description}")
        print(f"Predicted genre: {genre}")
        print()  # Add a blank line for readability

    print("Thank you for using the Movie Genre Classifier!")

if __name__ == "__main__":
    main()
