from agents.base_agent import BaseAgent
from agents.sql_agent import SQLAgent
from typing import Dict, Any

class PricingPromoAgent(BaseAgent):
    def __init__(self, sql_agent: SQLAgent):
        super().__init__("Pricing & Promo Agent", "Evaluates markdown depth, promo elasticity, and margins.")
        self.sql_agent = sql_agent

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        # Leverage the SQL Agent tool
        sql_response = self.sql_agent.analyze({"prompt": "Fetch historical discount depths & sales correlations", "domain": "Pricing"})
        # Evaluate data (Simulated LLM call)
        analysis = "Analysis: Competitor matching cut margins by 12%; internal promotions failed to drive structural velocity."
        return {"agent": self.name, "insights": analysis, "data_used": sql_response["data"]}

class InventoryManagementAgent(BaseAgent):
    def __init__(self, sql_agent: SQLAgent):
        super().__init__("Inventory Agent", "Tracks stock levels, out-of-stock events, and shrinkage.")
        self.sql_agent = sql_agent

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        sql_response = self.sql_agent.analyze({"prompt": "Get stock-out rates for top-tier SKUs", "domain": "Inventory"})
        analysis = "Analysis: Critical stock-outs in top 10 core SKUs led to a direct 8% drop in top-line transaction counts."
        return {"agent": self.name, "insights": analysis, "data_used": sql_response["data"]}

class SupplyChainAgent(BaseAgent):
    def __init__(self, sql_agent: SQLAgent):
        super().__init__("Supply Chain Agent", "Measures lead times, freight anomalies, and fulfillment rates.")
        self.sql_agent = sql_agent

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        sql_response = self.sql_agent.analyze({"prompt": "Fetch port delay tracking and inbound freight exceptions", "domain": "Logistics"})
        analysis = "Analysis: Lead times extended by 14 days due to overseas shipping bottlenecks, choking regional DC replenishment."
        return {"agent": self.name, "insights": analysis, "data_used": sql_response["data"]}

class PlanningAgent(BaseAgent):
    def __init__(self, sql_agent: SQLAgent):
        super().__init__("Planning Agent", "Assesses demand forecasting accuracy, open-to-buy budgets, and macro trends.")
        self.sql_agent = sql_agent

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        sql_response = self.sql_agent.analyze({"prompt": "Fetch forecasted demand vs actual performance", "domain": "Planning"})
        analysis = "Analysis: Demand forecasts overestimated seasonal ramp-up by 18%, forcing inefficient dynamic pricing corrections."
        return {"agent": self.name, "insights": analysis, "data_used": sql_response["data"]}

class SourcingAgent(BaseAgent):
    def __init__(self, sql_agent: SQLAgent):
        super().__init__("Sourcing Agent", "Evaluates Vendor performance, COGS deviations, and raw material liabilities.")
        self.sql_agent = sql_agent

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        sql_response = self.sql_agent.analyze({"prompt": "Analyze component/factory wholesale cost variance trends", "domain": "Sourcing"})
        analysis = "Analysis: Raw factory COGS scaled up 4.5% due to supplier index increases, directly depressing product gross profit."
        return {"agent": self.name, "insights": analysis, "data_used": sql_response["data"]}