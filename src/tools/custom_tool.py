from langchain.tools import Tool
from model.ollama_model import OllamaHandler
from tools.weather_tool import get_weather
from tools.stock_tool import get_stock_price

# Initialize the Ollama model for direct conversation
ollama_handler = OllamaHandler()

def custom_response_tool(query: str) -> str:
    """
    Analyzes user queries and directs them to the appropriate tool if available.
    If no suitable tool is found, initiates a live chat session.
    """
    query_lower = query.lower()

    # Check if the query is related to weather
    if "weather" in query_lower or "temperature" in query_lower or "forecast" in query_lower:
        city = query.split()[-1]  # Extract city name
        return get_weather(city)

    # Check if the query is related to stock prices
    if "stock" in query_lower or "price" in query_lower or "share" in query_lower:
        words = query.split()
        for word in words:
            if len(word) >= 2 and word.isalpha():  # Identify potential stock symbols
                return get_stock_price(word)

    # If no suitable tool is found, start a live chat session
    print("\nAI Assistant is now in live chat mode. Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting live chat mode.")
            return "Live chat session ended."

        # Call the Ollama model to generate responses
        response = ollama_handler.explain_question_mark(user_input)
        print(f"AI: {response}")

# Register the tool within LangChain
custom_tool = Tool(
    name="GeneralResponse",
    func=custom_response_tool,
    description="Handles queries dynamically and starts a live chat session if no tool matches.",
    return_direct=True,
)
