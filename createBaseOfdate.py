import sqlite3

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()
c . execute(' CREATE TABLE review_db (review text, sentiment INTEGER, date text) ')
example1 = 'I love this move'
c.execute("INSERT INTO review_db (review, sentiment, date) VALUES (?, ?, DATETIME ('now'))", (example1, 1))
example2 = 'I disliked this move'
c.execute("INSERT INTO review_db (review, sentiment, date) VALUES (?, ?, DATETIME ('now'))", (example2, 0))
c.execute("SELECT * FROM review_db WHERE date BETWEEN '2015-01-01 00:00:00' AND DATETIME ('now')")
results = c.fetchall()
print(results)
conn.commit()
conn.close()
