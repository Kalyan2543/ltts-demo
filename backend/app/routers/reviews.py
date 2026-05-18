from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import ReviewResponse
from .. import crud

router = APIRouter(prefix="/api/v1/reviews", tags=["reviews"])


@router.get("", response_model=list[ReviewResponse])
def list_reviews(product_id: int = Query(...), db: Session = Depends(get_db)):
    return crud.get_reviews(db, product_id)
