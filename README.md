# 🍽️ AI-Agent: Recipe Generator 🤖✨

## **Architecture Diagram** 📊

![Architecture Diagram](https://raw.githubusercontent.com/Denos-PB/AI-agent/main/diagram-export-03.04.2025-12_43_19.png)

## **Description** 📜

This project demonstrates an **AI-powered recipe agent** that utilizes **Gemini** (a Large Language Model) to generate dish recipes based on user input. Additionally, it integrates an **SQLite database** to store and retrieve recipe-related data for future improvements and personalization. 

---

## **Key Features** ⭐

1. **User Input Handling**:
   - Accepts user queries (e.g., "Give me a pasta recipe" or "Suggest a dessert with chocolate").
   - Preprocesses input to clean and structure it for better understanding.

2. **Recipe Generation with Gemini**:
   - The AI agent uses **Gemini** to generate recipes based on the user’s request.
   - The model considers ingredients, cuisine type, and dietary restrictions if provided.

3. **Database Integration (SQLite)**:
   - Stores user queries and generated recipes for analysis and improvements.
   - Retrieves past recommendations to enhance user experience.

4. **Future Enhancements**:
   - Machine learning-based recommendations based on user preferences.
   - Integration with external recipe APIs for broader recipe diversity.
   - User profile management for personalized recipe suggestions. 

---

## **How It Works** 🔍

1. **User Query**:
   - The user requests a recipe (e.g., "How do I make lasagna?").

2. **Preprocessing**:
   - The input is cleaned and structured for better understanding.

3. **Recipe Generation**:
   - The **Gemini LLM** generates a relevant recipe based on the request.

4. **Database Interaction (SQLite)**:
   - The generated recipe is stored for future reference.
   - If a similar query exists, the agent retrieves and refines past recipes.

5. **Response Output**:
   - The agent returns the recipe to the user in a structured format. 

---

## **Technologies Used** 🛠️

- **Gemini (LLM)**: AI model for recipe generation.
- **SQLite**: Database for storing user queries and recipes.
- **Python**: Core programming language for implementation.
- **Preprocessing Techniques**: Tokenization, text cleaning, and data structuring. 

---

## **Installation** 📦

1. Clone the repository:
   ```bash
   git clone https://github.com/Denos-PB/AI-agent.git
   cd AI-agent
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the agent:
   ```bash
   python main.py
