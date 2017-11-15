#! /usr/bin/env

import psycopg2

DBNAME = "news"


def  get_conn(query):
     ''' Connect to database '''
     db = psycopg2.connect(database=DBNAME)
     c = db.cursor()
     c.execute(query)
     return c.fetchall()
     db.close()
        

query1 = """
      SELECT articles.title, Count(*) As views
      FROM articles
      JOIN log
      ON log.path LIKE concat('/article/%', articles.slug)
      GROUP BY articles.title
      ORDER by views DESC
      LIMIT 3;
"""

query2 = """
      SELECT authors.name, Count(*) As views
      FROM authors
      JOIN articles
      ON authors.id = articles.author
      JOIN log
      ON log.path LIKE concat('/article/%', articles.slug)
      GROUP BY authors.name
      ORDER by views DESC
      LIMIT 3;
"""

query3 = """
      SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
      FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
      JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
      ON total.day = errors.day
      WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
      ORDER BY percent DESC;
"""
   
    
def first_query(query):
    results = get_conn(query)
    print('\n1. The most popular three articles of all time are:\n')
    for result in results:
        print ('  ' + str(result[0]) + ' - ' + str(result[1]) + ' views')
        

def second_query(query):
    results = get_conn(query)
    print('\n2. The most popular article authors of all time are:\n')
    for result in results:
        print ('  ' + str(result[0]) + ' - ' + str(result[1]) + ' views')

        
def third_query(query):
    results = get_conn(query)
    print('\n3. The day on which more than 1 percent of requests lead to errors:\n')
    for result in results:
        print ('  ' + str(result[0]) + ' - ' + str(result[1]) + ' %')


first_query(query1)
second_query(query2)
third_query(query3)
