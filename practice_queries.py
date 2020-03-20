import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = """
SELECT
	cc.character_id,
	count(cm.character_ptr_id) as mages,
	count(ccl.character_ptr_id) as clerics,
	count(cf.character_ptr_id) as fighters
FROM charactercreator_character as cc
LEFT JOIN charactercreator_mage as cm ON cm.character_ptr_id=cc.character_id
LEFT JOIN charactercreator_cleric as ccl ON ccl.character_ptr_id=cc.character_id
LEFT JOIN charactercreator_fighter as cf ON cf.character_ptr_id=cc.character_id
"""
result = curs.execute(query).fetchall()
print('charID, mages, clerics, fighters \n', result)