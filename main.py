import time
import requests
import genanki
import os.path

from get_soup import get_soup
from remove_prefix import remove_prefix
from anki_card_model import anki_card_model


def main():
    base_url = "https://www.goethe-verlag.com/book2/"
    new_deck = genanki.Deck(
        2059400110,
        "Hindi Animals Test Deck")

    soup = get_soup(
        "https://www.goethe-verlag.com/book2/_VOCAB/EM/EMHI/02.HTM")

    for phrase in soup.find_all("div", class_="col-sm-3"):
        english = phrase.find("span", class_="Stil36").get_text()
        hindi = phrase.find("span", class_="Stil46").get_text()
        transliteration = phrase.find("span", class_="Stil39").get_text()

        # clean up image url
        img_url = base_url + \
            remove_prefix(phrase.find("img").get("src"), "../../../")

        # TODO: Download jpg instead of using remote image
        # image_file_name = img_url.split("/")[-1]
        # doc = requests.get(img_url)
        # with open(image_file_name, 'wb') as f:
        #     f.write(doc.content)
        # anki_formatted_image = f'<img src="{image_file_name}">'

        # clean up audio url and download mp3
        audio_cleaned_path = remove_prefix(phrase.find(
            "source").get("src"), "../../../")
        audio_file_name = audio_cleaned_path.split("/")[-1]
        if not os.path.isfile(audio_file_name):
            audio_url = base_url + audio_cleaned_path
            doc = requests.get(audio_url)

            with open(audio_file_name, 'wb') as f:
                f.write(doc.content)

        anki_formatted_audio = "[sound:" + audio_file_name + "]"

        # try not to clobber the server by mass downloading a bunch of files
        time.sleep(1)

        # create card and add to deck
        new_note = genanki.Note(
            anki_card_model, [english, hindi, transliteration, anki_formatted_audio, img_url])
        new_deck.add_note(new_note)

        print(new_note)
        print("\n")

    genanki.Package(new_deck).write_to_file('output.apkg')
    return new_deck


if __name__ == "__main__":
    main()
