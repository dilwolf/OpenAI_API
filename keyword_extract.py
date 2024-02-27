import pandas as pd
import os
import warnings
warnings.filterwarnings(action='ignore')
import openai

# Your API key and DataFrame initialization
OPENAI_API_KEY = " "  # Put your OpenAI API key

df = pd.read_csv('food_article.csv', header=0)
df['keywords'] = ''  # Initialize the keywords column

openai.api_key = OPENAI_API_KEY
model = 'gpt-3.5-turbo-0613'
#model = 'text-davinci-003'

os.makedirs('dataset', exist_ok=True)
csv_file = 'dataset/rows_after_10748_keywords_gpt.csv'

if not os.path.exists(csv_file):
    df.head(0).to_csv(csv_file, index=False, encoding='utf-8-sig')

for idx, row in df.iterrows():
    # Construct the message to ask GPT-3 to extract bio, healthcare, and food related keywords from the summary
    messages = [
        {"role": "system", "content": "You are an intelligent assistant."},
        {"role": "user", "content": f"Extract only 3 keywords related to bio, healthcare, and food from the following summary: '{row['summary']}', and dont write 1: or other numbers, just 3 keywords with comma"}
    ]

    try:
        chat = openai.ChatCompletion.create(model=model, messages=messages)
        reply = chat.choices[0].message.content
        df.at[idx, 'keywords'] = reply  # Update the DataFrame with extracted keywords
        print(f"Processed row {idx}: Extracted keywords: {reply}")

        # Save the updated row to the CSV file
        df.loc[[idx]].to_csv(csv_file, index=False, mode='a', encoding='utf-8-sig', header=False)
        print(f"Saved row {idx} with extracted keywords: {reply}")

    except Exception as e:
        print(f"Error at index {idx}: {e}")
