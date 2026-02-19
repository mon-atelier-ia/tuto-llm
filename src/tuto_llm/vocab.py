"""Vocabulaire partagé pour le mini-LLM.

Définit l'alphabet, les mappings caractère<->id et les constantes
utilisées dans les notebooks 3, 4 et 5.
"""

VOCAB: list[str] = list(".abcdefghijklmnopqrstuvwxyz")
"""Alphabet du modèle : '.' (début/fin) + 26 lettres minuscules."""

VOCAB_SIZE: int = len(VOCAB)
"""Nombre de tokens dans le vocabulaire (27)."""

char_to_id: dict[str, int] = {c: i for i, c in enumerate(VOCAB)}
"""Mapping caractère -> identifiant numérique."""

id_to_char: dict[int, str] = {i: c for i, c in enumerate(VOCAB)}
"""Mapping identifiant numérique -> caractère."""
