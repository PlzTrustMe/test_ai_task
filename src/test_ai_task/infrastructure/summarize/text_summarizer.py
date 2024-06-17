from transformers import pipeline

from test_ai_task.domain.common.services.text_summarizer import TextSummarizer
from test_ai_task.domain.value_objects.summarized_text import SummarizedText
from test_ai_task.domain.value_objects.text_input import TextInput


class HuggingFaceTextSummarizer(TextSummarizer):
    def summarize_text(self, text: TextInput) -> SummarizedText:
        summarizer = pipeline(
            task="summarization",
            model="facebook/bart-large-cnn"
        )

        result = summarizer(
            text,
            max_length=130,
            min_length=30,
            do_sample=False
        )

        return SummarizedText(value=result[0]["summary_text"])
