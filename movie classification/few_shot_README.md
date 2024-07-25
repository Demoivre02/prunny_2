# Movie Genre Classifier (Few-Shot Learning)

This script demonstrates a simple movie genre classifier using few-shot learning with LangChain's FewShotPromptTemplate.

## Requirements

- Python 3.7+
- langchain library

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
python few_shot_genre_classifier.py
```

3. The script will output a formatted prompt that can be used with a language model to classify movie genres based on descriptions.

## Customization

You can modify the `examples` list in the script to add or change the few-shot examples used for classification. You can also adjust the `example_template` and `few_shot_prompt` to customize the prompt structure.

## Note

This script doesn't actually perform the classification; it only generates the prompt. To use it for real classification, you'd need to integrate it with a language model API call.
