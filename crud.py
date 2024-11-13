from sqlalchemy.orm import Session
from models import User
from schemas import SignupRequest,LoginRequest,UserResponse
from utils import generate_otp

# Create a new user (customer or admin)
def create_user(db: Session, user: SignupRequest, role: str = "customer"):
    new_user = User(
        name=user.name,
        mobile=user.mobile,
        email=user.email,
        profession=user.profession,
        city=user.city,
        role=role,
        otp=generate_otp()  # Generate random OTP
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get user by mobile number
def get_user_by_mobile(db: Session, mobile: str):
    return db.query(User).filter(User.mobile == mobile).first()

# Check if email or mobile exists
def check_user_exists(db: Session, email: str, mobile: str):
    return db.query(User).filter((User.email == email) | (User.mobile == mobile)).first()

# Generate and save OTP for user
def update_otp(db: Session, user: User):
    user.otp = generate_otp()  # Generate a new OTP
    db.commit()
    db.refresh(user)
    return user

