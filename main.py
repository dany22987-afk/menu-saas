# -*- coding: utf-8 -*-
from fastapi import FastAPI, Query
from typing import List
from app.generator import generate_menu

app = FastAPI(title="AI Chef Pro API", version="2.0")

@app.get("/")
def home():
    return {"message": "AI Chef Pro 🍝 backend attivo!"}

@app.get("/menu")
def menu(
    items_per_category: int = 2,
    style: str = "classico",
    exclude: List[str] = Query(default=[])
):
    """
    /menu?items_per_category=3&style=creativo&exclude=🥩&exclude=🐟
    """
    return generate_menu(items_per_category, style, exclude)