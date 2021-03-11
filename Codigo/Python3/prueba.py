from decorator import Structure

class pifia(Structure):

    def tempo(self):
        self.scale = 100
        print(dir(self))
    _fields = [
        'lo',
        ('supp', 0.01),  # This is the support, we set to the minimum
        ('datasetfilename', ""),  # The name of the file
        ('U', set()),  # The universe
        ('scale', 100000), #This is the scale
        ('v', None),  # The verbosity
    ]
