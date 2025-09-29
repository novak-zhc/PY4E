import sqlite3
import csv
import os

# --- 1. 数据库连接 ---
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# --- 2. 数据库结构初始化（确保清空旧数据并重建表） ---

print("清空旧表并重建结构...")

cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')

# 创建 Artist 表
cur.execute('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)''')

# 创建 Genre 表
cur.execute('''
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)''')

# 创建 Album 表
cur.execute('''
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
)''')

# 创建 Track 表
cur.execute('''
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
)''')

# --- 3. 文件处理与数据导入 ---

fname = input('输入文件名 (默认为 tracks.csv): ')
if len(fname) < 1 : fname = 'tracks.csv'

if not os.path.exists(fname):
    print(f"错误：文件 '{fname}' 未找到。请确保文件在同一目录下。")
    conn.close()
    exit()

print(f"正在导入数据文件: {fname}")

# 使用 csv 模块来正确读取逗号分隔的文件
with open(fname, encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    # 跳过 CSV 文件的表头行（如果存在的话）
    # next(reader, None)

    for row in reader:
        # 检查数据完整性：一行应该有 7 个字段
        if len(row) != 7:
            # print(f"警告：跳过不完整行: {row}")
            continue

        # 按顺序提取字段：Title, Artist, Album, Count, Rating, Length, Genre
        name, artist, album, count, rating, length, genre = row
        
        # 打印当前处理的记录，方便调试
        # print(f"{name}, {artist}, {album}, {genre}")

        # --- A. 导入 Artist（艺术家） ---
        # 插入或忽略 Artist，并获取其 ID
        cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES (?)''', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        # --- B. 导入 Genre（流派） ---
        # 插入或忽略 Genre，并获取其 ID
        cur.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES (?)''', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]
        
        # --- C. 导入 Album（专辑，依赖于 Artist_ID） ---
        # 插入或忽略 Album，并获取其 ID
        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES (?, ?)''', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]
        
        # --- D. 导入 Track（音轨，依赖于 Album_ID 和 Genre_ID） ---
        # INSERT OR REPLACE: 如果音轨标题已存在，则用新数据替换旧数据
        cur.execute('''INSERT OR REPLACE INTO Track 
            (title, album_id, genre_id, len, rating, count) 
            VALUES (?, ?, ?, ?, ?, ?)''', 
            (name, album_id, genre_id, length, rating, count))
    
    # --- 4. 最终提交（性能优化：一次性写入所有更改） ---
    conn.commit()

# --- 5. 运行验证查询（评分查询） ---

print("\n--- 验证查询结果（应与题目要求一致）---")
sqlstr = '''
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track 
    JOIN Album ON Track.album_id = Album.id 
    JOIN Artist ON Album.artist_id = Artist.id
    JOIN Genre ON Track.genre_id = Genre.id
    ORDER BY Artist.name LIMIT 3
'''

for row in cur.execute(sqlstr):
    print(f"音轨: {row[0]}, 艺术家: {row[1]}, 专辑: {row[2]}, 流派: {row[3]}")


# --- 6. 清理 ---
cur.close()
print("\n导入完成，数据库文件 'trackdb.sqlite' 已生成。请上传此文件。")