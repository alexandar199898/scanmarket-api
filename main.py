from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ScanMarket API",
    description="API di base per comparatore svizzero",
    version="0.1.0",
)

origins = [
    "https://scanmarket.ch",
    "https://www.scanmarket.ch",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "service": "scanmarket-api"}

@app.get("/search")
def search(q: str):
    results = [
        {
            "title": f"{q} su Ricardo",
            "price": 350,
            "platform": "Ricardo.ch",
            "link": "https://www.ricardo.ch/",
        },
        {
            "title": f"{q} su Tutti.ch",
            "price": 330,
            "platform": "Tutti.ch",
            "link": "https://www.tutti.ch/",
        },
    ]
    return {"query": q, "results": results}