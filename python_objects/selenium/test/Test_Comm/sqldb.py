# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "test")

cursor = db.cursor()


# find_sql = "SELECT * FROM info"
# insert_sql = "INSERT INTO info (name,age,sex) VALUES('KaMi', 23, '男');"
# update_sql = "UPDATE info SET name = 'Fred' WHERE name = 'Jhon' "
# del_sql = "DELETE FROM info WHERE id=3;"

# SQL 查询语句
def find(find_sql):
	try:
		cursor.execute(find_sql)
		db.commit()
		results = cursor.fetchall()
		for row in results:
			id = row[0]
			name = row[1]
			age = row[2]
			sex = row[3]
			print("id=%s,name=%s,age=%d,sex=%s" % (id, name, age, sex))
	except:
		print("Error: unable to fecth data")
		db.rollback()
	# 关闭数据库连接
	db.close()


# SQL 添加语句
def insert(insert_sql):
	try:
		cursor.execute(insert_sql)
		db.commit()
		print("Success: insert data seccess")
	except:
		print("Error: insert to fecth data")
		db.rollback()
	# 关闭数据库连接
	db.close()


# SQL 修改语句
def update(update_sql):
	try:
		cursor.execute(update_sql)
		db.commit()
		print("Success: update data seccess")
	except:
		print("Error: update to fecth data")
		db.rollback()
	# 关闭数据库连接
	db.close()


# SQL 删除语句
def delete(del_sql):
	try:
		cursor.execute(del_sql)
		db.commit()
		print("Success: delete data seccess")
	except:
		print("Error: update to fecth data")
		db.rollback()
	# 关闭数据库连接
	db.close()
