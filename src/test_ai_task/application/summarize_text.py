from dataclasses import dataclass

from test_ai_task.application.common.interactor import Interactor
from test_ai_task.domain.common.services.text_summarizer import TextSummarizer
from test_ai_task.domain.value_objects.summarized_text import SummarizedText
from test_ai_task.domain.value_objects.text_input import TextInput


@dataclass(frozen=True)
class TextInputDTO:
    text: str


@dataclass(frozen=True)
class TextOutputDTO:
    text: str


class SummarizeText(Interactor[TextInputDTO, TextOutputDTO]):
    def __init__(self, text_summarizer: TextSummarizer):
        self.text_summarizer = text_summarizer

    def __call__(self, data: TextInputDTO) -> TextOutputDTO:
        text_to_summarize = TextInput(data.text)

        summarized_text = self.text_summarizer.summarize_text(
            text_to_summarize
        )

        text_dto = TextOutputDTO(text=summarized_text.to_raw())

        return text_dto
