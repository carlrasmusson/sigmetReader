class Sigmet:
    def __init__(self, text):
        # To stop from accepting sigmet not ending with = (Maybe change to throw Error)
        if text[-1] != '=':
            print('Invalid end to Sigmet. (Must end with "=")')
            return
        else:
            self.rawText = text

    def parse(self):
        spiltText = self.rawText.split(' ')
        print(spiltText)
