import random


def primary():
    # print("Keep it logically awesome.")
    rnd = random.randint(0, 13)
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[rnd])


if __name__ == "__main__":
    primary()
