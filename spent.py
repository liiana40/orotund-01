import sqlite3 as db

def init():
	'''
	Initialize a new database to store spendings
	'''
	conn = db.connect("spent.db")
	cur = conn.cursor()
	sql = '''
	create table if not exists expenses (
		amount number,
		category string,
		message string,
		date string
		)
	'''
	cur.execute(sql)
	conn.commit()

def log(amount, category, message=""):
	'''
	logs the spendings in the database
	amount: numbar
	category: string
	message: (optional) string
	'''
	from datetime import datetime
	date = str(datetime.now())
	conn = db.connect("spent.db")
	cur = conn.cursor()
	sql = '''
	insert into expenses values (
		{},
		'{}',
		'{}',
		'{}'
		)
	'''.format(amount,category, message, date)
	cur.execute(sql)
	conn.commit()

#log(120, "transport", "uber service")

def view(category=None):
	'''
	Returns a list of all expenditures incuired, and the total expenses. 
	If a category is specified, it only returns info from that
	category
	'''
	conn = db.connect("spent.db")
	cur = conn.cursor()
	if category:
		sql = '''
		select * from expenses where category= '{}'
		'''.format(category)
		sql2 = '''

		'''
		select sum(amount)from expenses where category = '{}'
	else:
		sql='''
		select * from expenses 
		'''.format(category)
		sql2 = '''
		select sum(amount) from expenses
	cur.execute(sql)
	results = cur.fetchall()
	cur.execute(sql2)
	total_amount = cur.fetchone()[0]

	return total_amount, results


