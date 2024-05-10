import openai
from matplotlib import pyplot as plt
from sec_edgar_downloader import Downloader
import os

def download_filings(ticker):
    # Adjust the directory path according to your system
    dl = Downloader("YourCompanyName", "your.email@domain.com", "C:/sec-filings/")
    print(f"Downloading the most recent 10-K filings for {ticker}")
    dl.get("10-K", ticker, limit=29)  # This fetches only the most recent 29 10-K filings

def read_text_files(ticker):
    # Specify the path where the downloaded files are stored
    path = f"C:/sec-filings/sec-edgar-filings/{ticker}/10-K/"
    text_data = []
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
                text_data.append(file.read())
    return text_data

def analyze_text_with_openai(text_data):
    # Configure your OpenAI API key
    openai.api_key = 'your-openai-api-key'

    # Combining the text data into one large string for analysis
    combined_text = " ".join(text_data[:10])  # Limiting to 10 filings due to token limitations
    response = openai.Completion.create(
        engine="text-davinci-002",  # or choose the latest available model
        prompt="Summarize the key financial metrics and trends from these 10-K filings:\n" + combined_text,
        max_tokens=1500
    )
    return response.choices[0].text

def main():
    ticker = input("Enter the ticker for the company you wish to download 10-K filings for: ")
    download_filings(ticker)
    text_data = read_text_files(ticker)
    if text_data:
        insight = analyze_text_with_openai(text_data)
        print("Generated Insight:", insight)
    else:
        print("No text data found. Please check the file paths and ticker.")

main()
