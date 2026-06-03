LIGHT_ALLOWED: list[str] = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    lower = ingredients.lower()
    for allowed in LIGHT_ALLOWED:
        if allowed in lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
