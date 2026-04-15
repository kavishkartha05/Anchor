from __future__ import annotations

import copy

from anchor.memory import MemoryStore


class ScriptedModel:
    def __init__(self, responses: list[str]) -> None:
        self.responses = list(responses)
        self.calls: list[list[dict]] = []

    def __call__(self, messages: list[dict]) -> str:
        self.calls.append(copy.deepcopy(messages))
        if not self.responses:
            raise AssertionError("No scripted model responses left.")

        return self.responses.pop(0)


def scripted_model(*responses: str) -> ScriptedModel:
    return ScriptedModel(list(responses))


def deterministic_embedding(text: str) -> list[float]:
    counts = [0.0] * 27
    for char in text.lower():
        if "a" <= char <= "z":
            counts[ord(char) - ord("a")] += 1.0
        elif char.isdigit():
            counts[26] += float(ord(char) - ord("0"))

    total = sum(counts) or 1.0
    return [value / total for value in counts]


class FakeMemoryStore(MemoryStore):
    def __init__(
        self,
        *,
        query_results: list[list[dict]] | None = None,
        get_results: dict[str, dict | None] | None = None,
        allow_fallback_query: bool = False,
    ) -> None:
        self.items: dict[str, dict] = {}
        self.query_results = list(query_results or [])
        self.get_results = dict(get_results or {})
        self.allow_fallback_query = allow_fallback_query

    def queue_query_result(self, results: list[dict]) -> None:
        self.query_results.append(copy.deepcopy(results))

    def add(self, id: str, text: str, embedding: list[float], metadata: dict) -> None:
        self.items[id] = {
            "id": id,
            "content": text,
            "embedding": list(embedding),
            "metadata": dict(metadata),
        }

    def query(self, embedding: list[float], top_k: int = 5) -> list[dict]:
        if self.query_results:
            return copy.deepcopy(self.query_results.pop(0))[:top_k]

        if not self.allow_fallback_query:
            raise AssertionError("No fake memory query result queued.")

        return [
            {
                "id": item["id"],
                "content": item["content"],
                "metadata": dict(item["metadata"]),
                "source": item["metadata"].get("source", "unknown"),
                "score": 1.0,
            }
            for item in list(self.items.values())[:top_k]
        ]

    def delete(self, id: str) -> None:
        self.items.pop(id, None)
        self.get_results.pop(id, None)

    def get(self, id: str) -> dict | None:
        if id in self.get_results:
            return copy.deepcopy(self.get_results[id])

        item = self.items.get(id)
        if item is None:
            return None

        return {
            "id": item["id"],
            "content": item["content"],
            "metadata": dict(item["metadata"]),
        }
