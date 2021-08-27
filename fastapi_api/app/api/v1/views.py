from fastapi import APIRouter
from serializers.serializers import CarSerializer
from core.handler import CarHandler

router = APIRouter()


@router.post("/car/create", tags=["API"])
def create_car(car: CarSerializer):
    output = CarHandler.save_car(car)
    return output


@router.get("/car/consult", tags=["API"])
def get_car():
    return True
# TODO Serializador del path, del query, del response
