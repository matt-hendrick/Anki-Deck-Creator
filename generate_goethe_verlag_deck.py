import time
import requests
import genanki
import os.path
import random
from argparse import ArgumentParser

from get_soup import get_soup
from remove_prefix import remove_prefix
from anki_card_model import anki_card_model

# Dictionary mapping Goethe Verlag language names to the format used in their URLs
language_mapping = {'Adyghe': 'AD', 'Afrikaans': 'AF', 'Amharic': 'AM', 'Arabic': 'AR', 'Belarusian': 'BE', 'Bulgarian': 'BG', 'Bengali': 'BN', 'Bosnian': 'BS', 'Catalan': 'CA', 'Czech': 'CS', 'Danish': 'DA', 'German': 'DE', 'Greek': 'EL', 'English UK': 'EN', 'Esperanto': 'EO', 'Spanish': 'ES', 'Estonian': 'ET', 'Persian': 'FA', 'Finnish': 'FI', 'French': 'FR', 'Hebrew': 'HE', 'Hindi': 'HI', 'Croatian': 'HR', 'Hungarian': 'HU', 'Armenian': 'HY', 'Indonesian': 'ID', 'Italian': 'IT', 'Japanese': 'JA', 'Georgian': 'KA',
                    'Kazakh': 'KK', 'Kannada': 'KN', 'Korean': 'KO', 'Lithuanian': 'LT', 'Latvian': 'LV', 'Macedonian': 'MK', 'Marathi': 'MR', 'Dutch': 'NL', 'Norwegian - Nynorsk': 'NN', 'Norwegian': 'NO', 'Punjabi': 'PA', 'Polish': 'PL', 'Portuguese PT': 'PT', 'Portuguese BR': 'PX', 'Romanian': 'RO', 'Russian': 'RU', 'Slovak': 'SK', 'Slovene': 'SL', 'Albanian': 'SQ', 'Serbian': 'SR', 'Swedish': 'SV', 'Tamil': 'TA', 'Telugu': 'TE', 'Thai': 'TH', 'Tigrinya': 'TI', 'Turkish': 'TR', 'Ukrainian': 'UK', 'Urdu': 'UR', 'Vietnamese': 'VI', 'Chinese': 'ZH'}


def generate_goethe_verlag_deck(args):
    base_url = "https://www.goethe-verlag.com/book2/"
    new_deck = genanki.Deck(
        2059400110,
        f"{args.language} Deck")

    list_of_media_files = []

    # iterates through each category of phrases
    for page_number in range(1, 43):

        # randomize time slept between media downloads
        sleep_time = random.randint(1, 5)

        # for one digit numbers, a zero is included in the goethe-verlag url
        if page_number < 10:
            page_number = f"0{page_number}"
        page_url = f"https://www.goethe-verlag.com/book2/_VOCAB/EM/EM{language_mapping[args.language]}/{page_number}.HTM"

        # check page and throw error if page returns anything but 200
        page_status = requests.get(page_url).status_code
        if page_status != 200:
            raise Exception(
                f"HTTP error for {page_url}. Page status = {page_status}")

        soup = get_soup(page_url)

        # iterate through all phrases on the page
        for phrase in soup.find_all("div", class_="col-sm-3"):
            english = phrase.find("span", class_="Stil36").get_text()
            other_language = phrase.find("span", class_="Stil46").get_text()
            transliteration = phrase.find("span", class_="Stil39").get_text()

            # clean up image url
            img_url = base_url + \
                remove_prefix(phrase.find("img").get("src"), "../../../")

            # Download jpg instead of using remote image
            image_file_name = args.language + img_url.split("/")[-1]
            if not os.path.isfile(image_file_name):
                doc = requests.get(img_url)
                with open(image_file_name, 'wb') as f:
                    f.write(doc.content)

                # try not to clobber the server by mass downloading a bunch of files
                time.sleep(sleep_time)

            anki_formatted_image = f'<img src="{image_file_name}">'

            # add to list of media files to attach to anki package
            list_of_media_files.append(image_file_name)

            # clean up audio url and download mp3
            audio_cleaned_path = remove_prefix(phrase.find(
                "source").get("src"), "../../../")
            audio_file_name = args.language + audio_cleaned_path.split("/")[-1]
            if not os.path.isfile(audio_file_name):
                audio_url = base_url + audio_cleaned_path
                doc = requests.get(audio_url)

                with open(audio_file_name, 'wb') as f:
                    f.write(doc.content)

                # try not to clobber the server by mass downloading a bunch of files
                time.sleep(sleep_time)

            anki_formatted_audio = "[sound:" + audio_file_name + "]"

            # add to list of media files to attach to anki package
            list_of_media_files.append(audio_file_name)

            # create card and add to deck
            new_note = genanki.Note(
                anki_card_model, [english, other_language, transliteration, anki_formatted_audio, anki_formatted_image])
            new_deck.add_note(new_note)

            if args.verbosity is not None:
                print(new_note)
                print("\n")
                print(f"{len(new_deck.notes)} cards have been added to the deck.")

    if args.verbosity is not None:
        print(f"Finished deck contains {len(new_deck.notes)} cards.")
    new_package = genanki.Package(new_deck)
    new_package.media_files = list_of_media_files
    new_package.write_to_file('output.apkg')

    return new_deck


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Scrape Goethe Verlag language learning resources to generate an Anki deck with audio/video")
    parser.add_argument("-l", "--language",
                        help="Enter in the name of the language you wish to scrape. Example = 'Arabic'")
    parser.add_argument("-v", "--verbosity",
                        action="store_true",
                        help="Add this flag to print out each card as the scraper progresses")
    args = parser.parse_args()

    if args.language is None:
        raise Exception("Must provide a language as an argument")

    args.language = args.language.title()

    generate_goethe_verlag_deck(args)
