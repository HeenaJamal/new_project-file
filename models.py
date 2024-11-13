from sqlalchemy import Column, Integer, String, Enum
from database import engine , Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    mobile = Column(String(15), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    profession = Column(String(100))
    city = Column(String(100))
    role = Column(Enum('admin', 'customer', name='user_roles'), default='customer')
    otp = Column(String(6))  # OTP field for login

class CSVData(Base):
    __tablename__ = "csv_data"

    id = Column(Integer, primary_key=True, index=True)
    A = Column(String(255), nullable=True)
    B = Column(String(255), nullable=True)
    C = Column(String(255), nullable=True)
    D = Column(String(255), nullable=True)
    E = Column(String(255), nullable=True)
    F = Column(String(255), nullable=True)
    G = Column(String(255), nullable=True)
    H = Column(String(255), nullable=True)
    I = Column(String(255), nullable=True)
    J = Column(String(255), nullable=True)
    K = Column(String(255), nullable=True)
    L = Column(String(255), nullable=True)
    M = Column(String(255), nullable=True)
    N = Column(String(255), nullable=True)
    O = Column(String(255), nullable=True)
    P = Column(String(255), nullable=True)
    Q = Column(String(255), nullable=True)
    R = Column(String(255), nullable=True)
    S = Column(String(255), nullable=True)
    T = Column(String(255), nullable=True)
    U = Column(String(255), nullable=True)
    V = Column(String(255), nullable=True) 