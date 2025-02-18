# MULTIAGENT- AI Chatbot with LangGraph & LangChain

Welcome to the AI Chatbot project! This chatbot leverages **LangGraph** and **LangChain** to provide AI-driven conversational capabilities. It includes features like resume analysis, job matching, AI-powered tools integration, and more.

## 📌 Features
- **Conversational AI** powered by **LangGraph** and **LangChain**.
- **Tool Integration** with **Wikipedia** and **Arxiv API** for enhanced responses.
- **Graph-based Conversation Flow** using LangGraph.
- **Real-time AI Interaction** with models like **Gemma-2-9B-IT** and **LLaMA 3.3-70B-Versatile**.
- **Configurable Environment** using `.env` variables.

---

## 🛠 Setup & Installation

### 1️⃣ Prerequisites
Ensure you have **Python 3.8+** installed. Install dependencies using:
```bash
pip install -r requirements.txt
```

### 2️⃣ Environment Variables
Create a `.env` file in the root directory and set the following keys:
```env
langsmith_api_key=YOUR_LANGSMITH_API_KEY
groq_api_key=YOUR_GROQ_API_KEY
```

### 3️⃣ Running the Chatbot
#### **Option 1: Standalone Chatbot**
Run `Chatbot.py` for a simple chatbot experience:
```bash
python Chatbot.py
```
#### **Option 2: Chatbot with AI Tools**
For enhanced capabilities (Arxiv & Wikipedia integration), run:
```bash
python chatbot_with_tools.py
```

---

## 🏗️ Project Structure
```
├── chatbot.py                 # Standalone AI chatbot
├── chatbot_with_tools.py      # Chatbot with Wikipedia & Arxiv integration
├── .env                       # Environment variables (not included in repo)
├── requirements.txt           # Dependencies
├── .ipynb_checkpoints/        # Jupyter notebook checkpoints
└── README.md                  # This file
```

---

## 🚀 How It Works
- The chatbot processes user input using **LangGraph**.
- It utilizes **LangChain** to call AI models.
- When a query requires external knowledge, it invokes Wikipedia & Arxiv tools.
- Outputs are formatted and displayed in real time.

---

## 🔍 Example Usage
**Simple Chat:**
```shell
User: Hello, chatbot!
Assistant: Hello! How can I assist you today?
```

**With AI Tools:**
```shell
User: What is "Attention Is All You Need"?
Assistant: [Wikipedia & Arxiv results with AI response]
```

---

## 🤖 Technologies Used
- **Python 3.8+**
- **LangGraph** (State-based conversation flow)
- **LangChain** (AI integration)
- **Groq API** (LLM inference)
- **Arxiv API** (Research paper queries)
- **Wikipedia API** (Knowledge base)

---

## 📝 License
This project is open-source under the **MIT License**.

---

## 📞 Contact
For any queries, reach out to **Baljinder Singh**.

Happy coding! 🚀

