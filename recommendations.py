"""
Mapping: predicted waste class -> recommended Nielsen Solutions equipment.
Values based on Nielsen's own product catalogue (compression ratios per waste family).
"""

RECOMMENDATIONS = {
    "cardboard": {
        "label_fr": "Carton",
        "machine": "Presse à balles verticale",
        "reduction": "x8 (200-500 kg/balle)",
        "note": "Idéal grande distribution / e-commerce",
    },
    "glass": {
        "label_fr": "Verre",
        "machine": "Broyeur à verre",
        "reduction": "x4 à x6",
        "note": "Recommandé pour bars, hôtels, restaurants",
    },
    "metal": {
        "label_fr": "Métal",
        "machine": "Presse à paquets / balles métal",
        "reduction": "Densité optimisée pour revente au poids",
        "note": "Séparer ferreux / non-ferreux pour un meilleur prix",
    },
    "paper": {
        "label_fr": "Papier",
        "machine": "Presse à balles verticale (papier/carton)",
        "reduction": "x6 à x8",
        "note": "Sécurise aussi les documents sensibles avant recyclage",
    },
    "plastic": {
        "label_fr": "Plastique",
        "machine": "Compacteur / broyeur plastique",
        "reduction": "Variable selon le flux (PET, films, rigides)",
        "note": "Bien trié, le plastique devient une ressource",
    },
    "trash": {
        "label_fr": "Déchet non recyclable",
        "machine": "Compacteur de déchets classique",
        "reduction": "Réduction de volume standard",
        "note": "Non valorisable — filière déchets ultimes",
    },
}


def get_recommendation(predicted_class: str) -> dict:
    """Return the equipment recommendation for a predicted class.
    Falls back to a generic entry if the class is unknown."""
    return RECOMMENDATIONS.get(
        predicted_class,
        {
            "label_fr": predicted_class,
            "machine": "À déterminer",
            "reduction": "N/A",
            "note": "Contactez Nielsen Solutions pour une étude personnalisée",
        },
    )
