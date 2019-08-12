
#%%
# Import SQL Alchemy
from sqlalchemy import create_engine #i want to create a connection to your database

# Import and establish Base for which classes will be constructed 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session #a connection to the db

#automap base is for reacing tables form an existing database
Base = automap_base()
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/dvd')
Base.prepare(engine, reflect=True)
session = Session(engine)


#%%
Staff = Base.classes.staff
Customer = Base.classes.customer
Payment = Base.classes.payment


#%%
# Some queries - 

for row in session.query(Staff):
    #each row has a property for each col name
    print(row.first_name, row.last_name, row.email)
    break


#%%
# Same idea
for row in engine.execute("SELECT * FROM staff;"):
    print(row) #tuple
    break


#%%
# Complex queries - 


#%%



#%%
for row in session.query(Payment, Customer)    .filter(Payment.customer_id == Customer.customer_id):
    print(row.customer.email, row.payment.amount)
    break


#%%
# Inspect the query itself - what is it doing? cartesian product
q = session.query(Payment, Customer)
    .filter(Payment.customer_id == Customer.customer_id)


#%%
print(q)


#%%
# Some pandas

import pandas as pd


#%%
df = pd.read_sql("SELECT * FROM actor", engine)


#%%
df.head()


#%%
# More complex query

myquery = """
SELECT * FROM (
    SELECT p.*, 
        ROW_NUMBER() 
            OVER(PARTITION BY p.customer_ID ORDER BY p.payment_date)
    FROM payment p
    ) as t WHERE t.row_number = 1

"""


#%%
df1 = pd.read_sql(myquery, engine)


#%%
df1.head()


#%%
get_ipython().run_line_magic('matplotlib', 'inline')
df1.amount.sample(n=50).plot(kind='bar')


#%%
# What about aggregations?  

# SELECT payment.customer_id, sum(payment.amount) FROM payment p GROUP BY 1

from sqlalchemy.sql import func

# SELECT THE COLUMNS
qry = session.query(Payment.customer_id, 
                    func.sum(Payment.amount).label("max_score"))

# GROUP BY and ORDER BY
qry = qry.group_by(Payment.customer_id).order_by(func.sum(Payment.amount).desc())

for _res in qry.all():
    print (_res)
    break


#%%
# The above query with a JOIN

# [40]*750 # pour em out


#%%



