class Response:

    def __init__(self, meta, data):
        self.metadata = meta
        self.data = data

    def serlialize(self):
        return {
            "meta": self.metadata.serialize(),
            "data": [data_object.serialize() for data_object in self.data]
        }
