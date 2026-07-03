from typing import List, Dict, Any
from agents.base_agent import BaseAgent

class RootOrchestrator:
    """Collates domain-specific findings to build a deep structural 'Why' behind macro events."""
    
    def __init__(self, domain_agents: List[BaseAgent]):
        self.domain_agents = domain_agents

    def resolve_root_cause(self, core_problem: str) -> Dict[str, Any]:
        print(f"🕵️‍♂️ Root Orchestrator: Diagnosing macro issue -> '{core_problem}'\n")
        
        aggregated_insights = []
        
        # Gather information from all 5 specialized nodes
        for agent in self.domain_agents:
            print(f"🔄 Polling sub-system: {agent.name}...")
            report = agent.analyze({"problem_statement": core_problem})
            aggregated_insights.append(report)
            
        # Correlate inputs (Simulated LLM aggregation process)
        synthesis = (
            f"--- Root Cause Analysis Matrix for: '{core_problem}' ---\n"
            "The sales dip is structurally cross-functional. Sourcing & Logistics delays (Supply Chain/Sourcing) "
            "led to stockouts in top revenue-generating SKUs (Inventory). Planning over-forecasted seasonal capacity, "
            "triggering reactive discount depths (Pricing) that destroyed gross margin margins despite lower product volumes."
        )
        
        return {
            "macro_problem": core_problem,
            "root_cause_synthesis": synthesis,
            "raw_agent_reports": aggregated_insights
        }