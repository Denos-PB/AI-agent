# AI-agent

## Architecture Diagram

![Architecture Diagram](https://raw.githubusercontent.com/Denos-PB/AI-agent/main/diagram-export-20.03.2025-23_31_14.png)

## Description
# AI Agent with LLM and Weather API Integration

This project demonstrates the architecture and functionality of an **AI agent** that leverages a **Large Language Model (LLM)** to interact with users and fetch weather data using an external **Weather API**. The agent processes user input, detects intent, and provides relevant responses, either by generating a general response using the LLM or by fetching weather data from the API.

---

## **Key Features**

1. **User Input Handling**:
   - The AI agent accepts user input (e.g., "What's the weather in New York?").
   - The input is preprocessed to clean and tokenize the text for further processing.

2. **Intent Detection**:
   - The LLM is used to detect the user's intent (e.g., weather query or general query).
   - If the intent is a **weather query**, the agent proceeds to fetch weather data.
   - If the intent is a **general query**, the agent generates a response using the LLM.

3. **Weather API Integration**:
   - For weather queries, the agent calls an external **Weather API** to fetch real-time weather data.
   - The weather data is formatted and sent back to the user.

4. **Response Generation**:
   - For general queries, the LLM generates a response based on the user's input.
   - The response is postprocessed and sent back to the user.

---

## **How It Works**

1. **User Input**:
   - The user asks a question or provides input (e.g., "What's the weather in Paris?").

2. **Preprocessing**:
   - The input is cleaned and tokenized.

3. **Intent Detection**:
   - The LLM detects whether the input is a weather query or a general query.

4. **Weather Query**:
   - If the input is a weather query, the agent extracts the city name and calls the Weather API.
   - The weather data is fetched and formatted.

5. **General Query**:
   - If the input is a general query, the LLM generates a response.

6. **Output**:
   - The agent sends the weather data or general response back to the user.

---

## **Technologies Used**

- **Large Language Model (LLM)**: For intent detection and response generation.
- **Weather API**: For fetching real-time weather data.
- **Python**: For implementing the AI agent and integrating the LLM and API.
- **Tokenization and Cleaning**: For preprocessing user input.

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/Denos-PB/AI-agent.git
   cd AI-agent
