import sqlite3

class DBManager():
    def __init__(self, ruta_basedatos):
        self.ruta_basedatos = ruta_basedatos

    def consultaSQL(self, consulta):
        conn = sqlite3.connect(self.ruta_basedatos)
        cur = conn.cursor()
        cur.execute(consulta)
        
        keys=[]
        for item in cur.description:
            keys.append(item[0])
        
        registros = []

        for registro in cur.fetchall():
            ix_clave=0
            d={}

            for columna in keys:
                d[columna] = registro[ix_clave]
                ix_clave += 1
            registros.append(d)

        conn.close()
        return registros

    def modificaSQL(self, consulta, params):
        conn = sqlite3.connect(self.ruta_basedatos)

        cur = conn.cursor()
        claves = params.keys()

        cur.execute(consulta, params)
        conn.commit()
        conn.close()

    