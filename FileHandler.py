class FileHandler:
    __dico_spec = {
        'à': 'a',
        'â': 'a',
        'ä': 'a',
        'ô': 'o',
        'î': 'i',
        'ê': 'e',
        'é': 'e',
        'è': 'e',
        'ë': 'e'
    }

    def __init__(self, file_name):
        self.file_name = file_name

    def get_words(self):
        file = open(self.file_name, 'r', encoding='latin1')
        lines = [line.strip() for line in file.readlines()]
        words = ','.join(lines)
        for k, v in self.__dico_spec.items():
            words = words.replace(k,v)
        lines = words.split(',')
        file.close()
        return lines