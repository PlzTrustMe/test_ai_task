from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from test_ai_task.application.summarize_text import SummarizeText, \
    TextOutputDTO, TextInputDTO
from test_ai_task.presentation.schemas.text import TextToSummarizeSchema

router = APIRouter(
    prefix="/text",
    tags=["Text"],
    responses={404: {"description": "Not found"}},
    route_class=DishkaRoute
)


@router.post("/summarize")
async def summarize_text(
        data: TextToSummarizeSchema,
        action: FromDishka[SummarizeText]
) -> TextOutputDTO:
    response = action(
        TextInputDTO(text=data.text)
    )

    return response
