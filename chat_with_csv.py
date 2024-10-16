# -*- coding: utf-8 -*-
"""Chat_with_CSV.ipynb


"""

!pip install pandas openpyxl langchain openai python-dotenv langchain_openai

import os
import pandas as pd
from google.colab import files
from langchain_openai import AzureChatOpenAI
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from openai import BadRequestError
import time

def upload_file():
    uploaded = files.upload()
    filename = next(iter(uploaded))
    return filename

def read_file(filename):
    if filename.endswith('.xlsx'):
        return pd.read_excel(filename)
    elif filename.endswith('.csv'):
        return pd.read_csv(filename)
    else:
        raise ValueError("Unsupported file format. Please use .xlsx or .csv")

def setup_llm_chain():
    os.environ["OPENAI_API_TYPE"] = "place your OPENAI_API_TYPE"
    os.environ["OPENAI_API_VERSION"] = "place your OPENAI_API_VERSION"
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://YourOPENAI_ENDPOINT.com/"
    os.environ['AZURE_OPENAI_API_KEY'] = "Your OpenAI API Key"

    llm = AzureChatOpenAI(
        deployment_name="gpt-4o-mini",
        temperature=0.3,
        max_tokens=150,
        openai_api_version="2024-08-01-preview"
    )

    prompt = PromptTemplate(
        input_variables=["comment"],
        template="Analyze the sentiment and emotion of the following comment. Provide a brief, professional response based on the sentiment, avoiding any inappropriate or harmful content: {comment}"
    )
    return LLMChain(llm=llm, prompt=prompt)

def process_comments(df, chain):
    responses = []
    filtered_count = 0
    for i, comment in enumerate(df['FBPost']):
        try:
            response = chain.run(comment)
            responses.append(response)
        except BadRequestError as e:
            print(f"Comment {i+1} was filtered due to content policy. Skipping.")
            responses.append("Comment filtered due to content policy.")
            filtered_count += 1
        except Exception as e:
            print(f"Error processing comment {i+1}: {str(e)}")
            responses.append("Error processing comment.")

        if (i+1) % 10 == 0:
            print(f"Processed {i+1} comments. {filtered_count} comments filtered.")
            time.sleep(1)  # Add a small delay to avoid rate limiting

    df['response'] = responses
    print(f"Processing complete. Total comments filtered: {filtered_count}")
    return df

def main():
    print("Please upload your Excel or CSV file.")
    input_file = upload_file()

    print("Reading the file...")
    df = read_file(input_file)

    print("Setting up the language model...")
    chain = setup_llm_chain()

    print("Processing comments...")
    result_df = process_comments(df, chain)

    output_file = 'sentiment_analysis_results.xlsx'
    result_df.to_excel(output_file, index=False)
    print(f"Processing complete. Downloading {output_file}...")
    files.download(output_file)

if __name__ == "__main__":
    main()