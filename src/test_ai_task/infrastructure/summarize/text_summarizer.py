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
            text.to_raw(),
            max_length=200,
            min_length=10,
            do_sample=False
        )

        return SummarizedText(value=result[0]["summary_text"])
