# python-db
Postgre CRUD demo for Python

1、Execute SQL script  

CREATE TABLE users (  

  id SERIAL NOT NULL ,  
  
  name varchar(20) NOT NULL,  
  
  user_name varchar(20) NOT NULL,  
  
  PRIMARY KEY (id)  
  
);  

insert into users(name, user_name) values ('David','David'),('Ben','Ben'),('Eden','Eden');  


2、Install Python dependency libraries if necessary  

pip install psycopg2-binary  


3、Execute db.py  

for example, execute 'python3 db.py' in the command line  

In the db.py file, there are 5 functions that execute insert by default, while the other functions are commented out  

You can execute several other functions to view the results by removing annotations  

