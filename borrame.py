import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse("postgres://avcqayrpxqjeqv:p6TX2Vd4Bqm0nvzuHWS29g0-4p@ec2-54-227-253-238.compute-1.amazonaws.com:5432/d7h3k6h1jg61g3")

conn = psycopg2.connect(
    database="d7h3k6h1jg61g3",
    user="avcqayrpxqjeqv",
    password="p6TX2Vd4Bqm0nvzuHWS29g0-4p",
    host="ec2-54-227-253-238.compute-1.amazonaws.com",
    port=5432
)


cur = conn.cursor()
try:
    cur.execute("""select * from "Borrame" """)
except:
    print "I can't SELECT from Borrame"

rows = cur.fetchall()
print "\nRows: \n"
for row in rows:
    print row[0], "   ", row[1]



