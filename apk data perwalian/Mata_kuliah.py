from db import DBConnection as mydb
import mysql.connector

class Mata_kuliah:
    def __init__(self):
        self.__id=None
        self.__mahasiswa_id=None
        self.__nama_mk=None
        self.__sks=None
        self.__date=None
        self.conn = None
        self.affected = None
        self.result = None
        
    def __init__(self):
        # Inisialisasi koneksi database
        self.conn = mysql.connector.connect(
            host="sql.freedb.tech",
            user="freedb_mfaiz",
            password="C8jzgC2NJP%PssJ",
            database="freedb_perwalian" )
    @property
    def id(self):
        return self.__id
    @property
    def mahasiswa_id(self):
        return self.__mahasiswa_id
        
    @mahasiswa_id.setter
    def mahasiswa_id(self, value):
        self.__mahasiswa_id = value
    @property
    def nama_mk(self):
        return self.__nama_mk
        
    @nama_mk.setter
    def nama_mk(self, value):
        self.__nama_mk = value
    @property
    def sks(self):
        return self.__sks
        
    @sks.setter
    def sks(self, value):
        self.__sks = value
    @property
    def date(self):
        return self.__date
        
    @date.setter
    def date(self, value):
        self.__date = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__mahasiswa_id,self.__nama_mk,self.__sks,self.__date)
        sql="INSERT INTO mata_kuliah (mahasiswa_id,nama_mk,sks,date) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__mahasiswa_id,self.__nama_mk,self.__sks,self.__date, id)
        sql="UPDATE mata_kuliah SET mahasiswa_id = %s,nama_mk = %s,sks = %s,date = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateBy(self, ):
        self.conn = mydb()
        val = (self.__mahasiswa_id,self.__nama_mk,self.__sks,self.__date, )
        sql="UPDATE mata_kuliah SET mahasiswa_id = %s,nama_mk = %s,sks = %sdate = %s WHERE =%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM mata_kuliah WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def deleteBy(self, mahasiswa_id, nama_mk):
        cursor = self.conn.cursor()
        sql = "DELETE FROM mata_kuliah WHERE mahasiswa_id = %s AND nama_mk = %s"
        try:
            cursor.execute(sql, (mahasiswa_id, nama_mk))
            self.conn.commit()  # Commit perubahan ke database
            affected_rows = cursor.rowcount
            return affected_rows
        except mysql.connector.Error as e:
            print("Error:", e)
            self.conn.rollback()
            return None
        finally:
            cursor.close()  # Tutup kursor setelah penggunaan selesai

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM mata_kuliah WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__mahasiswa_id = self.result[1]
        self.__nama_mk = self.result[2]
        self.__sks = self.result[3]
        self.__date = self.result[4]
        self.conn.disconnect
        return self.result
    def getBy(self, ):
        a=str()
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM mata_kuliah WHERE ='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__mahasiswa_id = self.result[1]
            self.__nama_mk = self.result[2]
            self.__sks = self.result[3]
            self.__date = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__id = ''
            self.__mahasiswa_id = ''
            self.__nama_mk = ''
            self.__sks = ''
            self.__date = ''
            
            self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM mata_kuliah"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nama_mk FROM mata_kuliah"
        self.result = self.conn.findAll(sql)
        return self.result