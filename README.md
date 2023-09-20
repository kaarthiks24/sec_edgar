# sec_edgar

This repository uses OpenAI embeddings and llm models hence add your openapi key 
If using Mac/Linux use this command:


```echo "export OPENAI_API_KEY='your api key here'" >> ~/.zshrc```


TO INSTALL ALL THE NECESSARY DEPENDENCIES
```pip install -r requirements.txt```

TO GET NECESSARY FILINGS FROM THE SEC EDGAR:
```python xbrl_download.py```

TO INGEST INTO THE DATABASE:
```python ingest.py```

TO ASK QUERIES ON THE DOCUMENTS(experimental purpose please use the streamlit frontend for the chatbot):
```python run_query.py```

TO ASK QUERIES WITH A STREAMLIT FRONTEND:
```streamlit run frontend.py```
