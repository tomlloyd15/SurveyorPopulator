from fastapi import FastAPI
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
from pydantic import BaseModel
from main import create_document


class Item(BaseModel):
    address: str
    document_status: int  # 0 - Unsuccessful, 1 - Requesting, 2 - Successful, 3 - Error


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


"""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
"""


@app.get("/map")
def map_image():
    return FileResponse("FastAPI/map.png")


@app.get("/file")
def get_file():
    return FileResponse('Docx_Outputs/combinedExample.docx',
                        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')


@app.post("/items")
def find_address(item: Item):
    print("posted: " + item.address)
    try:
        create_document(item.address, 0.1)
        item.document_status = 2
    except KeyError:
        item.document_status = 3

    print(item.document_status)
    return item.document_status
