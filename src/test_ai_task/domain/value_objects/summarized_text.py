from test_ai_task.domain.common.vo import ValueObject


class SummarizedText(ValueObject[str]):
    value: str
