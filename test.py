#!/usr/bin/python
# coding: UTF-8

import sys
import errno

# https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
# https://github.com/mysql/mysql-connector-python
import mysql.connector


#
# MySQL Information
#
# host : localhost
# user : testuser@localhost / password
# database : testdb
# table : testtable
#
# - - - - - - - - - - 
#
# MySQL command.
#
# Create database
# mysql> CREATE DATABASE testdb;
#
# Use database
# mysql> USE testdb;
#
# Create table
# mysql> CREATE TABLE testdb.testtable (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, name VCHAR(16), lat DOUBLE, lon DOUBLE);
# 
# Create user
#mysql> CREATE USER testuser@localhost IDENTIFIED BY 'password';
#
# Grant user
# mysql> GRANT ALL ON testdb.* TO testuser@localhost;
#
# Login
# $ mysql -utestuser -ppassword
#
# Logout
# mysql> exit
# 
# Insert
# mysql> INSERT INTO testtable (name, lat, lon) VALUES ("honolulu", 21.313627, -157.857784);
# mysql> INSERT INTO testtable (name, lat, lon) VALUES ("naha", 26.213572, 127.687527);
# mysql> INSERT INTO testtable (name, lat, lon) VALUES ("borabora", -16.498990, -151.742255);
#
# Select
# mysql> SELECT * FROM testtable;
#
# Truncate
# mysql> TRUNCATE TABLE testtable;
#



# - - - - - - - - - - - - - - - - - - - -
# Functions - Main
# - - - - - - - - - - - - - - - - - - - -
def main():    
    config = {
      'user': 'testuser',
      'password': 'password',
      'host': 'localhost',
      'database': 'testdb',
      'raise_on_warnings': True
    }

    
    # Connect to database.
    # https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print(err)
        sys.exit(errno.EACCES)
    
    
    # Get cursor
    cursor = cnx.cursor(dictionary=True)


    # Insert data to table.
    # https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
    insert_operation =  ('INSERT INTO testtable '
                '(name, lat, lon) '
                'VALUES (%(name)s, %(lat)s, %(lon)s)')
    insert_params = {
        'name': "honolulu",
        'lat': 21.313627,
        'lon': -157.857784,
    }
    insert_params2 = {
        'name': "naha",
        'lat': 26.213572,
        'lon': 127.687527,
    }
    insert_params3 = {
        'name': "borabora",
        'lat': -16.498990,
        'lon': -151.742255,
    }
        
    try:
        cursor.execute(insert_operation, insert_params)
        cursor.execute(insert_operation, insert_params2)
        cursor.execute(insert_operation, insert_params3)
    except mysql.connector.Error as e:
        print(e)
    

    # Select data from table.
    cursor.execute('SELECT * FROM testtable')
    fetch_array = cursor.fetchall()
    for data in fetch_array:
        print('id[{0}] name[{1}] lat[{2}] lon[{3}]'.format(data['id'], data['name'], data['lat'], data['lon']))
    
    
    # Truncate.
    cursor.execute('TRUNCATE TABLE testtable')
    
    
    # Data commit to database.
    cnx.commit()
    
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    main()

