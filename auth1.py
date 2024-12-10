from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader



API_KEY = "admin123"  # Hardcoded API key for admin

api_key_header = APIKeyHeader(name="Authorization")

def get_admin_user(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Not authorized")
    return "admin".
