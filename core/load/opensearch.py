from typing import List, Union, Optional, Dict, Any
from core.load.base import Loader

# TODO: Implement OpenSearch interface


class OpenSearchLoader(Loader):
    def __init__(self) -> None:
        pass

    def check_and_setup_index(
        self, index_name: str, field_name: str, num_dimensions: int
    ) -> None:
        pass

    def upsert_embedding(
        self,
        index_name: str,
        embedding: List[float],
        id: Union[str, int],
        field_name: str,
        metadata: Optional[Dict[str, Any]],
    ) -> None:
        pass

    def bulk_upsert_embeddings(
        self,
        index_name: str,
        embeddings: List[List[float]],
        ids: List[Union[str, int]],
        field_name: str,
        metadata: Optional[List[Dict[str, Any]]],
    ) -> None:
        pass