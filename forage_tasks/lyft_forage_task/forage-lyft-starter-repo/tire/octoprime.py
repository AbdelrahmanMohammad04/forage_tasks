from tire.tire import tire

class Octoprime(tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        sum = 0
        for x in self.wear:
            sum+=x
        return sum >= 3