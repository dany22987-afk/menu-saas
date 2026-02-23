# -*- coding: utf-8 -*-
import random
from .descriptions import generate_description

# Piatti con emoji
dishes = {
    "antipasti": ["🥖 Bruschette", "🍅 Caprese", "🥩 Carpaccio", "🦑 Calamari fritti"],
    "primi": ["🍝 Carbonara", "🍝 Amatriciana", "🍄 Risotto ai funghi", "🍤 Spaghetti alle vongole"],
    "secondi": ["🥩 Tagliata", "🐟 Branzino al forno", "🍗 Pollo arrosto", "🥘 Ossobuco"],
    "dolci": ["🍰 Tiramisù", "🍮 Panna cotta", "🍨 Gelato", "🧁 Cupcake"]
}

def generate_menu(items_per_category: int = 2, style: str = "classico", exclude: list = None):
    """
    Genera un menu completo con descrizioni
    - items_per_category: quante portate per categoria
    - style: classico, creativo, gourmet
    - exclude: lista di ingredienti/emoji da escludere
    """
    exclude = exclude or []
    menu = {}
    for category, options in dishes.items():
        # filtra piatti che contengono elementi esclusi
        filtered = [d for d in options if all(e not in d for e in exclude)]
        selected = random.sample(filtered, min(items_per_category, len(filtered)))
        # aggiunge descrizione “AI”
        menu[category] = [{"dish": dish, "description": generate_description(dish, style)} for dish in selected]
    return menu