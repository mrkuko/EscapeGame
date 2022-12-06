import re

import pronouncing as pr
from typing import Tuple


def is_haiku(text: str) -> Tuple[bool, str]:
    lines = text.split('\n')
    non_empty_lines = []
    for line in lines:
        if line.strip() == '':
            continue
        non_empty_lines.append(line)
    try:
        if len(non_empty_lines) != 3:
            return False, "Incorrect number of lines: " \
                   + str(len(non_empty_lines))

        if count_syllables(non_empty_lines[0]) != 5:
            return False, "Incorrect number of syllables on line 1: " \
                   + str(count_syllables(non_empty_lines[0]))

        if count_syllables(non_empty_lines[1]) != 7:
            return False, "Incorrect number of syllables on line 2: " \
                   + str(count_syllables(non_empty_lines[1]))

        if count_syllables(non_empty_lines[2]) != 5:
            return False, "Incorrect number of syllables on line 3: " \
                   + str(count_syllables(non_empty_lines[2]))
    except ValueError as e:
        return False, str(e)
    return True, "Correct"


def count_syllables(line: str) -> int:
    words = re.findall(r'\b(\w+)\b', line)
    if len(words) == 0:
        return 0

    counts = map(count_syllables_word, map(str.lower, words))
    return sum(counts)


def count_syllables_word(word: str) -> int:
    phones = pr.phones_for_word(word)
    if len(phones) == 0:
        raise ValueError("Word does not exist: " + word)
    return pr.syllable_count(phones[0])


HAIKU = """
Skeleton Mountain —

the bones of long-horned bison

wash down from the slopes
"""

NOT_HAIKU = """
what picture do the stars scrawl
connecting the dots . . .
across the night sky
"""

NOT_HAIKU2 = """
Skeleton Mountain —
the bones of long-horned bison
wash down from the slopes, Hi
"""

NOT_HAIKU3 = """
Skeleton Mountain —
the bones of long-horned bison
wash down from the slopes,
YO
"""

NOT_HAIKU1 = """
s21d
d21
32
"""

NOT_HAIKU4 = """
"""

if __name__ == '__main__':
    print(is_haiku(HAIKU))
    print(is_haiku(NOT_HAIKU))
    print(is_haiku(NOT_HAIKU1))
    print(is_haiku(NOT_HAIKU2))
    print(is_haiku(NOT_HAIKU3))
    print(is_haiku(NOT_HAIKU4))
