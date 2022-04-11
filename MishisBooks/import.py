from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
import csv

engine = create_engine(os.getenv("postgresql://nqcfaquakesvau:b66550b48e768d6aa2e69054aa3806f322acd35b77e5c00ccdf9af85d634e661@ec2-44-194-92-192.compute-1.amazonaws.com:5432/d9ef2rp1qjtohv"))

db = scoped_session(sessionmaker(bind=engine)) 


f = open("books.csv")
reader = csv.reader(f)

for isbn, title, author, year in reader:
    db.execute("INSERT INTO books (isbn, title, author, publishyear) VALUES (:isbn, :title, :author, :year)",
            {"isbn": isbn, "title": title, "author": author, "year": year})
    db.commit()
print("yap")
