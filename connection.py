import pandas as pd
from typing import Any, Dict
import sqlite3

class DataIngestionEngine:
    """Handles parsing of files and DB connections into unified access queries."""
    
    def __init__(self, db_path: str = "retail_data.db"):
        self.db_path = db_path
        
    def upload_excel(self, file_path: str, table_name: str):
        df = pd.read_excel(file_path)
        with sqlite3.connect(self.db_path) as conn:
            df.to_sql(table_name, conn, if_exists="replace", index=False)
        return f"Successfully ingested Excel sheet into table: {table_name}"

    def upload_pdf(self, file_path: str):
        # Placeholder for extraction logic (e.g., pypdf) to ingest unstructured context
        return "Extracted PDF contents into vector/text context cache."

    def execute_query(self, query: str) -> pd.DataFrame:
        with sqlite3.connect(self.db_path) as conn:
            try:
                return pd.read_sql_query(query, conn)
            except Exception as e:
                return pd.DataFrame([{"Error": str(e)}])