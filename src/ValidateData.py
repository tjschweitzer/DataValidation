import pandas as pd
import sqlalchemy
class ValidateData:
    OracleEngine = None
    def __init__(self):
        pass

    def BuildEngine(self, username, password):
        """

        :param username:
        :param password:
        :return:
        """
        sqlalchemy.create_engine("")

    def row_validator(self, row):
        pass

    def lat_validation(self, lat: str) -> bool:
        """
        Latitude validation:
            Not Null
            +/- 90 Inclusive
        :param lat: string latitude value
        :return:
        :rtype: bool
        """
        if not lat:
            return False
        lat_float = float(lat)
        return -90 <= lat_float <= 90

    def lon_validation(self, lon: str) -> bool:
        """
        Longitude validation:
        Not Null
        -180/ 179.99999
        :param lon: string longitude value
        :return:
        :rtype: bool
        """
        if not lon:
            return False
        lon_float = float(lon)
        return -180 <= lon_float <= 179.99999

    def wind_speed_validation(self, wind_speed: str) -> bool:
        """
        Windspeed validation:
         Null
          >=0
        :param wind_speed:
        :return:
        """
        if not wind_speed:
            return True
        wind_speed_float = float(wind_speed)
        return wind_speed_float >= 0