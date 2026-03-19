#
# Word frequency.
# Your name:
#  - Ísak Elí Hauksson
#

from my_dict import MyDict


def read_in_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        return text


def word_frequency_alphabetical_pydict(text: str) -> list[tuple[str, int]]:
    """
    Returns a list of (word, frequency) tuples ordered alphabetically, with all words translated to lowercase,
    e.g., given the text "I am so so happy happy Happy" it returns [('am', 1), ('happy', 3), ('i', 1), ('so', 2)].
    Should be implemented using Python's build-in dictionary.
    :param text: text to process
    :return: list of word frequencies
    """

    text_list: list[str] = text.lower().split()
    word_frequency: dict[str, int] = {}

    for word in text_list:
        if word_frequency.get(word) is None:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1

    return sorted([(key, word_frequency[key]) for key in word_frequency])


def word_frequency_alphabetical_mydict(text):
    """
    Returns a list of (word, frequency) tuples ordered alphabetically, with all words translated to lowercase,
    e.g., given the text "I am so so happy happy Happy" it returns [('am', 1), ('happy', 3), ('i', 1), ('so', 2)].
    Should be implemented using your dictionary implementation (MyDict).
    :param text: text to process
    :return: list of word frequencies
    """
    text_list: list[str] = text.lower().split()
    word_frequency: MyDict = MyDict()

    for word in text_list:
        if word_frequency.get(word) is None:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1  # type: ignore

    return sorted([(key, word_frequency[key]) for key in word_frequency])


if __name__ == "__main__":
    text = read_in_text("data/word1.txt")
    l_py = word_frequency_alphabetical_pydict(text)
    print(l_py)
    l_my = word_frequency_alphabetical_mydict(text)
    print(l_my)
    if l_py == l_my:
        print("Yes!")
    else:
        print("No!")
