import sqlite3

class MyDatabase:
    def __init__(self,dbname):
        self.database = sqlite3.connect(dbname)
        if self.database !=None:
            print("Database Created.......")

    def createTable(self):
        query = "create table if not exists stud(id integer primary key autoincrement, sname text not null,srollno text not null);"
        self.database.execute(query)
        print("Table Created....")
    
    def insertData(self,sname):
        query = "insert into stud (sname) values ('{}');".format(sname)
        self.database.execute(query)
        self.database.commit()
        print('Inserted Successfully........')

    def selectData(self):
        query = "select * from stud;"
        cursor = self.database.execute(query)
        for row in cursor:
            print(row)

    def deleteData(self,id):
        query = "delete from stud where id = {};".format(id)
        self.database.execute(query)
        self.database.commit()

    def updateData(self,sname,id):
        query = "update stud set sname='{}', where id='{}';".format(sname,id)
        self.database.execute(query)
        self.database.commit()



myDatabase =  MyDatabase('entery.ms')
myDatabase.createTable()       
