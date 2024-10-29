class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = [*file_name]
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        list_ = []
        points = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for point in points:
                        if point in line:
                            line = line.replace(point, ' ')
                    split_line = line.split(sep=' ')
                    list_.append(split_line)
        list_new = [x for y in list_ for x in y]
        all_words[self.file_name] = list_new
        return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        list_ = []
        for name, words in dict_.items():
            for w in words:
                if word.lower() in w:
                    index = words.index(w)
                    list_.append(self.file_name)
                    list_.append(index+1)
                    break
        return list_

    def count(self, word):
        dict_ = self.get_all_words()
        list_count = []
        count = 0
        for name, words in dict_.items():
            for i in words:
                if word.lower() in i:
                    count += 1
        list_count.append(self.file_name)
        list_count.append(count)
        return list_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))