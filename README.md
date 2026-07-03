# multi-agent-framework

An asynchronous, tool-enabled multi-agent architecture designed to diagnose complex cross-functional business problems in retail ecosystems ("Why are gross margins dropping despite volume growth?").

This framework implements a Hub-and-Spoke dependency model, allowing five domain-specific agents to collaboratively query real-time data sources by accessing a specialized Text-to-SQL Agent as a shared diagnostic utility tool. A Root Orchestrator finally synthesizes the inputs into a cohesive root-cause analysis. 

# Core Architecture Components
1. Data Ingestion Engine: Acts as an abstraction layer across physical databases, Excel workbooks, and raw text extraction pipelines.

2. The SQL Agent (The Utility Hub): Accepts plain-text instructions from any sibling agent, handles Chain-of-Thought reasoning to maps the prompt against schema context, constructs structured SQL, and retrieves raw tabular data arrays.

3. Domain Agents (The Spokes): Five functional retail domain brains focusing on independent operational streams:

4. Pricing & Promotion: Analyzes markdown elasticities and margin erosion.

5. Inventory Management: Identifies systemic stock-out events and shrinkage issues.

6. Supply Chain & Logistics: Surfaces freight bottlenecks, lead times, and port delays.

5. Planning: Evaluates forward-looking demand forecasting variance.

6. Sourcing: Validates raw material index trends and COGS discrepancies.

7. Root Orchestrator: The structural convergence node that synthesizes downstream agent readouts to find the definitive cross-functional "Why" behind performance shifts.

retail_analytics_framework/
│
├── config.py                # System parameters & environment configuration
├── main.py                  # Operational pipeline entrypoint 
│
├── database/
│   ├── __init__.py
│   └── connection.py        # Connectors for Excel parsing & raw SQL execution
│
└── agents/
    ├── __init__.py
    ├── base_agent.py        # Abstract class layout enforcing execution patterns
    ├── sql_agent.py         # The centralized Text-to-SQL reasoning agent
    ├── domain_agents.py     # Functional domain expert nodes (Pricing, Inventory, etc.)
    └── orchestrator.py      # Master Root Orchestrator for macro diagnosis
