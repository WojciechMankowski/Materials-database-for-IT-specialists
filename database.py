import sqlite3


class Databass:
    def __init__(self, database_name):
        self.connecion = sqlite3.connect(database_name)
        self.cursor = self.connecion.cursor()

    def __del__(self):
        self.connecion.close()

    def creating_table(self, sql: str):
        # utworzenie tabeli w bazie danych
        self.cursor.execute(sql)
        self.connecion.commit()

    def Insert(self, table, category, category2, url):
        sql = f"INSERT INTO {table} (category, url, category2) VALUES('{category}', '{url}', '{category2}')"
        self.cursor.execute(sql)
        self.connecion.commit()
        self.connecion.close()
    def fetch_all(self, table, category):

        sql = f"SELECT * FROM {table} WHERE category =  '" + category + "'" + "OR category2 ='" + category + "'"
        return self.cursor.execute(sql)

    def fetch_category(self, table):
        sql = f"SELECT DISTINCT category FROM {table}"
        sql2 = f"SELECT DISTINCT category2 FROM {table}"
        return self.cursor.execute(sql).fetchall()
    def fetch_category2(self, table):
        sql = f"SELECT DISTINCT category2 FROM {table}"
        return self.cursor.execute(sql).fetchall()



