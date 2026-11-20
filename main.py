from fastapi import FastAPI
import os
# QA_RETENTION_CANARY_API_NOT_A_CREDENTIAL
app = FastAPI()
database_location = os.getenv("DATABASE_URL")
@app.get("/health")
def health():
    return {"status": "synthetic QA fixture", "database_configured": bool(database_location)}
