from fastapi import FastAPI

app = FastAPI(
    title="LeadDesk Mini API",
    description="Backend API service for LeadDesk Mini Lead Management SaaS",
    version="1.0.0",
)


@app.get("/", tags=["Health"])
async def root():
    return {"message": "Welcome to LeadDesk Mini API"}


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": "LeadDesk Mini API",
    }
