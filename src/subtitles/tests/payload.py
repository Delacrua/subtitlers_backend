FILM_DATA = {
    "title": "some_film_A",
    "other_titles": {},
    "released": 1997,
    "duration": "1:15:20",
    "difficulty_level": "beginner",
    "description": "some description",
    "summary": "some summary",
    "words": [
        {
            "text": "Word_a",
            "translations": None,
            "definition": "A_definition",
            "is_uncommon": True,
            "quantity": 5,
        },
        {
            "text": "Word_b",
            "translations": None,
            "definition": "B_definition",
            "is_uncommon": True,
            "quantity": 7,
        },
    ],
    "phrases": [
        {
            "text": "Phrase_A",
            "translations": None,
            "definition": "A_definition",
            "is_idiom": True,
        },
        {
            "text": "Phrase_B",
            "translations": None,
            "definition": "B_definition",
            "is_uncommon": True,
        },
    ],
    "questions": [
        {
            "question_text": "Question_A",
            "question_translations": None,
            "answer_text": "Answer_A",
            "answer_translations": None,
        },
        {
            "question_text": "Question_B",
            "question_translations": None,
            "answer_text": "Answer_B",
            "answer_translations": None,
        },
    ],
}

FILM_EVENT_DATA = {
    "event": "film.created",
    "film_data": FILM_DATA,
}
