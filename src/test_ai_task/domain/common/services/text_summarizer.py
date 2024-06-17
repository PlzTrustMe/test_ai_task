from abc import abstractmethod
from asyncio import Protocol

from test_ai_task.domain.value_objects.summarized_text import SummarizedText
from test_ai_task.domain.value_objects.text_input import TextInput


class TextSummarizer(Protocol):
    @abstractmethod
    def summarize_text(self, text: TextInput) -> SummarizedText:
        ...
