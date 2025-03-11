import language_tool_python

def check_and_correct(text):
    # Initialize the language tool for US English.
    tool = language_tool_python.LanguageTool('en-US')

    # Correct the text using the instance's correct method.
    corrected_text = tool.correct(text)
    return corrected_text

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    corrected_sentence = check_and_correct(sentence)
    print("Corrected sentence:")
    print(corrected_sentence)
    