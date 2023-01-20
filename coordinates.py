# import dataclasses as dataclasses


# @dataclasses(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


# @dataclasses(slots=True, frozen=True)
class CoordinatesR:
    latitude: float = 47.2213858
    longitude: float = 39.7114196


# @dataclasses(slots=True, frozen=True)
class CoordinatesN:
    latitude: float = 55.0415 #54.96781445
    longitude: float = 82.9346#82.95159894278376


# @dataclasses(slots=True, frozen=True)
class CoordinatesP:
    latitude: float = 59.9386 #59.938732
    longitude: float = 30.3141 #30.316229
