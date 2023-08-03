from fastapi import FastAPI
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os



app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/map")
def map_image():
    return FileResponse("map.png")


@app.get("/file")
def get_file():

    return FileResponse('combinedExample.docx',
                        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')




