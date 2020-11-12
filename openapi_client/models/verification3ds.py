# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.14.0.20201015.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Verification3ds(object):
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
        'code': 'str',
        'status': 'str',
        'scheme': 'str'
    }

    attribute_map = {
        'code': 'code',
        'status': 'status',
        'scheme': 'scheme'
    }

    def __init__(self, code=None, status=None, scheme=None):  # noqa: E501
        """Verification3ds - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._status = None
        self._scheme = None
        self.discriminator = None

        self.code = code
        if status is not None:
            self.status = status
        self.scheme = scheme

    @property
    def code(self):
        """Gets the code of this Verification3ds.  # noqa: E501

        3DS response code.  # noqa: E501

        :return: The code of this Verification3ds.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Verification3ds.

        3DS response code.  # noqa: E501

        :param code: The code of this Verification3ds.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and not re.search(r'^(?!\s*$).+', code):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._code = code

    @property
    def status(self):
        """Gets the status of this Verification3ds.  # noqa: E501

        Interpretation of the response code.  # noqa: E501

        :return: The status of this Verification3ds.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Verification3ds.

        Interpretation of the response code.  # noqa: E501

        :param status: The status of this Verification3ds.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def scheme(self):
        """Gets the scheme of this Verification3ds.  # noqa: E501

        Identifier of the scheme.  # noqa: E501

        :return: The scheme of this Verification3ds.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this Verification3ds.

        Identifier of the scheme.  # noqa: E501

        :param scheme: The scheme of this Verification3ds.  # noqa: E501
        :type: str
        """
        if scheme is None:
            raise ValueError("Invalid value for `scheme`, must not be `None`")  # noqa: E501
        if scheme is not None and not re.search(r'^(?!\s*$).+', scheme):  # noqa: E501
            raise ValueError(r"Invalid value for `scheme`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._scheme = scheme

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
        if not isinstance(other, Verification3ds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
