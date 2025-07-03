import sqlite3
import json
from pathlib import Path

# 连接数据库
conn = sqlite3.connect('sneakers.db')
c = conn.cursor()

# 扫描目录
json_dir = Path('query_results')
json_files = list(json_dir.glob('*.json'))

count = 0

for json_file in json_files:
    with open(json_file, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ Skipping {json_file} due to JSON decode error.")
            continue

        for item in data:
            sneaker_id = item.get("uuid")
            if not sneaker_id:
                continue
            name = item.get("name")
            pid = item.get("pid")
            image = item.get("image")
            searchKey = item.get("searchKey")
            details = item.get("details", {})
            retail = details.get("retail")
            releaseDate = details.get("releaseDate")
            colorway = details.get("colorway")
            brand = details.get("brand")
            type_ = details.get("type")
            gender = details.get("gender")
            description = details.get("description")

            try:
                c.execute("""
                INSERT OR REPLACE INTO sneakers
                (id, name, pid, image, searchKey, retail, releaseDate, colorway, brand, type, gender, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    sneaker_id, name, pid, image, searchKey,
                    retail, releaseDate, colorway, brand, type_, gender, description
                ))
                count += 1
            except Exception as e:
                print(f"⚠️ Error inserting {sneaker_id}: {e}")

conn.commit()
conn.close()
print(f"✅ Successfully imported {count} sneaker records into sneakers.db")
