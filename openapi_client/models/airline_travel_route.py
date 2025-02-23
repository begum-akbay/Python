# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 21.1.0.20210122.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AirlineTravelRoute(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'departure_date': 'date',
        'origin': 'str',
        'destination': 'str',
        'carrier_code': 'str',
        'service_class': 'str',
        'stopover_type': 'str',
        'fare_basis_code': 'str',
        'departure_tax': 'float',
        'flight_number': 'str'
    }

    attribute_map = {
        'departure_date': 'departureDate',
        'origin': 'origin',
        'destination': 'destination',
        'carrier_code': 'carrierCode',
        'service_class': 'serviceClass',
        'stopover_type': 'stopoverType',
        'fare_basis_code': 'fareBasisCode',
        'departure_tax': 'departureTax',
        'flight_number': 'flightNumber'
    }

    def __init__(self, departure_date=None, origin=None, destination=None, carrier_code=None, service_class=None, stopover_type=None, fare_basis_code=None, departure_tax=None, flight_number=None):  # noqa: E501
        """AirlineTravelRoute - a model defined in OpenAPI"""  # noqa: E501

        self._departure_date = None
        self._origin = None
        self._destination = None
        self._carrier_code = None
        self._service_class = None
        self._stopover_type = None
        self._fare_basis_code = None
        self._departure_tax = None
        self._flight_number = None
        self.discriminator = None

        if departure_date is not None:
            self.departure_date = departure_date
        if origin is not None:
            self.origin = origin
        if destination is not None:
            self.destination = destination
        if carrier_code is not None:
            self.carrier_code = carrier_code
        if service_class is not None:
            self.service_class = service_class
        if stopover_type is not None:
            self.stopover_type = stopover_type
        if fare_basis_code is not None:
            self.fare_basis_code = fare_basis_code
        if departure_tax is not None:
            self.departure_tax = departure_tax
        if flight_number is not None:
            self.flight_number = flight_number

    @property
    def departure_date(self):
        """Gets the departure_date of this AirlineTravelRoute.  # noqa: E501

        Date of departure.  # noqa: E501

        :return: The departure_date of this AirlineTravelRoute.  # noqa: E501
        :rtype: date
        """
        return self._departure_date

    @departure_date.setter
    def departure_date(self, departure_date):
        """Sets the departure_date of this AirlineTravelRoute.

        Date of departure.  # noqa: E501

        :param departure_date: The departure_date of this AirlineTravelRoute.  # noqa: E501
        :type: date
        """

        self._departure_date = departure_date

    @property
    def origin(self):
        """Gets the origin of this AirlineTravelRoute.  # noqa: E501

        The IATA code for the departure airport.  # noqa: E501

        :return: The origin of this AirlineTravelRoute.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this AirlineTravelRoute.

        The IATA code for the departure airport.  # noqa: E501

        :param origin: The origin of this AirlineTravelRoute.  # noqa: E501
        :type: str
        """
        if origin is not None and len(origin) > 3:
            raise ValueError("Invalid value for `origin`, length must be less than or equal to `3`")  # noqa: E501

        self._origin = origin

    @property
    def destination(self):
        """Gets the destination of this AirlineTravelRoute.  # noqa: E501

        The IATA code for the destination. airport.  # noqa: E501

        :return: The destination of this AirlineTravelRoute.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this AirlineTravelRoute.

        The IATA code for the destination. airport.  # noqa: E501

        :param destination: The destination of this AirlineTravelRoute.  # noqa: E501
        :type: str
        """
        if destination is not None and len(destination) > 3:
            raise ValueError("Invalid value for `destination`, length must be less than or equal to `3`")  # noqa: E501

        self._destination = destination

    @property
    def carrier_code(self):
        """Gets the carrier_code of this AirlineTravelRoute.  # noqa: E501

        The IATA code for the carrier.  # noqa: E501

        :return: The carrier_code of this AirlineTravelRoute.  # noqa: E501
        :rtype: str
        """
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, carrier_code):
        """Sets the carrier_code of this AirlineTravelRoute.

        The IATA code for the carrier.  # noqa: E501

        :param carrier_code: The carrier_code of this AirlineTravelRoute.  # noqa: E501
        :type: str
        """
        if carrier_code is not None and len(carrier_code) > 2:
            raise ValueError("Invalid value for `carrier_code`, length must be less than or equal to `2`")  # noqa: E501

        self._carrier_code = carrier_code

    @property
    def service_class(self):
        """Gets the service_class of this AirlineTravelRoute.  # noqa: E501

        The airline code for the service class of the ticket.  # noqa: E501

        :return: The service_class of this AirlineTravelRoute.  # noqa: E501
        :rtype: str
        """
        return self._service_class

    @service_class.setter
    def service_class(self, service_class):
        """Sets the service_class of this AirlineTravelRoute.

        The airline code for the service class of the ticket.  # noqa: E501

        :param service_class: The service_class of this AirlineTravelRoute.  # noqa: E501
        :type: str
        """
        if service_class is not None and len(service_class) > 1:
            raise ValueError("Invalid value for `service_class`, length must be less than or equal to `1`")  # noqa: E501

        self._service_class = service_class

    @property
    def stopover_type(self):
        """Gets the stopover_type of this AirlineTravelRoute.  # noqa: E501

        Indicates whether the route is direct.  # noqa: E501

        :return: The stopover_type of this AirlineTravelRoute.  # noqa: E501
        :rtype: str
        """
        return self._stopover_type

    @stopover_type.setter
    def stopover_type(self, stopover_type):
        """Sets the stopover_type of this AirlineTravelRoute.

        Indicates whether the route is direct.  # noqa: E501

        :param stopover_type: The stopover_type of this AirlineTravelRoute.  # noqa: E501
        :type: str
        """
        allowed_values = ["DIRECT", "STOPOVER"]  # noqa: E501
        if stopover_type not in allowed_values:
            raise ValueError(
                "Invalid value for `stopover_type` ({0}), must be one of {1}"  # noqa: E501
                .format(stopover_type, allowed_values)
            )

        self._stopover_type = stopover_type

    @property
    def fare_basis_code(self):
        """Gets the fare_basis_code of this AirlineTravelRoute.  # noqa: E501

        The airline fare basis code.  # noqa: E501

        :return: The fare_basis_code of this AirlineTravelRoute.  # noqa: E501
        :rtype: str
        """
        return self._fare_basis_code

    @fare_basis_code.setter
    def fare_basis_code(self, fare_basis_code):
        """Sets the fare_basis_code of this AirlineTravelRoute.

        The airline fare basis code.  # noqa: E501

        :param fare_basis_code: The fare_basis_code of this AirlineTravelRoute.  # noqa: E501
        :type: str
        """
        if fare_basis_code is not None and len(fare_basis_code) > 2:
            raise ValueError("Invalid value for `fare_basis_code`, length must be less than or equal to `2`")  # noqa: E501

        self._fare_basis_code = fare_basis_code

    @property
    def departure_tax(self):
        """Gets the departure_tax of this AirlineTravelRoute.  # noqa: E501

        Fee charged by a country when a person leaves the country.  # noqa: E501

        :return: The departure_tax of this AirlineTravelRoute.  # noqa: E501
        :rtype: float
        """
        return self._departure_tax

    @departure_tax.setter
    def departure_tax(self, departure_tax):
        """Sets the departure_tax of this AirlineTravelRoute.

        Fee charged by a country when a person leaves the country.  # noqa: E501

        :param departure_tax: The departure_tax of this AirlineTravelRoute.  # noqa: E501
        :type: float
        """
        if departure_tax is not None and departure_tax > 999999999999:  # noqa: E501
            raise ValueError("Invalid value for `departure_tax`, must be a value less than or equal to `999999999999`")  # noqa: E501

        self._departure_tax = departure_tax

    @property
    def flight_number(self):
        """Gets the flight_number of this AirlineTravelRoute.  # noqa: E501

        The airline flight number associated with the ticket.  # noqa: E501

        :return: The flight_number of this AirlineTravelRoute.  # noqa: E501
        :rtype: str
        """
        return self._flight_number

    @flight_number.setter
    def flight_number(self, flight_number):
        """Sets the flight_number of this AirlineTravelRoute.

        The airline flight number associated with the ticket.  # noqa: E501

        :param flight_number: The flight_number of this AirlineTravelRoute.  # noqa: E501
        :type: str
        """
        if flight_number is not None and len(flight_number) > 10:
            raise ValueError("Invalid value for `flight_number`, length must be less than or equal to `10`")  # noqa: E501

        self._flight_number = flight_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AirlineTravelRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
