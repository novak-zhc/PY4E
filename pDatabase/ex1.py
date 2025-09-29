import sqlite3
import re # 导入 re 模块，虽然 split('@') 更简洁，但为了示范健壮性，这里保留

# 1. 初始化数据库连接和游标
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# 确保表是干净的，符合题目要求
cur.execute('DROP TABLE IF EXISTS Counts')

# 按照题目要求创建表，注意列名是 org
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# 2. 文件处理
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'

# 使用 with 语句确保文件被安全关闭
try:
    fh = open(fname)
except FileNotFoundError:
    print(f"Error: File '{fname}' not found.")
    cur.close()
    conn.close()
    exit()

# 3. 核心数据处理循环
for line in fh:
    if not line.startswith('From: '): continue
    
    pieces = line.split()
    if len(pieces) < 2: continue # 避免空行或格式不正确的行
    
    email = pieces[1]
    
    # *** 修正点 1: 提取组织名 (Org) ***
    try:
        # 找到 '@' 符号后面的部分，即域名/组织名
        org = email.split('@')[1] 
    except IndexError:
        # 如果邮件格式不正确（没有 '@' 符号），则跳过
        continue

    # 4. SQL 插入或更新逻辑
    
    # 查询当前组织名是否已存在
    # 注意：使用 org 作为占位符的值
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    
    if row is None:
        # 组织名是新的，插入新行，count=1
        cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
    else:
        # 组织名已存在，更新 count + 1
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    
    # *** 修正点 2: 移除 conn.commit() (保持高效) ***

# 5. 提交所有更改 (仅一次)
# 将所有事务一次性写入磁盘，提高效率
conn.commit()

# 6. 查询并打印结果
print("Counts:")
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# 7. 清理
cur.close()
conn.close()