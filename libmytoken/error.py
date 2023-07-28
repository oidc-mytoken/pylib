class MytokenError(Exception):
    def __init__(self, err, errorDetails=""):
        self.err = err
        self.errorDetails = errorDetails

    def __str__(self):
        e = self.err
        if self.errorDetails != "":
            e += ": " + self.errorDetails
        return e
