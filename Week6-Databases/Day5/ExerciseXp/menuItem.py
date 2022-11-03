import psycopg2

class MenuItem():
    def __init__(self,name,price):
        self.name = name
        self.price = price

    @staticmethod
    def connection():
        HOSTNAME = 'localhost'
        USERNAME = 'postgres'
        PASSWORD = 'root'
        DATABASE = 'menuItems'

        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        return connection

    def save(self):
        con = self.connection()
        cursor = con.cursor()
        query = f"Insert into items (name,price) values ('{self.name}',{self.price});"
        cursor.execute(query)
        con.commit()
        # results = cursor.fetchall()
        cursor.close()
        return True

    def delete(self):
        con = self.connection()
        cursor = con.cursor()
        query = f"Delete from items where name = '{self.name}';"
        cursor.execute(query)
        con.commit()
        # results = cursor.fetchall()
        cursor.close()
        return True

    def update(self,name,price):
        con = self.connection()
        cursor = con.cursor()
        query = f"Update items set name = '{name}',price = {price} where name = '{self.name}';"
        cursor.execute(query)
        con.commit()
        # results = cursor.fetchall()
        cursor.close()

    def all(self):
        con = self.connection()
        cursor = con.cursor()
        query = "select name,price from items;"
        cursor.execute(query)
        con.commit()
        results = cursor.fetchall()
        cursor.close()
        return results

    @classmethod
    def get_by_name(cls,name):
        con = cls.connection()
        cursor = con.cursor()
        query = f"select name,price from items where name ilike '{name}';"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        cursor.close()
        if len(result) > 0:
            return cls(result[0][0],result[0][1])
        return None


# item = MenuItem('Beef Stew', 13)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuItem.get_by_name('Veggie Burger')
# print(item2)
# if item2 != None:
#     items = item2.all()