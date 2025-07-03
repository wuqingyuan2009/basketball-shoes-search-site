from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os
from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
async def query_sneakers(request: Request):
    data = await request.json()
    user_query = data.get("query", "")

    # 使用 ChatGPT 生成 SQL
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个将用户查询翻译为 SQLite SQL 的助手，只返回 SQL，不要解释。表名为 sneakers，字段包含 id, name, pid, image, searchKey, retail, releaseDate, colorway, brand, type, gender, description. 数据库里的数据都是英文，releaseDate的格式是 YYYY-MM-DD，查询的时候要用大于小于号限定范围。字段中除了retail是integer，其它都是text，所有text的匹配都要使用 LIKE 语句。"},
            {"role": "user", "content": user_query}
        ]
    )
    sql = completion.choices[0].message.content.strip().strip(';')

    # 安全校验（可选：防注入）
    if not sql.lower().startswith("select"):
        return {"error": "Only SELECT statements are allowed."}

    # 执行 SQL 查询
    conn = sqlite3.connect("sneakers.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = [dict(row) for row in rows]
    except Exception as e:
        conn.close()
        return {"error": str(e)}
    conn.close()
    return {"sql": sql, "result": result}
