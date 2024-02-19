# Project Setup Guide

## Step 1: Clone Repository and Set Up Pinecone Vector Database

- Clone the repository:

- Create an account and index on the Pinecone vector database.

## Step 2: Create .env File

- Create a `.env` file in the root directory of the project.

## Step 3: Configure Environment Variables

- Inside the `.env` file, add the following variables:

```dotenv
PINECONE_API_KEY = <your_pinecone_api_key>
PINECONE_ENV_NAME = <your_pinecone_environment_name>
OPENAI_API_KEY = <your_openai_api_key>
```

## Step 4: Set Up Virtual Environment

pip install pipenv
Or, if you're using Python 3:
pip3 install pipenv
Activate the virtual environment using the following command:
pipenv shell

## Step 5: Run Embedding and Retrieval Scripts

- Execute the following command to store embeddings in the vector database:
  `python embedding.py`
- Run the retrieval script to check if documents can be generated from the vector database:
  `python retrieve.py`

## Step 6: Customize Streamlit Frontend

- Customize the Streamlit frontend according to your preferences.

- If you want to clear the previous chat history, use 1.py as main.py

## Step 7: Deployment

- Deploy the application on Streamlit.
