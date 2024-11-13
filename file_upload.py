from fastapi import FastAPI, Depends, File, UploadFile, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from io import StringIO

# Database Setup
DATABASE_URL = "mysql://root:MahitNahi%4012@localhost/data_project"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    role = Column(String(20))  # 'admin' or 'customer'

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI Setup
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Mocked authentication function
def fake_decode_token(token):
    # This should be replaced with actual token decoding logic
    return {"username": token}  # For demo purposes

# Admin Authentication
def get_current_admin(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)  # Replace with actual user retrieval logic
    if user["username"] != "admin":  # Assuming 'admin' is the username
        raise HTTPException(status_code=403, detail="Not authorized")
    return user

# File Upload Endpoint
@app.post("/file_upload/")
async def upload_file(file: UploadFile = File(...), admin: dict = Depends(get_current_admin), db: Session = Depends(get_db)): # type: ignore
    # Read CSV file into DataFrame
    contents = await file.read()
    df = pd.read_csv(StringIO(contents.decode("utf-8")))

    # Assuming the CSV has columns you want to save into the database
    for index, row in df.iterrows():
        user = User(username=row['username'], role='customer')  # Adjust as needed
        db.add(user)
    db.commit()
    return {"filename": file.filename, "detail": "File uploaded successfully!"}

# Token Endpoint (Admin Login without Password)
@app.post("/token")
async def login(username: str):
    # Check if the username is 'admin'
    if username == "admin":  # Simple check for demo purposes
        return {"access_token": username, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Invalid username")





























































'''from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import CSVData
#from fastapi import Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import csv
import io

app = FastAPI()

# Dependency to check if the user is an admin


def get_current_admin_user():
    user_role = "admin"  # Hardcoded for simplicity; replace with actual admin check logic
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can upload data")
    return user_role  ''

security = HTTPBasic()

def get_current_admin_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "hello12":
        raise HTTPException(status_code=403, detail="Only admin can upload data")
    return credentials.username



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
    return {"message": "CSV data uploaded successfully."} '''
