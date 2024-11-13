from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from io import StringIO
import csv
from database import get_db  # Assuming get_db is your database session dependency
from file_upload import upload_csv  # Assuming UploadedData is your model for storing admin-uploaded data

app = FastAPI()

# API for downloading data as CSV
@app.get("/download_data/{user_id}", response_class=StreamingResponse)
def download_data(user_id: int, number_of_records: int, db: Session = Depends(get_db)):
    # Fetch data uploaded by admin, filtered by user_id
    data_query = db.query(upload_csv).filter(upload_csv.user_id == user_id).limit(number_of_records).all()

    # Check if data exists
    if not data_query:
        raise HTTPException(status_code=404, detail="No data found for the given user")

    # Prepare the CSV output
    output = StringIO()
    writer = csv.writer(output)
    
    # Write CSV headers
    writer.writerow(["Record ID", "User ID", "Data", "Timestamp"])  # Adjust the headers based on your data model
    
    # Write the data rows
    for record in data_query:
        writer.writerow([record.id, record.user_id, record.data_field, record.timestamp])  # Adjust fields as per your model
    
    output.seek(0)  # Reset cursor to the beginning of the stream
    
    # Return as a streaming response with appropriate headers
    response = StreamingResponse(output, media_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename=user_{user_id}_data.csv"
    
    return response
