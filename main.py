# -*- coding: utf-8 -*-
from fastapi import FastAPI
from app.generator import generate_menu

app = FastAPI(title="Menu SaaS API", version="1.0")

@app.get("/")
def home():
    return {"message": "Backend Menu SaaS attivo 🍝"}

@app.get("/menu")
def menu(items_per_category: int = 2):
    return generate_menu(items_per_category)