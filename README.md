# SEC 10-K Filings Analyzer

Overview

This project aims to automate the downloading and analysis of SEC 10-K filings for publicly traded companies from 1995 to 2023. The application enables users to enter a company ticker, downloads the relevant 10-K filings, and performs text analysis to extract key financial insights. A simple Flask web application is used to interact with the user, providing a convenient interface for data visualization based on the analyzed results.
Features

    Automated Downloading: Automatically download 10-K filings from the SEC EDGAR database for any user-specified ticker from 1995 to 2023.
    Text Analysis: Leverage OpenAI's powerful language models to analyze and extract insights from the filings.
    Data Visualization: Generate and display visualizations of the analyzed data directly in the web application.
    User Interface: Simple and intuitive web interface for users to input company tickers and view results.

Technologies Used

    Python: Primary programming language for backend development.
    Flask: Web framework used to create the user interface.
    OpenAI API: For performing advanced text analysis using machine learning models.
    Matplotlib: For generating visualizations of the financial data.
    sec-edgar-downloader: Python library used for downloading filings from the SEC website.

Installation

To get this project up and running on your local machine, follow these steps:

Clone this repository: git clone https://github.com/yourusername/SEC-Filings-Analyzer.git
Navigate to the project directory: cd SEC-Filings-Analyzer
Install required Python packages: pip install -r requirements.txt
Start the Flask application: python app.py

Usage

Enter a company ticker into the input field and submit the form. The application will process the latest 29 years of 10-K filings, analyze them, and present a plot summarizing the key financial trends.
