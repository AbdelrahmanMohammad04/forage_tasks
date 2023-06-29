from tire.tire import tire

class Carrigan(tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        for x in self.wear:
            if x >= 0.9:
                return True
        return False

