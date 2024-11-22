from mod1_packets import hello


def good_word(name):
    hello(name)
    print("Best :", name)

if __name__ == '__main__':
    good_word('URBAN')