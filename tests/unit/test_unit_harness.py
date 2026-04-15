from __future__ import annotations

from anchor.ingestor import Ingestor
from anchor.retriever import Retriever
from tests.unit_harness import FakeMemoryStore, deterministic_embedding, scripted_model


def test_unit_harness_supports_offline_ingest_and_retrieval() -> None:
    store = FakeMemoryStore()
    ingestor = Ingestor(
        store,
        deterministic_embedding,
        question_fn=scripted_model("alpha?\nbeta?"),
    )

    chunk_id = ingestor.ingest("alpha project notes", source="docs")
    store.queue_query_result(
        [
            {
                "id": chunk_id,
                "content": "alpha project notes",
                "metadata": {"source": "docs", "questions": "alpha?\nbeta?"},
                "source": "docs",
                "score": 1.0,
            }
        ]
    )

    record = store.get(chunk_id)
    assert record is not None
    assert record["id"] == chunk_id
    assert record["content"] == "alpha project notes"
    assert record["metadata"]["source"] == "docs"
    assert record["metadata"]["questions"] == "alpha?\nbeta?"
    assert "timestamp" in record["metadata"]

    retriever = Retriever(store, deterministic_embedding)
    assert retriever.retrieve("alpha", top_k=1) == [
        {
            "id": chunk_id,
            "content": "alpha project notes",
            "metadata": {"source": "docs", "questions": "alpha?\nbeta?"},
            "source": "docs",
            "score": 1.0,
        }
    ]
