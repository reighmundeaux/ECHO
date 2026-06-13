from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Let's get the backend up
app = FastAPI(
    title="ECHO",
    description="Passive Signals Intelligence Platform",
    version="0.1.0"
)

# CORS middleware - establishes communication path for frontend to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check Endpoint
@app.get("/")
async def root():
    return {
        "system": "ECHO",
        "status": "online",
        "version": "0.1.0",
        "message": "Hello, Clarice..."
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "components": {
            "api": "online",
            "databases": "pending",
            "ollama": "pending",
            "watcher": "pending",
        }
    }