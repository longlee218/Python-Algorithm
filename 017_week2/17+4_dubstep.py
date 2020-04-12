"""
    Let's assume that a song consists of some number of words. To make the dubstep remix of this song
    ,Vasya inserts a certain number of words "WUB" before the first word of the song (the number may be zero)
    ,after the last word (the number may be zero), and between words (at least one between any pair of neighbouring
    words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club

    For example, a song with words "I AM X" can transform into dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot
    transform into "WUBWUBIAMXWUB"

    INPUT:
        The input consists of a single non-empty string, consisting only of uppercase English letter, the string's
        length doesn't exceed 200 characters. It is guaranteed that before Vasya remix the song, no word contained
        substring "WUB" in it; Vasya didn't change the word order. It is also guaranteed that initially the song had at
        least one word.
    OUTPUT:
        Print the word of the initial song that Vasya used to make a dubstep remix. Separate the words with a space.

"""


def decode():
    strings = ""
    while len(strings) > 200 or len(strings) == 0 or "WUB" not in strings:
        strings = str(input("Enter: ").upper())
    return " ".join(strings.replace('WUB', ' ').split())


if __name__ == '__main__':
    print(decode())
