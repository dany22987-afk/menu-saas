# -*- coding: utf-8 -*-
import random

# Piatti con emoji
dishes = {
    "antipasti": ["🥖 Bruschette", "🍅 Caprese", "🥩 Carpaccio", "🦑 Calamari fritti"],
    "primi": ["🍝 Carbonara", "🍝 Amatriciana", "🍄 Risotto ai funghi", "🍤 Spaghetti alle vongole"],
    "secondi": ["🥩 Tagliata", "🐟 Branzino al forno", "🍗 Pollo arrosto", "🥘 Ossobuco"],
    "dolci": ["🍰 Tiramisù", "🍮 Panna cotta", "🍨 Gelato", "🧁 Cupcake"]
}

# Frasi creative
adjectives = ["delizioso", "gustoso", "succulento", "irresistibile", "saporito"]

def generate_menu(items_per_category: int = 2, style: str = "classico"):
    """
    Genera un menu casuale in stile AI Chef.
    - items_per_category: quanti piatti per categoria
    - style: 'classico' o 'creativo' (aggiunge aggettivi)
    """
    menu = {}
    for category, options in dishes.items():
        selected = random.sample(options, min(items_per_category, len(options)))
        if style == "creativo":
            selected = [f"{dish} ({random.choice(adjectives)})" for dish in selected]
        menu[category] = selected
    return menu