# Text Summarizer

This is a simple text summarization tool that uses a pre-trained BART model to generate summaries of input text.

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory:
   ```
   cd path/to/text-summarizer
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```
   python text_summarizer.py
   ```

2. When prompted, enter the text you want to summarize. Press Enter twice to finish input.

3. The program will generate and display the summary.

4. You can choose to summarize another text or exit the program.

## Notes

- The model used is "suriya7/bart-finetuned-text-summarization" from the Hugging Face model hub.
- The input text should be at least 10 characters long.
- The generated summary is limited to a maximum of 100 tokens.

## Troubleshooting

If you encounter any issues, make sure:
- You have a stable internet connection (required for the first run to download the model).
- You have sufficient disk space and RAM to load the model.
- You've installed all the required dependencies listed in `requirements.txt`.

If problems persist, please check the error message for more details or seek help from the project maintainers.
