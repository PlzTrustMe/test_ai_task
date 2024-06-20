from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from transformers import pipeline

from test_ai_task.domain.common.services.text_summarizer import TextSummarizer
from test_ai_task.domain.value_objects.summarized_text import SummarizedText
from test_ai_task.domain.value_objects.text_input import TextInput
from langchain_huggingface import HuggingFacePipeline


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


class LangChainTextSummarizer(TextSummarizer):
    def summarize_text(self, text: TextInput) -> SummarizedText:
        summarization_pipeline = pipeline(
            task="summarization",
            model="facebook/bart-large-cnn"
        )

        llm = HuggingFacePipeline(pipeline=summarization_pipeline)

        summarize_prompt = PromptTemplate(
            input_variables=["text"],
            template="{text}"
        )

        summarize_chain = LLMChain(llm=llm, prompt=summarize_prompt)

        summary = summarize_chain.run(text=text.to_raw())

        return SummarizedText(value=summary)
