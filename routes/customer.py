from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User

router = APIRouter()

# Route for customers to download their data
@router.get("/customer/download/")
def download_customer_data(mobile: str, db: Session = Depends(get_db)):
    # Fetch the user based on mobile number
    user = db.query(User).filter(User.mobile == mobile).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.role != "customer":
        raise HTTPException(status_code=403, detail="Access forbidden")

    # Return the user data as a response (for downloading)
    return {
        "name": user.name,
        "mobile": user.mobile,
        "email": user.email,
        "profession": user.profession,
        "city": user.city
    }
        
    