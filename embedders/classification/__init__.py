from embedders import Embedder


class SentenceEmbedder(Embedder):
    def __init__(self, batch_size=128):
        self.batch_size = batch_size
