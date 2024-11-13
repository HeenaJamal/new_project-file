from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import SignupRequest, LoginRequest, UserResponse
from crud import create_user, get_user_by_mobile, check_user_exists, update_otp
from database import get_db



router = APIRouter()

# Signup route (for both admin and customer)
@router.post("/signup/", response_model=UserResponse)
def signup(user: SignupRequest, db: Session = Depends(get_db)):
    # Check if the email or mobile already exists
    if check_user_exists(db, user.email, user.mobile):
        raise HTTPException(status_code=400, detail="Email or Mobile already registered")

    new_user = create_user(db=db, user=user, role="customer")
    return {"name": new_user.name, "role": new_user.role}

# Login route (for both admin and customer)
@router.post("/login/", response_model=UserResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    # Check if the user exists
    user = get_user_by_mobile(db, login_data.mobile)
    if not user or user.otp != login_data.otp:
        raise HTTPException(status_code=400, detail="Invalid mobile number or OTP")

    # Return user's name and role
    return {"name": user.name, "role": user.role}

# Create a hardcoded admin user
@router.on_event("startup")
def create_admin(db: Session = next(get_db())):
    admin = get_user_by_mobile(db, "9875645678")  # Admin's mobile number
    if not admin:
        create_user(
            db=db,
            user=SignupRequest(
                name="Admin",
                mobile="9875645678",
                email="admin@gmail.com",
                profession="Admin",
                city="pune"
            ),
            role="admin")
        


