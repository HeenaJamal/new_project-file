from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import CSVData
import csv
import io

app = FastAPI()

# Dependency to check if the user is an admin
def get_current_admin_user():
    user_role = "admin"  # Hardcoded for simplicity; replace with actual admin check logic
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can upload data")
    return user_role

@app.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db), admin_user: str = Depends(get_current_admin_user)):
    # Ensure file is a CSV
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")

    # Read CSV data
    contents = await file.read()
    csv_reader = csv.DictReader(io.StringIO(contents.decode('utf-8')))
    
    for row in csv_reader:
        csv_data = CSVData(
            A=row.get('A'),
            B=row.get('B'),
            C=row.get('C'),
            D=row.get('D'),
            E=row.get('E'),
            F=row.get('F'),
            G=row.get('G'),
            H=row.get('H'),
            I=row.get('I'),
            J=row.get('J'),
            K=row.get('K'),
            L=row.get('L'),
            M=row.get('M'),
            N=row.get('N'),
            O=row.get('O'),
            P=row.get('P'),
            Q=row.get('Q'),
            R=row.get('R'),
            S=row.get('S'),
            T=row.get('T'),
            U=row.get('U'),
            V=row.get('V')
        )
        db.add(csv_data)
    
    db.commit()
    return {"message": "CSV data uploaded successfully."}
