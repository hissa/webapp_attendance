"""
DB接続と切断を行う
"""

import sqlite3

class Database:
    @staticmethod
    def get_connection():
        conn = sqlite3.connect('models/database.sqlite3')
        return conn

    def query(self, sql):
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except sqlite3.Error as e:
	        print(e)
        finally:
            conn.close()

    def run(self, sql):
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except sqlite3.Error as e:
	        print(e)
        finally:
            conn.close()