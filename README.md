# Anki Deck Generator

This is a repo that generates language Anki decks from publicly available source(s) that provide audio and/or visual in addition to the English and other language text.

Currently, the repo contains one script that can generate Anki decks for 50 languages using the content from [Goethe-Verlag.com](https://www.goethe-verlag.com/book2/EM/).

To run the script and generate a deck, you must specify the name of the language. The available languages are:

> Adyghe, Afrikaans, Albanian, Amharic, Arabic, Armenian, Belarusian, Bengali, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English UK, Esperanto, Estonian, Finnish, French, Georgian, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Marathi, Norwegian, Norwegian - Nynorsk, Persian, Polish, Portuguese BR, Portuguese PT, Punjabi, Romanian, Russian, Serbian, Slovak, Slovene, Spanish, Swedish, Tamil, Telugu, Thai, Tigrinya, Turkish, Ukrainian, Urdu, Vietnamese

An example command is:

    python generate_goethe_verlag_deck.py -l Arabic

To have the scraper print out each new card added to the deck, pass in the -v flag. Example:

    python generate_goethe_verlag_deck.py -l Finnish -v
