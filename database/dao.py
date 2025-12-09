from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.rifiugio import Rifugio
from datetime import timedelta

class DAO:

    @staticmethod
    def read_rifugi():
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = 'SELECT * FROM rifugio'
        cursor.execute(query)
        for row in cursor:
            result[row['id']] = Rifugio(**row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_connessioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM connessione"
        cursor.execute(query)
        for row in cursor:
            result.append(Connessione(**row))
        cursor.close()
        conn.close()
        return result
