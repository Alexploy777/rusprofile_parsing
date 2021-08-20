from random import randint, choice
import pyperclip


class Phonegenerator:

    def random_pref(self):
        prefix_beeline = [900, 902, 903, 904, 905, 906, 908, 909, 950, 951, 953, 960, 961, 962, 963, 964, 965, 966, 967,
                          968, 969, 980, 983, 986]
        prefix_mts = [901, 902, 904, 908, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 950, 978, 980, 981, 982,
                      983,
                      984, 985, 986, 987, 988, 989]
        prefix_megafon = [902, 904, 908, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 936,
                          937, 938, 939, 950, 951, 999]
        prefix = prefix_beeline + prefix_mts + prefix_megafon

        return choice(prefix)

    def random_num(self):
        return ''.join([str(randint(0, 9)) for i in range(7)])

    def get_num(self, flag_coda=False):
        # flag_coda = Phonegenerator.flag_coda
        if flag_coda:
            return f'+7{self.random_pref()}{self.random_num()}'
        else:
            return f'{self.random_pref()}{self.random_num()}'


def main():
    flag_coda = True
    pg = Phonegenerator()
    res = pg.get_num()
    print(res)

    pyperclip.copy(res)
    # pyperclip.paste()


if __name__ == '__main__':
    main()
