from typing import List
from ..schemas import ReviewRequestModel, \
    ReviewResponseModel, \
    ReviewRequestPutModel
from fastapi import APIRouter, Depends, Path
from ..helpers import oauth_schema
from ..models import User
from ..helpers import get_current_user
from ..services import ReviewService

router = APIRouter(
    prefix='/reviews',
    tags=["reviews"],
    dependencies=[Depends(oauth_schema)]
)


@router.post("", response_model=ReviewResponseModel)
async def create_review(review: ReviewRequestModel, user: User = Depends(get_current_user))\
        -> ReviewResponseModel:
    review_created = ReviewService.create_review(review, user)
    return review_created


@router.get("", response_model=List[ReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10)\
        -> List[ReviewResponseModel]:
    reviews = ReviewService.get_reviews(page, limit)
    return [review for review in reviews]


@router.get("/{review_id}", response_model=ReviewResponseModel)
def get_review(review_id: int = Path(ge=1)) -> ReviewResponseModel:
    review = ReviewService.get_review(review_id)
    return review


@router.put("/{review_id}", response_model=ReviewResponseModel)
async def update_review(review_request: ReviewRequestPutModel, review_id: int = Path(ge=1))\
        -> ReviewResponseModel:
    review_updated = ReviewService.update_review(review_request, review_id)
    return review_updated


@router.delete("/{review_id}", response_model=ReviewResponseModel)
def delete_review(review_id: int = Path(ge=1)) -> ReviewResponseModel:
    review_deleted = ReviewService.delete_review(review_id)
    return review_deleted
