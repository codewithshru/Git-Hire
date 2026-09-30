"""Standard pagination primitives used by all list endpoints."""

from typing import Generic, TypeVar

from fastapi import Query
from pydantic import BaseModel

T = TypeVar("T")


class Page(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    size: int


class PaginationParams:
    """FastAPI dependency: `page: PaginationParams = Depends()`."""

    def __init__(
        self,
        page: int = 1,
        size: int = Query(default=20, le=100, ge=1),
    ) -> None:
        self.page = page
        self.size = size
