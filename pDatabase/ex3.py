import json
import sqlite3
import os

# --- 1. 数据库连接 ---
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# --- 2. 数据库结构初始化（修正 Member 表以存储 role） ---

# 注意：Member 表的 PRIMARY KEY 应该只包含 user_id 和 course_id，
# 确保一个用户在同一课程中只有一条记录，role 是该记录的一个属性。
# 如果将 role 包含在 PRIMARY KEY 中，则一个用户可以在一门课中拥有多个角色记录，
# 这与一般花名册系统的设计意图不符（通常一个用户/课程组合只有一条记录，角色可更新）。
# 因此，我们使用标准的复合主键 (user_id, course_id)。

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,  -- 新增 role 字段
    PRIMARY KEY (user_id, course_id)
)
''')

# --- 3. 文件处理 ---
fname = input('Enter file name (roster_data.json): ')
if len(fname) < 1:
    fname = 'roster_data.json'

if not os.path.exists(fname):
    print(f"Error: File '{fname}' not found. Please download your specific roster data file.")
    cur.close()
    conn.close()
    exit()

try:
    str_data = open(fname).read()
    json_data = json.loads(str_data)
except Exception as e:
    print(f"Error reading or parsing JSON file: {e}")
    cur.close()
    conn.close()
    exit()


# --- 4. 核心数据导入循环 ---

# 数据格式: [ "Name", "Course_Title", Role_Integer ]
for entry in json_data:

    if len(entry) < 3:
        print(f"Skipping incomplete entry: {entry}")
        continue
        
    name = entry[0]
    title = entry[1]
    role = entry[2] # *** 关键修正点 1: 提取 role 字段 ***

    print((name, title, role))

    # A. 处理 User 表
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    # B. 处理 Course 表
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    # C. 处理 Member 表
    # *** 关键修正点 2: 使用 INSERT OR REPLACE 并包含 role 字段 ***
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

# --- 5. 提交所有更改 ---
# 仅提交一次，提高效率
conn.commit()

cur.close()
print("数据导入完成，rosterdb.sqlite 文件已生成。")