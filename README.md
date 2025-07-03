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
```
.
├── main.py # FastAPI backend
├── sneakers.db # Your SQLite sneaker database
└── index.html # Frontend
```
---

## ⚡ Usage

### 1️⃣ Start the FastAPI server:
```bash
uvicorn main:app --reload
The API will be accessible at:

http://127.0.0.1:8000/query
```
### 2️⃣ Serve the frontend:

```
python -m http.server 8000
Visit:

http://127.0.0.1:8000/index.html
```
🧩 Example Queries
"Show all Nike sneakers released in 2023"

"Display all sneakers under $200"

"List Adidas basketball sneakers"

The website will:
✅ Display generated SQL
✅ Show matching sneaker results with images

![screenshot](/images/Screenshot.png)
