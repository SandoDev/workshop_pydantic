from fastapi import APIRouter
from serializers.serializers import CarSerializer

router = APIRouter()


@router.post("/create/car", tags=["API"])
def create_car(car: CarSerializer):
    # TODO guardar en db
    return car

# TODO Serializador del path, del query, del response
