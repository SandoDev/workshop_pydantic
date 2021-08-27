from .process import CarProcess
from serializers.serializers import CarSerializer


class CarHandler:
    def save_car(car: CarSerializer):
        return CarProcess.save_car(car)
