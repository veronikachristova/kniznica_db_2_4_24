import psycopg2
#na prepojenie databazy so serverom

conn = psycopg2.connect(
    dbname='bva2e94t1hjabargw4qm',
    user='uoxfcfn6z1ax4uvdhs8d',
    password='BqNof4FiTkz7VmAFcWYqzxjR5vMqRv',
    host='bva2e94t1hjabargw4qm-postgresql.services.clever-cloud.com',
    port='50013'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM authors')
autori= cursor.fetchall()
print(autori)

cursor.execute('SELECT * FROM authors')
prvy_autor = cursor.fetchone()
print(prvy_autor)

cursor.execute('SELECT * FROM authors ORDER BY author_id DESC')
posledny_autor = cursor.fetchone()
print(posledny_autor)



cursor.close()  # ked koncis pracu s databazou tak to skoncis
conn.close()  #zatvaras kompletne cele spojenie, cize ho budes musiet znova prepojit ked budes chciet robit s data

#vytvorime novy objekt
