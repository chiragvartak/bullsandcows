def bulls(original, guess):
    pairs = zip(original, guess)
    bullCount = 0
    for x,y in pairs:
        if x.lower() == y.lower():
            bullCount += 1
    return bullCount

def cows(original, guess):
    original_set = set()
    covered_set = set()
    cowCount = 0
    for letter in original:
        original_set.add(letter.lower())
    for letter in guess:
        if letter.lower() in original_set and letter.lower() not in covered_set:
            cowCount += 1
            covered_set.add(letter.lower())
    return cowCount

if __name__ == "__main__":
    assert bulls("abc", "abc") is 3
    assert bulls("charm", "chasm") is 4
    assert bulls("red", "yellow") is 1
    assert bulls("violet", "mauve") is 1

    assert cows("abc", "abc") is 3
    assert cows("charm", "chasm") is 4
    assert cows("red", "yellow") is 1
    assert cows("violet", "mauve") is 2
    assert cows("keen", "blue") is 1