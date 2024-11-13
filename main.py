from fastapi import FastAPI
from database import engine, Base
from routes import auth, customer
 



# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include authentication routes
app.include_router(auth.router, prefix="/auth")
app.include_router(customer.router)


