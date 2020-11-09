class Allergies:
    ALLERGENS = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                 'tomatoes', 'chocolate', 'pollen', 'cats']

    def __init__(self, score):
        allergies = list("{0:b}".format(score)[::-1][:len(self.ALLERGENS)])
        self._lst = []
        for index, number in enumerate(allergies):
            if number == '1':
                self._lst.append(self.ALLERGENS[index])

    def allergic_to(self, item):
        return item in self._lst

    @property
    def lst(self):
        return self._lst
