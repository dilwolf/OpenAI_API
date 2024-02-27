This repository contains two Python scripts, `keyword_extract.py` and `OpenAI_chat_bot.py`, designed to leverage OpenAI's GPT models for various text-related tasks. Below is a brief overview of each script's functionality:


**AI-Assisted-Keyword-Extraction**

---
### `keyword_extract.py`

This script utilizes OpenAI's GPT-3.5 model to extract keywords related to bio, healthcare, and food from a provided summary. It demonstrates how to integrate OpenAI's ChatCompletion API for natural language processing tasks. Key features include:

- Extraction of keywords from textual summaries using GPT-3.5
- Integration with Pandas for efficient data handling
- Creation of a CSV dataset storing extracted keywords

**AI-Assisted-Chat-Bot**

---
### `OpenAI_chat_bot.py`

In this script, OpenAI's GPT-3.5 model is employed to build a very simple chatbot interface. Users can engage in conversations with the chatbot, and responses are generated based on the input provided. Features include:

- Implementation of a conversational interface using GPT-3.5
- Integration with OpenAI's ChatCompletion API for generating responses
- User-friendly interface for interactive communication with the chatbot

---
**Usage**

To utilize these scripts effectively, follow the steps below:

1. **OpenAI API Key Setup**: Ensure you have an OpenAI API key and replace the placeholder with your actual key in both scripts.
   
2. **Data Input (for `keyword_extract.py`)**: Provide a CSV file containing summaries from which keywords are to be extracted. Ensure the summary column is labeled appropriately in the CSV file.

3. **Execution**: Run the respective Python scripts (`keyword_extract.py` for keyword extraction, `OpenAI_chat_bot.py` for chatbot interaction) in your preferred environment.

4. **Interaction (for `OpenAI_chat_bot.py`)**: Engage with the chatbot by inputting messages when prompted. To exit the chat, type "quit", "exit", or "bye".

5. **Output (for `keyword_extract.py`)**: Check the generated CSV file in the `dataset` directory for extracted keywords corresponding to each summary.

---
**Note**: Ensure dependencies such as Pandas and OpenAI's `openai` library are installed in your Python environment to execute these scripts successfully. For further details on installation and usage, refer to the documentation of these dependencies.

For any inquiries or support, feel free to reach out to the repository maintainers.

Happy coding! 🚀