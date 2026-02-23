# -*- coding: utf-8 -*-
import random

# Descrizioni fittizie stile “AI”
adjectives = ["delizioso", "gustoso", "succulento", "irresistibile", "saporito", "raffinato", "creativo"]

def generate_description(dish_name: str, style: str = "classico"):
    """
    Genera una descrizione “AI” per il piatto
    """
    if style == "creativo":
        return f"{dish_name} è {random.choice(adjectives)} e sorprende con un tocco unico."
    elif style == "gourmet":
        return f"{dish_name} è un capolavoro gourmet, raffinato nei sapori e nella presentazione."
    else:
        return f"{dish_name} è {random.choice(adjectives)}."