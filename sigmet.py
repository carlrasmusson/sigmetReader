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
        # Get validity time (Format: DDHHMM)
        rawValidityPeriod = spiltText[((spiltText.index('VALID'))+1)]
        self.validFrom = rawValidityPeriod.split('/')[0]
        self.validTo = rawValidityPeriod.split('/')[-1]

        #Get sigmet number and ident
        self.id = spiltText[((spiltText.index('SIGMET'))-1)].split('\n')[1] + ' SIGMET ' + spiltText[((spiltText.index('SIGMET'))+1)]

        # Handle CNL Sigmet
        if spiltText[((spiltText.index('FIR')) + 1)] == 'CNL':
            self.phenomenon = 'CNL'

            return

        # Get phenomenon
        self.phenomenon = spiltText[((spiltText.index('FIR')) + 1)] + ' ' + spiltText[((spiltText.index('FIR')) + 2)]

        # Get observed or Forcasted
        if spiltText[((spiltText.index('FIR')) + 3)] == 'OBS':
            self.nowOrThen = 'OBS'
            if spiltText[((spiltText.index('OBS')) + 1)] == 'AT':
                self.nowOrThen += f' AT {spiltText[((spiltText.index('AT')) + 1)]}'

        elif spiltText[((spiltText.index('FIR')) + 3)] == 'FCST':
            self.nowOrThen = 'FCST'

        print(self.id)
        print(self.phenomenon)
        print(self.nowOrThen + '\n')



