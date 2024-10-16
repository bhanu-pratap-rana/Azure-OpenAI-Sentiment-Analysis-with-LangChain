# Azure-OpenAI-Sentiment-Analysis-with-LangChain
Azure OpenAI Sentiment Analysis with LangChain
A Python-based sentiment analysis tool that processes comments from Excel/CSV files using Azure OpenAI and LangChain. The tool analyzes the sentiment and emotion of comments and provides human-like responses based on the analysis.
Features

Upload Excel (.xlsx) or CSV files containing comments
Process comments using Azure OpenAI's GPT model
Sentiment and emotion analysis with human-like responses
Error handling for content filtering
Progress tracking during processing
Export results back to Excel format
Built for Google Colab environment

Prerequisites

Google Colab account
Azure OpenAI API access
Python 3.x
Required Python packages:

langchain
openai
pandas
openpyxl



Setup

Clone this repository:

bashCopygit clone https://github.com/bhanu-pratap-rana/azure-openai-sentiment-analysis.git

Open the notebook in Google Colab.
Set up your Azure OpenAI credentials in the code:

pythonCopyos.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2024-08-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = "your-endpoint"
os.environ['AZURE_OPENAI_API_KEY'] = "your-api-key"
Usage

Prepare your input file:

Create an Excel (.xlsx) or CSV file
Include a column named 'comment' containing the text to analyze


Run the script in Google Colab:

Upload the notebook to Google Colab
Run all cells
Upload your input file when prompted
Wait for processing to complete
Download the results file



Code Structure
pythonCopy# Main components:
- upload_file(): Handles file upload in Colab
- read_file(): Reads Excel/CSV files
- setup_llm_chain(): Configures Azure OpenAI and LangChain
- process_comments(): Processes comments and generates responses
- main(): Orchestrates the entire process
Output
The script generates an Excel file containing:

Original comments
Sentiment analysis responses
Processing status for each comment

Error Handling
The script includes robust error handling for:

Content filtering (Azure OpenAI policy)
Rate limiting
File processing errors
Invalid input formats

Limitations

Requires Azure OpenAI API access
Designed for Google Colab environment
Processes comments sequentially (may be slow for large datasets)
Subject to Azure OpenAI's content filtering policies

Contributing

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
Acknowledgments

Built with LangChain
Powered by Azure OpenAI
Inspired by the need for efficient sentiment analysis of user comments

Author
Bhanu Pratap Rana - GitHub Profile
Project Link: https://github.com/bhanu-pratap-rana/azure-openai-sentiment-analysis
Connect
Feel free to connect or reach out for any questions or suggestions about the project.
GitHub
