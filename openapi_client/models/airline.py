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


class Airline(object):
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
        'passenger_name': 'str',
        'ticket_number': 'str',
        'issuing_carrier': 'str',
        'carrier_name': 'str',
        'travel_agency_iata_code': 'str',
        'travel_agency_name': 'str',
        'airline_plan_number': 'str',
        'airline_invoice_number': 'str',
        'reservation_system': 'str',
        'restricted': 'bool',
        'travel_route': 'list[AirlineTravelRoute]',
        'related_ticket_number': 'str',
        'ancillary_service_category': 'list[AirlineAncillaryServiceCategory]',
        'ticket_purchase': 'bool'
    }

    attribute_map = {
        'passenger_name': 'passengerName',
        'ticket_number': 'ticketNumber',
        'issuing_carrier': 'issuingCarrier',
        'carrier_name': 'carrierName',
        'travel_agency_iata_code': 'travelAgencyIataCode',
        'travel_agency_name': 'travelAgencyName',
        'airline_plan_number': 'airlinePlanNumber',
        'airline_invoice_number': 'airlineInvoiceNumber',
        'reservation_system': 'reservationSystem',
        'restricted': 'restricted',
        'travel_route': 'travelRoute',
        'related_ticket_number': 'relatedTicketNumber',
        'ancillary_service_category': 'ancillaryServiceCategory',
        'ticket_purchase': 'ticketPurchase'
    }

    def __init__(self, passenger_name=None, ticket_number=None, issuing_carrier=None, carrier_name=None, travel_agency_iata_code=None, travel_agency_name=None, airline_plan_number=None, airline_invoice_number=None, reservation_system=None, restricted=None, travel_route=None, related_ticket_number=None, ancillary_service_category=None, ticket_purchase=None):  # noqa: E501
        """Airline - a model defined in OpenAPI"""  # noqa: E501

        self._passenger_name = None
        self._ticket_number = None
        self._issuing_carrier = None
        self._carrier_name = None
        self._travel_agency_iata_code = None
        self._travel_agency_name = None
        self._airline_plan_number = None
        self._airline_invoice_number = None
        self._reservation_system = None
        self._restricted = None
        self._travel_route = None
        self._related_ticket_number = None
        self._ancillary_service_category = None
        self._ticket_purchase = None
        self.discriminator = None

        if passenger_name is not None:
            self.passenger_name = passenger_name
        if ticket_number is not None:
            self.ticket_number = ticket_number
        if issuing_carrier is not None:
            self.issuing_carrier = issuing_carrier
        if carrier_name is not None:
            self.carrier_name = carrier_name
        if travel_agency_iata_code is not None:
            self.travel_agency_iata_code = travel_agency_iata_code
        if travel_agency_name is not None:
            self.travel_agency_name = travel_agency_name
        if airline_plan_number is not None:
            self.airline_plan_number = airline_plan_number
        if airline_invoice_number is not None:
            self.airline_invoice_number = airline_invoice_number
        if reservation_system is not None:
            self.reservation_system = reservation_system
        if restricted is not None:
            self.restricted = restricted
        if travel_route is not None:
            self.travel_route = travel_route
        if related_ticket_number is not None:
            self.related_ticket_number = related_ticket_number
        if ancillary_service_category is not None:
            self.ancillary_service_category = ancillary_service_category
        if ticket_purchase is not None:
            self.ticket_purchase = ticket_purchase

    @property
    def passenger_name(self):
        """Gets the passenger_name of this Airline.  # noqa: E501

        The passenger name associated with the transaction.  # noqa: E501

        :return: The passenger_name of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, passenger_name):
        """Sets the passenger_name of this Airline.

        The passenger name associated with the transaction.  # noqa: E501

        :param passenger_name: The passenger_name of this Airline.  # noqa: E501
        :type: str
        """
        if passenger_name is not None and len(passenger_name) > 30:
            raise ValueError("Invalid value for `passenger_name`, length must be less than or equal to `30`")  # noqa: E501

        self._passenger_name = passenger_name

    @property
    def ticket_number(self):
        """Gets the ticket_number of this Airline.  # noqa: E501

        The airline ticket number associated with the transaction.  # noqa: E501

        :return: The ticket_number of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._ticket_number

    @ticket_number.setter
    def ticket_number(self, ticket_number):
        """Sets the ticket_number of this Airline.

        The airline ticket number associated with the transaction.  # noqa: E501

        :param ticket_number: The ticket_number of this Airline.  # noqa: E501
        :type: str
        """
        if ticket_number is not None and len(ticket_number) > 20:
            raise ValueError("Invalid value for `ticket_number`, length must be less than or equal to `20`")  # noqa: E501

        self._ticket_number = ticket_number

    @property
    def issuing_carrier(self):
        """Gets the issuing_carrier of this Airline.  # noqa: E501

        The carrier that issued the ticket.  # noqa: E501

        :return: The issuing_carrier of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._issuing_carrier

    @issuing_carrier.setter
    def issuing_carrier(self, issuing_carrier):
        """Sets the issuing_carrier of this Airline.

        The carrier that issued the ticket.  # noqa: E501

        :param issuing_carrier: The issuing_carrier of this Airline.  # noqa: E501
        :type: str
        """
        if issuing_carrier is not None and len(issuing_carrier) > 20:
            raise ValueError("Invalid value for `issuing_carrier`, length must be less than or equal to `20`")  # noqa: E501

        self._issuing_carrier = issuing_carrier

    @property
    def carrier_name(self):
        """Gets the carrier_name of this Airline.  # noqa: E501

        The carrier associated with the transaction.  # noqa: E501

        :return: The carrier_name of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this Airline.

        The carrier associated with the transaction.  # noqa: E501

        :param carrier_name: The carrier_name of this Airline.  # noqa: E501
        :type: str
        """
        if carrier_name is not None and len(carrier_name) > 20:
            raise ValueError("Invalid value for `carrier_name`, length must be less than or equal to `20`")  # noqa: E501

        self._carrier_name = carrier_name

    @property
    def travel_agency_iata_code(self):
        """Gets the travel_agency_iata_code of this Airline.  # noqa: E501

        The IATA code associated with the travel agency.  # noqa: E501

        :return: The travel_agency_iata_code of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._travel_agency_iata_code

    @travel_agency_iata_code.setter
    def travel_agency_iata_code(self, travel_agency_iata_code):
        """Sets the travel_agency_iata_code of this Airline.

        The IATA code associated with the travel agency.  # noqa: E501

        :param travel_agency_iata_code: The travel_agency_iata_code of this Airline.  # noqa: E501
        :type: str
        """
        if travel_agency_iata_code is not None and len(travel_agency_iata_code) > 20:
            raise ValueError("Invalid value for `travel_agency_iata_code`, length must be less than or equal to `20`")  # noqa: E501

        self._travel_agency_iata_code = travel_agency_iata_code

    @property
    def travel_agency_name(self):
        """Gets the travel_agency_name of this Airline.  # noqa: E501

        The business name of the travel agency.  # noqa: E501

        :return: The travel_agency_name of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._travel_agency_name

    @travel_agency_name.setter
    def travel_agency_name(self, travel_agency_name):
        """Sets the travel_agency_name of this Airline.

        The business name of the travel agency.  # noqa: E501

        :param travel_agency_name: The travel_agency_name of this Airline.  # noqa: E501
        :type: str
        """
        if travel_agency_name is not None and len(travel_agency_name) > 30:
            raise ValueError("Invalid value for `travel_agency_name`, length must be less than or equal to `30`")  # noqa: E501

        self._travel_agency_name = travel_agency_name

    @property
    def airline_plan_number(self):
        """Gets the airline_plan_number of this Airline.  # noqa: E501

        The airline plan number associated with the transaction.  # noqa: E501

        :return: The airline_plan_number of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._airline_plan_number

    @airline_plan_number.setter
    def airline_plan_number(self, airline_plan_number):
        """Sets the airline_plan_number of this Airline.

        The airline plan number associated with the transaction.  # noqa: E501

        :param airline_plan_number: The airline_plan_number of this Airline.  # noqa: E501
        :type: str
        """
        if airline_plan_number is not None and len(airline_plan_number) > 2:
            raise ValueError("Invalid value for `airline_plan_number`, length must be less than or equal to `2`")  # noqa: E501

        self._airline_plan_number = airline_plan_number

    @property
    def airline_invoice_number(self):
        """Gets the airline_invoice_number of this Airline.  # noqa: E501

        The invoice number used by the airline.  # noqa: E501

        :return: The airline_invoice_number of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._airline_invoice_number

    @airline_invoice_number.setter
    def airline_invoice_number(self, airline_invoice_number):
        """Sets the airline_invoice_number of this Airline.

        The invoice number used by the airline.  # noqa: E501

        :param airline_invoice_number: The airline_invoice_number of this Airline.  # noqa: E501
        :type: str
        """
        if airline_invoice_number is not None and len(airline_invoice_number) > 6:
            raise ValueError("Invalid value for `airline_invoice_number`, length must be less than or equal to `6`")  # noqa: E501

        self._airline_invoice_number = airline_invoice_number

    @property
    def reservation_system(self):
        """Gets the reservation_system of this Airline.  # noqa: E501

        The reservation system used to create the ticket.  # noqa: E501

        :return: The reservation_system of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._reservation_system

    @reservation_system.setter
    def reservation_system(self, reservation_system):
        """Sets the reservation_system of this Airline.

        The reservation system used to create the ticket.  # noqa: E501

        :param reservation_system: The reservation_system of this Airline.  # noqa: E501
        :type: str
        """
        allowed_values = ["START", "TWA", "DELTA", "SABRE", "COVIA_APOLLO", "DR_BLANK", "DER", "TUI"]  # noqa: E501
        if reservation_system not in allowed_values:
            raise ValueError(
                "Invalid value for `reservation_system` ({0}), must be one of {1}"  # noqa: E501
                .format(reservation_system, allowed_values)
            )

        self._reservation_system = reservation_system

    @property
    def restricted(self):
        """Gets the restricted of this Airline.  # noqa: E501

        If the transaction is associated with a restricted class fare.  # noqa: E501

        :return: The restricted of this Airline.  # noqa: E501
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """Sets the restricted of this Airline.

        If the transaction is associated with a restricted class fare.  # noqa: E501

        :param restricted: The restricted of this Airline.  # noqa: E501
        :type: bool
        """

        self._restricted = restricted

    @property
    def travel_route(self):
        """Gets the travel_route of this Airline.  # noqa: E501

        Array containing up to 4 items that describe the route associated with the transaction.  # noqa: E501

        :return: The travel_route of this Airline.  # noqa: E501
        :rtype: list[AirlineTravelRoute]
        """
        return self._travel_route

    @travel_route.setter
    def travel_route(self, travel_route):
        """Sets the travel_route of this Airline.

        Array containing up to 4 items that describe the route associated with the transaction.  # noqa: E501

        :param travel_route: The travel_route of this Airline.  # noqa: E501
        :type: list[AirlineTravelRoute]
        """

        self._travel_route = travel_route

    @property
    def related_ticket_number(self):
        """Gets the related_ticket_number of this Airline.  # noqa: E501

        The number of any other tickets associated with the transaction ticket.  # noqa: E501

        :return: The related_ticket_number of this Airline.  # noqa: E501
        :rtype: str
        """
        return self._related_ticket_number

    @related_ticket_number.setter
    def related_ticket_number(self, related_ticket_number):
        """Sets the related_ticket_number of this Airline.

        The number of any other tickets associated with the transaction ticket.  # noqa: E501

        :param related_ticket_number: The related_ticket_number of this Airline.  # noqa: E501
        :type: str
        """
        if related_ticket_number is not None and len(related_ticket_number) > 20:
            raise ValueError("Invalid value for `related_ticket_number`, length must be less than or equal to `20`")  # noqa: E501

        self._related_ticket_number = related_ticket_number

    @property
    def ancillary_service_category(self):
        """Gets the ancillary_service_category of this Airline.  # noqa: E501

        Identify the purchase of ancillary goods or services with a false value. If this element is not provided, the transaction is assumed to be a purchase of an airline ticket.  # noqa: E501

        :return: The ancillary_service_category of this Airline.  # noqa: E501
        :rtype: list[AirlineAncillaryServiceCategory]
        """
        return self._ancillary_service_category

    @ancillary_service_category.setter
    def ancillary_service_category(self, ancillary_service_category):
        """Sets the ancillary_service_category of this Airline.

        Identify the purchase of ancillary goods or services with a false value. If this element is not provided, the transaction is assumed to be a purchase of an airline ticket.  # noqa: E501

        :param ancillary_service_category: The ancillary_service_category of this Airline.  # noqa: E501
        :type: list[AirlineAncillaryServiceCategory]
        """

        self._ancillary_service_category = ancillary_service_category

    @property
    def ticket_purchase(self):
        """Gets the ticket_purchase of this Airline.  # noqa: E501

        Identifies if the transaction is a ticket purchase.  # noqa: E501

        :return: The ticket_purchase of this Airline.  # noqa: E501
        :rtype: bool
        """
        return self._ticket_purchase

    @ticket_purchase.setter
    def ticket_purchase(self, ticket_purchase):
        """Sets the ticket_purchase of this Airline.

        Identifies if the transaction is a ticket purchase.  # noqa: E501

        :param ticket_purchase: The ticket_purchase of this Airline.  # noqa: E501
        :type: bool
        """

        self._ticket_purchase = ticket_purchase

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
        if not isinstance(other, Airline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
