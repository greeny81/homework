import string
import re



class WordsFinder:
    file_names = []
    def __init__(self, *args):
        for f_name in args:
            self.file_names.append(f_name)

    def get_all_words(self):
        repl = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for name in self.file_names:
            all_words= {}
            with open(name, encoding='UTF-8') as file:
                tmp = []
                for l in file:
                    line=l.lower()
                    for sym in repl:
                        if sym in line:
                            line = line.replace(sym, "")
                    for word in line.split(): #line = re.split(" |\n", line)
                        tmp.append(word)
                all_words[name] = tmp
        return (all_words)

    def find(self, word):
        w_pos = {}
        for key, value in self.get_all_words().items():
            a = 1
            for wrd in value:
                if wrd == word.lower():
                    w_pos[key] = a
                    break
                a += 1

        return w_pos

    def count(self, word):
        cnt = {}
        for key, value in self.get_all_words().items():
            count = 0
            for wrd in value:
                if wrd == word.lower():
                    count += 1
                cnt[key] = count
        return cnt

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))