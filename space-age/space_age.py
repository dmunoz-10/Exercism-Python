class SpaceAge:
    EARTH_ORBITAL_PERIOD = 31_557_600

    def __init__(self, seconds):
        self.seconds = float(seconds)

    def on_earth(self):
        return round(self.seconds / EARTH_ORBITAL_PERIOD, 2)

    def on_mercury(self):
        return round(self.seconds / (EARTH_ORBITAL_PERIOD * 0.2408467), 2)

    def on_venus(self):
        return round(self.seconds / (EARTH_ORBITAL_PERIOD * 0.61519726), 2)

    def on_mars(self):
        return round(self.seconds / (EARTH_ORBITAL_PERIOD * 1.8808158), 2)

    def on_jupiter(self):
        return round(self.seconds / (EARTH_ORBITAL_PERIOD * 11.862615), 2)

    def on_saturn(self):
        return round(self.seconds / (EARTH_ORBITAL_PERIOD * 29.447498), 2)

    def on_uranus(self):
        return round(self.seconds / (EARTH_ORBITAL_PERIOD * 84.016846), 2)

    def on_neptune(self):
        return round(self.seconds / (EARTH_ORBITAL_PERIOD * 164.79132), 2)
