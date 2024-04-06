import sqlite3
from fastapi import FastAPI, HTTPException

data = "FashionAnalysis_temp.db"

app=FastAPI()

def get_db_connection():
    conn = sqlite3.connect(data)
    conn.row_factory = sqlite3.Row
    return conn

@app.get('/')
def read_root():
    return {"message": "Hello, World"}

@app.get("/get_info/{ID}")     
def get_info(ID: int):        #get the id of a person

    conn = get_db_connection()
    person = conn.execute('SELECT * FROM persons WHERE id = ?', (ID,)).fetchone()
    conn.close()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return dict(person)

@app.post("/create_person/")
def create_person(name: str, age: int):        #create a new person

    conn = get_db_connection()
    conn.execute('INSERT INTO persons (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    new_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
    conn.close()
    return {"id": new_id, "name": name, "age": age}

@app.put("/update_person/{ID}")
def update_person(ID: int, name: str = None, age: int = None):        #update an existing person by ID
    conn = get_db_connection()
    person = conn.execute('SELECT * FROM persons WHERE id = ?', (ID,)).fetchone()
    if person is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Person not found")
    
    if name:
        conn.execute('UPDATE persons SET name = ? WHERE id = ?', (name, ID))
    if age is not None:
        conn.execute('UPDATE persons SET age = ? WHERE id = ?', (age, ID))
    
    conn.commit()
    conn.close()
    return {"message": "Person updated successfully", "id": ID, "name": name, "age": age}
