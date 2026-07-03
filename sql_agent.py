from agents.base_agent import BaseAgent
from database.connection import DataIngestionEngine
from config import config
from typing import Dict, Any

class SQLAgent(BaseAgent):
    """Generates precise SQL queries based on natural language prompts using chain-of-thought reasoning."""
    
    def __init__(self, db_engine: DataIngestionEngine):
        super().__init__(name="SQL Agent", role="Text-to-SQL Engineer")
        self.db_engine = db_engine

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        nl_prompt = context.get("prompt", "")
        domain = context.get("domain", "General")
        
        # 1. Chain-of-thought Reasoning step (Simulated LLM Generation)
        reasoning = f"Reasoning [{domain}]: Need to fetch metric matching '{nl_prompt}'. Mapping to active schema."
        
        # 2. SQL Generation
        # Production build requires feeding schema metadata to the LLM context wrapper
        generated_sql = f"SELECT * FROM {domain.lower()}_table WHERE date >= date('now', '-30 days');"
        
        if "sales" in nl_prompt.lower():
            generated_sql = "SELECT revenue, margin FROM transactions WHERE date >= date('now', '-90 days');"
            
        # 3. Data Retrieval
        data_df = self.db_engine.execute_query(generated_sql)
        
        return {
            "reasoning": reasoning,
            "generated_sql": generated_sql,
            "data": data_df.to_dict(orient="records")
        }