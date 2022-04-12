import genanki

anki_card_model = genanki.Model(
    1485830179,
    'Card with Audio/Video',
    fields=[
        {
            'name': 'English',
            'font': 'Arial',
        },
        {
            'name': 'Hindi',
            'font': 'Arial',
        },
        {
            'name': 'Transliteration',
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
            'afmt': '{{FrontSide}}\n\n<hr id=answer>\n\n{{Hindi}}\n\n{{Transliteration}}\n\n<img src={{Image}}><br>{{Audio}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Hindi}}\n\n{{Transliteration}}<br>{{Audio}}',
            'afmt': '{{FrontSide}}\n\n<hr id=answer>\n\n{{English}}\n\n<img src={{Image}}>',
        },
    ],
    css='.card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n',
)
