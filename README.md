# DIY Sneaker Query Website

This project is a **DIY sneaker information website** that:

✅ Lets users **input natural language queries** (e.g., "Show Nike sneakers from 2023")  
✅ Uses **OpenAI ChatGPT API** to **translate queries into SQL**  
✅ Executes SQL on your **local `sneakers.db` SQLite database**  
✅ Displays sneaker results with **images, names, prices, and release dates** on a user-friendly website  
✅ Shows the **generated SQL** with a **copy button** for transparency and debugging

---

## 🚀 Features

- **FastAPI backend** serving:
  - `/sneakers` for raw JSON of all sneakers
  - `/query` to process user queries and return generated SQL + results
- **Frontend (index.html)** with:
  - Natural language query input
  - Displays generated SQL + copy button
  - Grid view of sneaker results with images
- **SQLite (`sneakers.db`)** for your sneaker data
- Uses **ChatGPT API** for generating SQL dynamically

---

## 🛠️ Requirements

- Python 3.8+
- `pip install fastapi uvicorn openai`
- A valid **OpenAI API key** (`export OPENAI_API_KEY="your_key_here"`)

---

## 📂 Project Structure


![screenshot](/images/Screenshot.png)
