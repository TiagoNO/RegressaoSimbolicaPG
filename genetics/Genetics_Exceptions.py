

class EmptyPopulation( Exception ):
    def __str__(self):
        print "Empty population in the genetic process..."

class NoValidationFile( Exception ):
    def __str__(self):
        print "No validation data file passed..."