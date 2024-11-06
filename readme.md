### Start development server
```python
flask run --debug --host=0.0.0.0

### SQLITE
```
import sqlite3

# Connect to an SQLITE database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table 
cursor.execute(''CREATE TABLE IF NOT EXIST stocks 
                date text, trans text, symbol text, qty real, price')
# Insert a row of data 
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY', ) ")#   p r o d u c t - b a c k  
 