from get_soup import get_soup


def get_language_mapping():
    page_url = "https://www.goethe-verlag.com/book2/EM/"

    language_mapping = {}

    soup = get_soup(page_url)

    # iterate through all language headers on the page
    for phrase in soup.find_all("h5"):
        text = phrase.get_text().strip().split(" ")
        language_mapping[" ".join(text[1:])] = text[0]

    print(language_mapping)


if __name__ == "__main__":
    get_language_mapping()
