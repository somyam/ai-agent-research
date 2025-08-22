⏺ This is an AI-powered research assistant application that helps users conduct research on various topics. Here's what it does:
  LLM Pipeline Components:
  - Input Processing: Structured prompt templates with placeholders for chat history, user query, and agent scratchpad
  - Model Integration: OpenAI GPT-4o-mini integration with temperature controls
  - Output Parsing: Pydantic-based structured output parsing to ensure consistent response format
  - Error Handling: Try-catch blocks for parsing failures with fallback to raw output

  Model Orchestration:
  - Agent Framework: Uses LangChain's create_tool_calling_agent for orchestrating model decisions
  - Tool Coordination: Automatic tool selection and execution based on model reasoning
  - Execution Flow: AgentExecutor manages the complete pipeline from input to structured output
  - Multi-step Reasoning: Agent can chain tool calls and use previous outputs to inform next steps

  Production-Ready Patterns:
  - Environment Management: Uses .env files for API key management
  - Structured Data Models: Pydantic schemas for consistent API responses
  - Logging/Persistence: File saving with timestamps for audit trails
  - Modular Design: Separated tools (tools.py) from main orchestration logic

