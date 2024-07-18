from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_model():
    print("Loading model... This may take a moment.")
    tokenizer = AutoTokenizer.from_pretrained("suriya7/bart-finetuned-text-summarization")
    model = AutoModelForSeq2SeqLM.from_pretrained("suriya7/bart-finetuned-text-summarization")
    print("Model loaded successfully.")
    return tokenizer, model

def generate_summary(text, tokenizer, model):
    try:
        inputs = tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
        summary_ids = model.generate(inputs['input_ids'], max_new_tokens=100, do_sample=False)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        print(f"An error occurred while generating the summary: {str(e)}")
        return None

def get_user_input():
    print("Enter your text below (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("Text Summarizer")
    print("---------------")

    tokenizer, model = load_model()

    while True:
        user_input = get_user_input()

        if len(user_input.strip()) == 0:
            print("Error: Empty input. Please enter some text to summarize.")
        elif len(user_input) < 10:
            print("Error: Input text is too short. Please enter at least 10 characters.")
        else:
            print("Generating summary...")
            summary = generate_summary(user_input, tokenizer, model)
            
            if summary:
                print("\nSummary:")
                print(summary)

        retry = input("\nDo you want to summarize another text? (yes/no): ").lower()
        if retry != 'yes' and retry != 'y':
            break

    print("Thank you for using the Text Summarizer!")

if __name__ == "__main__":
    main()
