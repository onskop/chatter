from dotenv import load_dotenv
import os
import MySQLdb
import pandas as pd
# Load environment variables from the .env file

envpath = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path=envpath+'/.env')
crt = envpath + '/ca-bundle.crt'

# Connect to the database
connection = MySQLdb.connect(
  host= os.getenv("DATABASE_HOST"),
  user=os.getenv("DATABASE_USERNAME"),
  passwd= os.getenv("DATABASE_PASSWORD"),
  db= os.getenv("DATABASE"),
  autocommit=True,
  ssl_mode="VERIFY_IDENTITY",
  # See https://planetscale.com/docs/concepts/secure-connections#ca-root-configuration
  # to determine the path to your operating systems certificate file.
  ssl={ "ca": crt }
)

try:
    # Create a cursor to interact with the database
    cursor = connection.cursor()


except MySQLdb.Error as e:
    print("MySQL Error:", e)


cursor.execute("select * from users")
response = cursor.fetchall()

df = pd.DataFrame(response, columns=['id', 'name', 'description'], index= None)
df.set_index('id', inplace=True)
print(df)

# Close the cursor and connection
cursor.close()
connection.close()