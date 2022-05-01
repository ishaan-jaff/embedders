from typing import List, Union, Generator
from sentence_transformers import SentenceTransformer
from embedders import util
from embedders.classification import SentenceEmbedder
from spacy.tokens.doc import Doc


class TransformerSentenceEmbedder(SentenceEmbedder):
    def __init__(self, config_string: str, batch_size: int = 128):
        super().__init__(batch_size)
        self.model = SentenceTransformer(config_string)

    def _encode(
        self, documents: List[Union[str, Doc]], fit_model: bool
    ) -> Generator[List[List[float]], None, None]:
        for documents_batch in util.batch(documents, self.batch_size):
            yield self.model.encode(documents_batch, show_progress_bar=False).tolist()
