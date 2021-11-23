# %%
# !pip install psycopg2
# %%
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="password",
    port=5444
    )

# %%
cur = conn.cursor()
cur.execute('SELECT version()')
cur.fetchone()
# %%
cur.execute('SELECT 1')
cur.fetchone()
# %%
