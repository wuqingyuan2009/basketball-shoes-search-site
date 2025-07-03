import sqlite3

conn = sqlite3.connect('sneakers.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS sneakers (
    id TEXT PRIMARY KEY,
    name TEXT,
    pid TEXT,
    image TEXT,
    searchKey TEXT,
    retail INTEGER,
    releaseDate TEXT,
    colorway TEXT,
    brand TEXT,
    type TEXT,
    gender TEXT,
    description TEXT
)
""")

# 可选索引优化查询速度
c.execute("CREATE INDEX IF NOT EXISTS idx_brand ON sneakers(brand)")
c.execute("CREATE INDEX IF NOT EXISTS idx_type ON sneakers(type)")
c.execute("CREATE INDEX IF NOT EXISTS idx_name ON sneakers(name)")
c.execute("CREATE INDEX IF NOT EXISTS idx_colorway ON sneakers(colorway)")
c.execute("CREATE INDEX IF NOT EXISTS idx_gender ON sneakers(gender)")
c.execute("CREATE INDEX IF NOT EXISTS idx_releaseDate ON sneakers(releaseDate)")
c.execute("CREATE INDEX IF NOT EXISTS idx_retail ON sneakers(retail)")

conn.commit()
conn.close()

print("Database and table created with indexes.")
