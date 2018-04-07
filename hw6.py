import sqlite3 as sqlite


worker_id_list = []
def pull_worker_ids():
    # Your code goes here
    conn = sqlite.connect('civility.db')
    cur = conn.cursor()
    statement = '''
    SELECT DISTINCT _worker_id FROM full_report 
    '''
    cur.execute(statement)
    for row in cur:
        worker_id_list.append(row[0])

pull_worker_ids()

conn = sqlite.connect('civility.db')
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


pair_dict = {}
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
				pair = str(row[4]) + '_' + str(row[5])
				pair_option = str(row[5]) + '_' + str(row[4])
				if pair not in pair_dict.keys() and pair_option not in pair_dict.keys():
					pair_dict[pair] = []
					pair_dict[pair].append({'post_id': str(row[2]), 'civility1': str(row[0]), 'civility2': str(row[1])})	
				elif pair in pair_dict.keys():
					pair_dict[pair].append({'post_id': str(row[2]), 'civility1': str(row[0]), 'civility2': str(row[1])})
				elif pair_option in pair_dict.keys():
					pair_dict[pair_option].append({'post_id': str(row[2]), 'civility1': str(row[0]), 'civility2': str(row[1])})




pair_scores = []
for pair in pair_dict:
	civility_list1 = []
	civility_list2 = []
	for post in pair_dict[pair]:
		civility_list1.append(post['civility1'])
		civility_list2.append(post['civility2'])
	pair_scores.append([civility_list1, civility_list2])







