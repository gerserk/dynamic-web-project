# classe???
from fastapi import FastAPI, Request, HTTPException
import json
import uvicorn
import mysql.connector
from mysql.connector import Error
from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# get all data
@app.get("/")
def getall():
    connection = mysql.connector.connect(
    host = "db",
    user = "rubrica",
    password = "rubrica",
    database = "rubrica"
    )
    cursor = connection.cursor()
    cursor.execute('Select * FROM lista_contatti')
    contatti =cursor.fetchall()
    connection.close()
    return {"message": contatti}

# add another entry
@app.post("/")
async def add_or_update(request: Request):
    body = await request.body()
    body = json.loads(body)

    id = body['id']
    nome = body['nome']
    cognome = body['cognome']
    indirizzo = body['indirizzo']
    telefono = body['telefono']
    anni = body['anni']

    connection = mysql.connector.connect(
        host="db",
        user="rubrica",
        password="rubrica",
        database="rubrica"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM lista_contatti WHERE id = %s", (id,))
    existing_user = cursor.fetchone()

    if existing_user:  
        query = """
        UPDATE lista_contatti
        SET nome = %s, cognome = %s, indirizzo = %s, telefono = %s, anni = %s
        WHERE id = %s
        """
        values = (nome, cognome, indirizzo, telefono, anni, id)
        cursor.execute(query, values)
        connection.commit()
        message = "Person updated successfully!"
    else:  
        query = """
        INSERT INTO lista_contatti (id, nome, cognome, indirizzo, telefono, anni)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (id, nome, cognome, indirizzo, telefono, anni)
        cursor.execute(query, values)
        connection.commit()
        message = "Person added successfully!"

    cursor.close()
    connection.close()

    return {"message": message}

@app.delete("/")
async def deleteone(request: Request):
    id = request.query_params.get('id')

    if id is None:
        return {"error": "ID parameter is missing"}

    connection = mysql.connector.connect(
        host="db",
        user="rubrica",
        password="rubrica",
        database="rubrica"
    )
    cursor = connection.cursor()

    query = """
    DELETE FROM lista_contatti
    WHERE id = %s
    """
    values = (id,)

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "person deleted successfully!"}

uvicorn.run(app, host="0.0.0.0", port=5000)