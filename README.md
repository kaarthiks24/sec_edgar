# sec_edgar

This repository uses OpenAI embeddings and llm models hence add your openapi key 
If using Mac/Linux use this command:


```echo "export OPENAI_API_KEY='your api key here'" >> ~/.zshrc```


TO GET NECESSARY FILINGS FROM THE SEC EDGAR:

```python xbrl_download.py```

TO INGEST INTO THE DATABASE:
```python ingest.py```

TO ASK QUERIES ON THE DOCUMENTS:
```python run_query.py```
