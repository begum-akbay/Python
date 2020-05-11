# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.10.1.20200226.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class EndpointResponse(object):
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
        'endpoint_id': 'str',
        'status': 'str',
        'batch_number': 'str'
    }

    attribute_map = {
        'endpoint_id': 'endpointID',
        'status': 'status',
        'batch_number': 'batchNumber'
    }

    def __init__(self, endpoint_id=None, status=None, batch_number=None):  # noqa: E501
        """EndpointResponse - a model defined in OpenAPI"""  # noqa: E501

        self._endpoint_id = None
        self._status = None
        self._batch_number = None
        self.discriminator = None

        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if status is not None:
            self.status = status
        if batch_number is not None:
            self.batch_number = batch_number

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this EndpointResponse.  # noqa: E501

        Specifies the identifier of an endpoint.  # noqa: E501

        :return: The endpoint_id of this EndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this EndpointResponse.

        Specifies the identifier of an endpoint.  # noqa: E501

        :param endpoint_id: The endpoint_id of this EndpointResponse.  # noqa: E501
        :type: str
        """

        self._endpoint_id = endpoint_id

    @property
    def status(self):
        """Gets the status of this EndpointResponse.  # noqa: E501

        Defines the clearing status of an endpoint.  # noqa: E501

        :return: The status of this EndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EndpointResponse.

        Defines the clearing status of an endpoint.  # noqa: E501

        :param status: The status of this EndpointResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPROVED", "DECLINED", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def batch_number(self):
        """Gets the batch_number of this EndpointResponse.  # noqa: E501

        Defines the batch number of an endpoint clearing process.  # noqa: E501

        :return: The batch_number of this EndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._batch_number

    @batch_number.setter
    def batch_number(self, batch_number):
        """Sets the batch_number of this EndpointResponse.

        Defines the batch number of an endpoint clearing process.  # noqa: E501

        :param batch_number: The batch_number of this EndpointResponse.  # noqa: E501
        :type: str
        """

        self._batch_number = batch_number

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
        if not isinstance(other, EndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
