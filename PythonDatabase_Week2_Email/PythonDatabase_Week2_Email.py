'''
Week2 assignment1:
------------------------------------------------------------------------------
Author: MiracleZhang 
Date: May, 2016
------------------------------------------------------------------------------
'''

import sqlite3

# store the file in the countPerOrg.sqlite
conn = sqlite3.connect('countPerOrg.sqlite')
# connect object
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')

if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)	
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    orgs = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (orgs, ))
    try:
    	row = cur.fetchone()[0]
    	cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (orgs, ))
    except:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (orgs, ))
  
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in conn.execute(sqlstr) :
    print str(row[0]), row[1]

conn.close()


# import sqlite3

# conn = sqlite3.connect('orgs.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# fname = raw_input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'mbox.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '):
#         continue
#     pieces = line.split()
#     email = pieces[1]
#     org = email.split('@')[1]
#     cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
#     try:
#         count = cur.fetchone()[0]
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))
#     except:
#         cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org, ))

# conn.commit()

# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
# for row in conn.execute(sqlstr):
#     print row[0], row[1]

# conn.close()