from dateutil import parser
import uuid
import datetime
import genanki

from get_soup import get_soup
from remove_prefix import remove_prefix
from anki_card_model import anki_card_model


def main():
    base_url = "https://www.goethe-verlag.com/book2/"
    new_deck = genanki.Deck(
        2059400110,
        "Animals")

    soup = get_soup(
        "https://www.goethe-verlag.com/book2/_VOCAB/EM/EMHI/02.HTM")

    for phrase in soup.find_all("div", class_="col-sm-3"):
        english = phrase.find("span", class_="Stil36").get_text()
        hindi = phrase.find("span", class_="Stil46").get_text()
        transliteration = phrase.find("span", class_="Stil39").get_text()
        img_url = base_url + \
            remove_prefix(phrase.find("img").get("src"), "../../../")
        audio_url = "[sound:" + base_url + remove_prefix(phrase.find(
            "source").get("src"), "../../../") + "]"
        card_id = str(uuid.uuid4())
        # card_list.append({"english": english, "hindi": hindi,
        #                 "transliteration": transliteration, "img_url": img_url, "audio_url": audio_url, "card_id": card_id})
       #   print(card_list[-1])
        new_note = genanki.Note(
            anki_card_model, [english, hindi, transliteration, audio_url, img_url])
        new_deck.add_note(new_note)
        print(new_note)
        print("\n")

    genanki.Package(new_deck).write_to_file('output.apkg')
    return new_deck


if __name__ == "__main__":
    main()
