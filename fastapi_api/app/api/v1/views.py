from fastapi import APIRouter
from serializers.serializers import CarSerializer

router = APIRouter()


@router.post("/create/car", tags=["API"])
def root(car: CarSerializer):
    """
    Root of host
    """
    return car
