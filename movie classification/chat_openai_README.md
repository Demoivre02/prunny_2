# Movie Genre Classifier (ChatOpenAI)

This script implements a movie genre classifier using LangChain's ChatOpenAI model. It allows users to input movie descriptions and receive predicted genres based on the input.

## Requirements

- Python 3.7+
- langchain library
- openai library

## Installation

1. Clone this repository or download the script.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Make sure you have set up your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

2. Run the script:

```bash
python chat_openai_genre_classifier.py
```

3. Follow the prompts to enter movie descriptions. The script will classify each description and output the predicted genre.

4. Type 'quit' when prompted for a description to exit the program.

## Customization

You can modify the `examples` list in the script to add or change the few-shot examples used for classification. You can also adjust the `system_template` to customize the prompt structure.

## Note

This script requires an active internet connection to communicate with the OpenAI API for classification.
