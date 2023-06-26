#pymysql libreria

import pymysql

def get_connection():
        return pymysql.connect(
            host='34.16.150.201',
            user='root',
            password='12345678',
            db='planner'
        )
