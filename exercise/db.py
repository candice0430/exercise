from unittest import result
import pymysql


class DBOperator:

    db = None
    cursor = None

    def __init__(self) -> None:
        if not self.db:
            self.db = pymysql.connect(
                host="localhost",
                user="root",
                passwd="!@#123456iou",
                database="test_py_db"
            )
        self.cursor = self.db.cursor()

    def insert(self,sql):
        print(self.db)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("success")
        except Exception as e:
            self.db.rollback()
            print(e)
            print("rollback...")

    def query(self,sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print(result)

        except:
            pass


db_operator = DBOperator()

if __name__ == '__main__':
    sql = 'insert into active_code(status,code) VALUES (0,"test")'
    DBOperator().insert(sql)
    # sql = 'select * from active_code'
    # db_operator.query(sql)