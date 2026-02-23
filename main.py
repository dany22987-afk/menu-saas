# -*- coding: utf-8 -*-
from fastapi import FastAPI
from app.generator import generate_menu

app = FastAPI(title="AI Chef Menu API", version="1.0")

@app.get("/")
def home():
    return {"message": "AI Chef 🍝 backend attivo!"}

@app.get("/menu")
def menu(items_per_category: int = 2, style: str = "classico"):
    """
    /menu?items_per_category=2&style=creativo
    """
    return generate_menu(items_per_category, style)