from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import os

CONTENT_NOT_RELEVANT_TITLE = os.getenv("CONTENT_NOT_RELEVANT_TITLE")
CONTENT_NOT_RELEVANT_BODY = os.getenv("CONTENT_NOT_RELEVANT_BODY")

CONTENT_1_KEYWORD = os.getenv("CONTENT_1_KEYWORD")
CONTENT_1_RESULT_TITLE = os.getenv("CONTENT_1_RESULT_TITLE")
CONTENT_1_RESULT_BODY = os.getenv("CONTENT_1_RESULT_BODY")

CONTENT_2_KEYWORD = os.getenv("CONTENT_2_KEYWORD")
CONTENT_2_RESULT_TITLE = os.getenv("CONTENT_2_RESULT_TITLE")
CONTENT_2_RESULT_BODY = os.getenv("CONTENT_2_RESULT_BODY")

class Input(BaseModel):
    query: str
    filter: Union[str, None] = None
    metadata: Union[str, None] = None

class SearchResult(BaseModel):
    title : str
    body: str
    url: str

class Output(BaseModel):
    search_results: list[SearchResult]

app = FastAPI()

@app.post("/search")
async def search(input: Input):
    print("Endpoint invoked")
    print("Query: ", input.query)
    
    output: Output = Output(search_results=[])
    results = [SearchResult(title="No content found", body="No content found", url="https://example.com"),
               SearchResult(title="No content found", body="No content found", url="https://example.com")]    
    
    if CONTENT_1_KEYWORD in input.query:
        results[0].title = CONTENT_1_RESULT_TITLE
        results[0].body = CONTENT_1_RESULT_BODY
        results[1].title = CONTENT_NOT_RELEVANT_TITLE
        results[1].body = CONTENT_NOT_RELEVANT_BODY
    if CONTENT_2_KEYWORD in input.query:
        results[0].title = CONTENT_2_RESULT_TITLE
        results[0].body = CONTENT_2_RESULT_BODY
        results[1].title = CONTENT_NOT_RELEVANT_TITLE
        results[1].body = CONTENT_NOT_RELEVANT_BODY

    output.search_results = results
    return output
