from db import DBConnection as mydb
class Mahasiswa:
    def __init__(self):
        self.__id=None
        self.__nim=None
        self.__nama=None
        self.__semester=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nim(self):
        return self.__nim
        
    @nim.setter
    def nim(self, value):
        self.__nim = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def semester(self):
        return self.__semester
        
    @semester.setter
    def semester(self, value):
        self.__semester = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nim,self.__nama,self.__semester)
        sql="INSERT INTO mahasiswa (nim,nama,semester) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nim,self.__nama,self.__semester, id)
        sql="UPDATE mahasiswa SET nim = %s,nama = %s,semester = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNIM(self, nim):
        self.conn = mydb()
        val = (self.__nama,self.__semester, nim)
        sql="UPDATE mahasiswa SET nama = %s,semester = %s WHERE nim=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM mahasiswa WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNIM(self, nim):
        self.conn = mydb()
        sql="DELETE FROM mahasiswa WHERE nim='" + str(nim) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nim = self.result[1]
        self.__nama = self.result[2]
        self.__semester = self.result[3]
        self.conn.disconnect
        return self.result
    def getByNIM(self, nim):
        a=str(nim)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa WHERE nim='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__nim = self.result[1]
            self.__nama = self.result[2]
            self.__semester = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__id = ''
            self.__nim = ''
            self.__nama = ''
            self.__semester = ''
            
            self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nama FROM mahasiswa"
        self.result = self.conn.findAll(sql)
        return self.result