import uvicorn
from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI()


@app.post('/api/registration')
def registration(data: Dict[Any, Any]):
    return 200

uvicorn.run(app, host="0.0.0.0", port=1001)