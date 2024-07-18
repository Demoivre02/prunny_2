
from langchain import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate

# Define our examples
examples = [
    {
        "description": "A young orphan joins a group of wizards as he discovers his magical powers and fights against the dark forces that threaten the wizarding world.",
        "genre": "Fantasy"
    },
    {
        "description": "A group of superheroes must come together to save the world from an alien invasion that threatens to destroy humanity.",
        "genre": "Action"
    },
    {
        "description": "Two strangers meet on a train and develop a romantic relationship as they travel across Europe, exploring different cities and cultures.",
        "genre": "Romance"
    },
    {
        "description": "A brilliant detective and his loyal friend investigate a series of mysterious murders in Victorian London, uncovering a complex conspiracy.",
        "genre": "Mystery"
    },
    {
        "description": "In a post-apocalyptic world, survivors must navigate dangerous terrain and fight off zombies while searching for a safe haven.",
        "genre": "Horror"
    }
]

# Define the prompt template
example_template = """
Description: {description}
Genre: {genre}
"""

example_prompt = PromptTemplate(
    input_variables=["description", "genre"],
    template=example_template
)

# Create the few-shot prompt template
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Classify the genre of a movie based on its description. Here are some examples:",
    suffix="Description: {input}\nGenre:",
    input_variables=["input"],
    example_separator="\n\n"
)

# Example usage
movie_description = "A brilliant mathematician works to crack the Enigma code during World War II, while struggling with his personal life and keeping his sexuality a secret."
print(few_shot_prompt.format(input=movie_description))
