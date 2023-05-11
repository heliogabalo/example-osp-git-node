####### SECTION import libraries #######
import mysql.connector
from mysql.connector import Error
import pandas as pd


####### connect to the serer and create database #######
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

pw = "******" # IMPORTANT! Put your MySQL Terminal password here.
db = "customers_db" # This is the name of the database we will create in the next step - call it whatever you like.

connection = create_server_connection("localhost", "root", pw)


####### SECTION create new database #######
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE customers_db"
create_database(connection, create_database_query)

####### SECTION modify server connectionfunction #######
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
    

####### SECTION define query execution function #######
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        
        
####### SECTION create tables #######

def create_clients_table = """
    CREATE TABLE clients(
      client_id INT PRIMARY KEY,
      client_name VARCHAR(40) NOT NULL,
      client_address VARCHAR(60) NOT NULL,
      client_industry VARCHAR(20),
      client_notes VARCHAR(60),
      client_telephone INT,
      client_status BOOLEAN
    );
"""

def create_products_table = """
    CREATE TABLE products(
      product_id INT PRIMARY KEY,
      product_name VARCHAR(40) NOT NULL,
      product_description VARCHAR(60) NOT NULL,
      product_price decimal,
      product_discount decimal,
      product_tax decimal,
      product_pvp decimal,
      product_status BOOLEAN
    );
"""

def create_services_table = """
    CREATE TABLE services(
      service_id INT PRIMARY KEY,
      service_name VARCHAR(40) NOT NULL,
      service_description VARCHAR(60) NOT NULL,
      service_price decimal,
      service_discount decimal,
      service_tax decimal,
      service_pvp decimal,
      service_status BOOLEAN
    );
"""

def create_offers_table = """
    CREATE TABLE offers(
      offer_id INT PRIMARY KEY,
      offer_name VARCHAR(40) NOT NULL,
      offer_description VARCHAR(60) NOT NULL,
      offer_price decimal,
      offer_discount decimal,
      offer_tax decimal,
      offer_pvp decimal,
      offer_status BOOLEAN
    );
"""

def create_budgets_table = """
    CREATE TABLE budgets(
      budget_id INT PRIMARY KEY,
      budget_name VARCHAR(40) NOT NULL,
      budget_description VARCHAR(60) NOT NULL,
      budget_price decimal,
      budget_discount decimal,
      budget_tax decimal,
      budget_pvp decimal,
      budget_status BOOLEAN
    );
"""

def create_bills_table = """
    CREATE TABLE bills(
      bill_id INT PRIMARY KEY,
      bill_name VARCHAR(40) NOT NULL,
      bill_description VARCHAR(60) NOT NULL,
      bill_price decimal,
      bill_discount decimal,
      bill_tax decimal,
      bill_pvp decimal,
      bill_status BOOLEAN
    );
"""

def create_orders_table = """
    CREATE TABLE orders(
      order_id INT PRIMARY KEY,
      order_name VARCHAR(40) NOT NULL,
      order_description VARCHAR(60) NOT NULL,
      order_price decimal,
      order_discount decimal,
      order_tax decimal,
      order_pvp decimal,
      order_status BOOLEAN
    );
"""

def create_delivery_notes_table = """
    CREATE TABLE delivery_notes(
      dn_id INT PRIMARY KEY,
      dn_name VARCHAR(40) NOT NULL,
      dn_description VARCHAR(60) NOT NULL,
      dn_price decimal,
      dn_discount decimal,
      dn_tax decimal,
      dn_pvp decimal,
      dn_status BOOLEAN
    );
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_clients_table)
execute_query(connection, create_products_table)
execute_query(connection, create_services_table)
execute_query(connection, create_offers_table)
execute_query(connection, create_budgets_table)
execute_query(connection, create_bills_table)
execute_query(connection, create_orders_table)
execute_query(connection, create_delivery_notes_table)


######### SECTION alter_tables ##########

alter_clients = """
  pass
"""

alter_products = """
  pass
"""

alter_services = """
  pass
"""

alter_offers = """
  ALTER TABLE offers
  ADD FOREIGN KEY(clints)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""

alter_budgets = """
  ALTER TABLE budgets
  ADD FOREIGN KEY(clints)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""

alter_bills = """
  ALTER TABLE bills
  ADD FOREIGN KEY(clints)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""

alter_orders = """
  ALTER TABLE orders
  ADD FOREIGN KEY(clints)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""

alter_delivery_notes = """
  ALTER TABLE delivery_notes
  ADD FOREIGN KEY(clints)
  REFERENCES clients(client_id)
  ON DELETE SET NULL;
"""


connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, alter_clients_table)
execute_query(connection, alter_products_table)
execute_query(connection, alter_services_table)
execute_query(connection, alter_offers_table)
execute_query(connection, alter_budgets_table)
execute_query(connection, alter_bills_table)
execute_query(connection, alter_orders_table)
execute_query(connection, alter_delivery_notes_table)
#execute_query(connection, create_takescourse_table)

####### SECTION populate table function ########

pop_clients = """
INSERT INTO clients VALUES
('field', 'field', 'field', 'field', 'field', 'field', 'field'),
('field', 'field', 'field', 'field', 'field', 'field', 'field');
"""

pop_products = """
INSERT INTO products VALUES
('field', 'field', 'field', 'field', 'field', 'field', 'field'),
('field', 'field', 'field', 'field', 'field', 'field', 'field');
"""

pop_services = """
INSERT INTO services VALUES
('field', 'field', 'field', 'field', 'field', 'field', 'field'),
('field', 'field', 'field', 'field', 'field', 'field', 'field');
"""

pop_offers = """
INSERT INTO offers VALUES
('field', 'field', 'field', 'field', 'field', 'field', 'field'),
('field', 'field', 'field', 'field', 'field', 'field', 'field');
"""

pop_budgets = """
INSERT INTO budgets VALUES
('field', 'field', 'field', 'field', 'field', 'field', 'field'),
('field', 'field', 'field', 'field', 'field', 'field', 'field');
"""

pop_bills = """
INSERT INTO bills VALUES
('field', 'field', 'field', 'field', 'field', 'field', 'field'),
('field', 'field', 'field', 'field', 'field', 'field', 'field');
"""

pop_orders = """
INSERT INTO orders VALUES
('field', 'field', 'field', 'field', 'field', 'field', 'field'),
('field', 'field', 'field', 'field', 'field', 'field', 'field');
"""

pop_delivery_nontes = """
INSERT INTO delivery_nontes VALUES
('field', 'field', 'field', 'field', 'field', 'field', 'field'),
('field', 'field', 'field', 'field', 'field', 'field', 'field');
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, pop_table)