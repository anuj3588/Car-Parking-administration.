import os
from enum import Enum

BASE_DIR = os.path.abspath(os.path.dirname(""))


class BaseEnum(Enum):
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def tuple(cls):
        return tuple(map(lambda c: c.value, cls))


class ParkingSpotStatus(BaseEnum):
    ACTIVE = "ACTIVE"
    DEACTIVE = "DEACTIVE"
    MAINTENANCE = "MAINTENANCE"


class SpotReservationStatus(BaseEnum):
    RESERVED = "RESERVED"
    VACANT = "VACANT"
    PARKED = "PARKED"


class DateFormat(BaseEnum):
    DATETIMEFORMAT = "%Y-%m-%d %H:%M:%S"
