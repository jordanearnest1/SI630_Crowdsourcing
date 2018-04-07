import sqlite3 as sqlite


worker_id_list = []
def pull_worker_ids():
    # Your code goes here
    conn = sqlite.connect('crowd.db')
    cur = conn.cursor()
    statement = '''
    SELECT DISTINCT _worker_id FROM full_report 
    '''
    cur.execute(statement)
    for row in cur:
        worker_id_list.append(row[0])
    print(worker_id_list)

pull_worker_ids()

conn = sqlite.connect('crowd.db')
cur = conn.cursor()

# for worker_id_1 in worker_id_list:
# 	for worker_id_2 in worker_id_list:
# 		if worker_id_1 != worker_id_2: 
# 			statement = '''
# 			FROM full_report AS full_report_1
# 			JOIN full_report AS full_report_2
# 			WHERE full_report_1.post_id = full_report_2_post.id			
# 			SELECT full_report_1.rating, full_report_2.rating, full_report_1.post_id, full_report_2.post_id
# 			WHERE full_report_1._worker_id = worker_id_1 AND full_report_2._worker_id = worker_id_2
# 			'''
# 			cur.execute(statement)
# 			for row in cur: 
# 				print(row)


for worker_id_1 in worker_id_list:
	for worker_id_2 in worker_id_list:
		if worker_id_1 != worker_id_2: 
			params = worker_id_1, worker_id_2
			statement = '''
			SELECT full_report_1.civility, full_report_2.civility, full_report_1.post_id, full_report_2.post_id, full_report_1._worker_id, full_report_2._worker_id
			FROM full_report AS full_report_1
			JOIN full_report AS full_report_2
			WHERE full_report_1.post_id = full_report_2.post_id	AND full_report_1._worker_id = ? AND full_report_2._worker_id = ?
			'''
			cur.execute(statement, params)
			for row in cur: 
				print(row)


