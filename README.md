# Anki Deck Generator

This is a work in progress repo that generates language Anki decks from publicly available source(s) that provide audio and/or visual in addition to the English and other language text.

Currently, the repo contains one script that can generate Anki decks for 50 languages using the content from [Goethe-Verlag.com] (https://www.goethe-verlag.com/book2/EM/).

To run the script and generate a deck, you must specify the name of the language. The available languages are:

> Adyghe, Afrikaans, Amharic, Arabic, Belarusian, Bulgarian, Bengali, Bosnian, Catalan, Czech, Danish, German, Greek, English UK, Esperanto, Spanish, Estonian, Persian, Finnish, French, Hebrew, Hindi, Croatian, Hungarian, Armenian, Indonesian, Italian, Japanese, Georgian, Kazakh, Kannada, Korean, Lithuanian, Latvian, Macedonian, Marathi, Dutch, Norwegian - Nynorsk, Norwegian, Punjabi, Polish, Portuguese PT, Portuguese BR, Romanian, Russian, Slovak, Slovene, Albanian, Serbian, Swedish, Tamil, Telugu, Thai, Tigrinya, Turkish, Ukrainian, Urdu, Vietnamese, Chinese

An example command is:

    python generate_goether_verlag_deck.py -l Arabic

To have the scraper print out each new card added to the deck, pass in the -v flag. Example:

    python generate_goether_verlag_deck.py -l Finnish -v
