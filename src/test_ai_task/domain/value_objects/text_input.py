from test_ai_task.domain.common.vo import ValueObject


class TextInput(ValueObject[str]):
    value: str
