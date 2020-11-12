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


class StoreBrandingStyleConfiguration(object):
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
        'id': 'str',
        'combined': 'CombinedMode',
        'classic': 'ClassicMode'
    }

    attribute_map = {
        'id': 'id',
        'combined': 'combined',
        'classic': 'classic'
    }

    def __init__(self, id=None, combined=None, classic=None):  # noqa: E501
        """StoreBrandingStyleConfiguration - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._combined = None
        self._classic = None
        self.discriminator = None

        self.id = id
        if combined is not None:
            self.combined = combined
        if classic is not None:
            self.classic = classic

    @property
    def id(self):
        """Gets the id of this StoreBrandingStyleConfiguration.  # noqa: E501

        An optional outlet id for clients that support multiple stores in the same developer app.  # noqa: E501

        :return: The id of this StoreBrandingStyleConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoreBrandingStyleConfiguration.

        An optional outlet id for clients that support multiple stores in the same developer app.  # noqa: E501

        :param id: The id of this StoreBrandingStyleConfiguration.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def combined(self):
        """Gets the combined of this StoreBrandingStyleConfiguration.  # noqa: E501


        :return: The combined of this StoreBrandingStyleConfiguration.  # noqa: E501
        :rtype: CombinedMode
        """
        return self._combined

    @combined.setter
    def combined(self, combined):
        """Sets the combined of this StoreBrandingStyleConfiguration.


        :param combined: The combined of this StoreBrandingStyleConfiguration.  # noqa: E501
        :type: CombinedMode
        """

        self._combined = combined

    @property
    def classic(self):
        """Gets the classic of this StoreBrandingStyleConfiguration.  # noqa: E501


        :return: The classic of this StoreBrandingStyleConfiguration.  # noqa: E501
        :rtype: ClassicMode
        """
        return self._classic

    @classic.setter
    def classic(self, classic):
        """Sets the classic of this StoreBrandingStyleConfiguration.


        :param classic: The classic of this StoreBrandingStyleConfiguration.  # noqa: E501
        :type: ClassicMode
        """

        self._classic = classic

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
        if not isinstance(other, StoreBrandingStyleConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
