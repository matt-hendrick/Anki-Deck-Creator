import random
import genanki


anki_card_model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    'Card with Audio/Video',
    fields=[
        {
            'name': 'English',
            'font': 'Arial',
        },
        {
            'name': 'Romanian',
            'font': 'Arial',
        },
        {
            'name': 'Audio',
        },
        {
            'name': 'Image',
        },
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{English}}',
            'afmt': '{{FrontSide}}\n\n<hr id=answer>\n\n{{Romanian}}<br>{{Image}}<br>{{Audio}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Romanian}}<br>{{Audio}}',
            'afmt': '{{FrontSide}}\n\n<hr id=answer>\n\n{{English}}<br>{{Image}}',
        },
    ],
    css='.card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n',
)
