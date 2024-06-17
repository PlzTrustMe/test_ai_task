from dishka import (
    Provider,
    Scope,
    AsyncContainer,
    make_async_container
)

from test_ai_task.application.summarize_text import SummarizeText
from test_ai_task.domain.common.services.text_summarizer import TextSummarizer
from test_ai_task.infrastructure.summarize.text_summarizer import (
    HuggingFaceTextSummarizer
)


def service_provider() -> Provider:
    provider = Provider()

    provider.provide(
        HuggingFaceTextSummarizer,
        scope=Scope.REQUEST,
        provides=TextSummarizer
    )

    return provider


def interactor_provider() -> Provider:
    provider = Provider()

    provider.provide(SummarizeText, scope=Scope.REQUEST)

    return provider


def setup_providers() -> list[Provider]:
    providers = [
        service_provider(),
        interactor_provider()
    ]

    return providers


def setup_http_di() -> AsyncContainer:
    providers = setup_providers()

    container = make_async_container(*providers)

    return container
