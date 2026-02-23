# -*- coding: utf-8 -*-
import random

dishes = {
    "antipasti": ["Bruschette", "Caprese", "Carpaccio"],
    "primi": ["Carbonara", "Amatriciana", "Risotto ai funghi"],
    "secondi": ["Tagliata", "Branzino", "Pollo arrosto"],
    "dolci": ["Tiramisù", "Panna cotta", "Gelato"]
}

def generate_menu(num_items_per_category: int = 2):
    return {
        category: random.sample(items, min(num_items_per_category, len(items)))
        for category, items in dishes.items()
    }