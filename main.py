from database.connection import DataIngestionEngine
from agents.sql_agent import SQLAgent
from agents.orchestrator import RootOrchestrator
from agents.domain_agents import (
    PricingPromoAgent, 
    InventoryManagementAgent, 
    SupplyChainAgent, 
    PlanningAgent, 
    SourcingAgent
)
import json

def main():
    # 1. Initialize DB Infrastructure Engine
    db_engine = DataIngestionEngine()
    
    # Mock data injection setup 
    # db_engine.upload_excel("q3_sales.xlsx", "pricing")
    
    # 2. Instantiate Shared SQL Agent
    shared_sql_agent = SQLAgent(db_engine=db_engine)
    
    # 3. Instantiate Domain Experts and pass the SQL engine instance to them
    domain_nodes = [
        PricingPromoAgent(sql_agent=shared_sql_agent),
        InventoryManagementAgent(sql_agent=shared_sql_agent),
        SupplyChainAgent(sql_agent=shared_sql_agent),
        PlanningAgent(sql_agent=shared_sql_agent),
        SourcingAgent(sql_agent=shared_sql_agent)
    ]
    
    # 4. Spin up the Root Orchestrator
    orchestrator = RootOrchestrator(domain_agents=domain_nodes)
    
    # 5. Execute core diagnostic request
    results = orchestrator.resolve_root_cause(core_problem="Why are sales dropping in Q3?")
    
    # Output final results
    print("\n" + "="*60)
    print("🎯 FINAL SYNTHESIZED REPORT")
    print("="*60)
    print(results["root_cause_synthesis"])
    
if __name__ == "__main__":
    main()