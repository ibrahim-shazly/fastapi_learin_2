from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1' : {'title' : 'Title one', 'author' : 'Author one'},
    'book_2' : {'title' : 'Title two', 'author' : 'Author two'},
    'book_3' : {'title' : 'Title three', 'author' : 'Author three'},
    'book_4' : {'title' : 'Title four', 'author' : 'Author four'},
    'book_5' : {'title' : 'Title five', 'author' : 'Author five'},
}

class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "east"
    west = "West"


@app.get("/")
async def read_All_bboks():
    return BOOKS


@app.get("/books/mybook")
async def read_All_books():
    return {'book title' : 'My favorite book Title'}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {'book title' : book_id}

################################3

@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {'Direction': direction_name, "sub" : "Up"}
    if direction_name == DirectionName.south:
        return {'Direction': direction_name, "sub" : "Down"}
    if direction_name == DirectionName.west:
        return {'Direction': direction_name, "sub" : "Left"}
    return {'Direction': direction_name, "sub" : "Right"}


    north = "North"
    south = "South"
    east = "east"
    west = "West"