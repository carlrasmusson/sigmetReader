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

        # Get phenomenon
        rawPhenomenon = spiltText[((spiltText.index('FIR')) + 1)] + ' ' + spiltText[((spiltText.index('FIR')) + 2)]

        # Get observed or Forcasted
        if spiltText[((spiltText.index('FIR')) + 3)] == 'OBS':
            self.nowOrThen = 'OBS'
            if spiltText[((spiltText.index('OBS')) + 1)] == 'AT':
                self.nowOrThen += f' AT {spiltText[((spiltText.index('AT')) + 1)]}'

        elif spiltText[((spiltText.index('FIR')) + 3)] == 'FCST':
            self.nowOrThen = 'FCST'


        print(self.nowOrThen)
        print(spiltText)

