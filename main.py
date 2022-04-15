import time
import requests
import genanki
import os.path

from get_soup import get_soup
from remove_prefix import remove_prefix
from anki_card_model import anki_card_model


def main():
    base_url = "https://www.goethe-verlag.com/book2/"
    # TODO: Allow passing in variables for both deck name, language, and logging verbosity
    new_deck = genanki.Deck(
        2059400110,
        "Hindi Deck")

    list_of_media_files = []

    # TODO: Dynamically get all pages for a language instead of getting fixed range
    # iterates through each category of phrases
    for page_number in range(1, 43):
        # TODO: rework the need for this
        if page_number < 10:
            page_number = f"0{page_number}"

        page_url = f"https://www.goethe-verlag.com/book2/_VOCAB/EM/EMHI/{page_number}.HTM"

        # check page and throw error if page returns anything but 200
        page_status = requests.get(page_url).status_code
        if page_status != 200:
            raise Exception(
                f"HTTP error for {page_url}. Page status = {page_status}")

        soup = get_soup(page_url)

        # iterate through all phrases on the page
        for phrase in soup.find_all("div", class_="col-sm-3"):
            english = phrase.find("span", class_="Stil36").get_text()
            hindi = phrase.find("span", class_="Stil46").get_text()
            transliteration = phrase.find("span", class_="Stil39").get_text()

            # clean up image url
            img_url = base_url + \
                remove_prefix(phrase.find("img").get("src"), "../../../")

            # Download jpg instead of using remote image
            image_file_name = "Hindi" + img_url.split("/")[-1]
            if not os.path.isfile(image_file_name):
                doc = requests.get(img_url)
                with open(image_file_name, 'wb') as f:
                    f.write(doc.content)

                # try not to clobber the server by mass downloading a bunch of files
                time.sleep(.5)

            anki_formatted_image = f'<img src="{image_file_name}">'

            # add to list of media files to attach to anki package
            list_of_media_files.append(image_file_name)

            # clean up audio url and download mp3
            audio_cleaned_path = remove_prefix(phrase.find(
                "source").get("src"), "../../../")
            audio_file_name = "Hindi" + audio_cleaned_path.split("/")[-1]
            if not os.path.isfile(audio_file_name):
                audio_url = base_url + audio_cleaned_path
                doc = requests.get(audio_url)

                with open(audio_file_name, 'wb') as f:
                    f.write(doc.content)

                # try not to clobber the server by mass downloading a bunch of files
                time.sleep(.5)

            anki_formatted_audio = "[sound:" + audio_file_name + "]"

            # add to list of media files to attach to anki package
            list_of_media_files.append(audio_file_name)

            # create card and add to deck
            new_note = genanki.Note(
                anki_card_model, [english, hindi, transliteration, anki_formatted_audio, anki_formatted_image])
            new_deck.add_note(new_note)
            print(new_note)
            print("\n")

    new_package = genanki.Package(new_deck)
    new_package.media_files = list_of_media_files
    new_package.write_to_file('output.apkg')

    return new_deck


if __name__ == "__main__":
    main()
