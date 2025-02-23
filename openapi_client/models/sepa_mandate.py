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


class SepaMandate(object):
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
        'reference': 'str',
        'url': 'str',
        'signature_date': 'date',
        'type': 'str'
    }

    attribute_map = {
        'reference': 'reference',
        'url': 'url',
        'signature_date': 'signatureDate',
        'type': 'type'
    }

    def __init__(self, reference=None, url=None, signature_date=None, type='SINGLE'):  # noqa: E501
        """SepaMandate - a model defined in OpenAPI"""  # noqa: E501

        self._reference = None
        self._url = None
        self._signature_date = None
        self._type = None
        self.discriminator = None

        self.reference = reference
        self.url = url
        self.signature_date = signature_date
        self.type = type

    @property
    def reference(self):
        """Gets the reference of this SepaMandate.  # noqa: E501

        Existing mandate reference, managed by merchant. Must match [A-Za-z0-9:?/+(),. -]{1,35} and not start with two slashes (\"//\"). Also known as the mandate ID.  # noqa: E501

        :return: The reference of this SepaMandate.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SepaMandate.

        Existing mandate reference, managed by merchant. Must match [A-Za-z0-9:?/+(),. -]{1,35} and not start with two slashes (\"//\"). Also known as the mandate ID.  # noqa: E501

        :param reference: The reference of this SepaMandate.  # noqa: E501
        :type: str
        """
        # if reference is None:
        #     raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501
        if reference is not None and len(reference) > 35:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `35`")  # noqa: E501
        if reference is not None and not re.search(r'[A-Za-z0-9:?\/+(),. -]{1,35}', reference):  # noqa: E501
            raise ValueError(r"Invalid value for `reference`, must be a follow pattern or equal to `/[A-Za-z0-9:?\/+(),. -]{1,35}/`")  # noqa: E501

        self._reference = reference

    @property
    def url(self):
        """Gets the url of this SepaMandate.  # noqa: E501

        Valid URL pointing to the SEPA mandate (PDF / HTML format recommended).  # noqa: E501

        :return: The url of this SepaMandate.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SepaMandate.

        Valid URL pointing to the SEPA mandate (PDF / HTML format recommended).  # noqa: E501

        :param url: The url of this SepaMandate.  # noqa: E501
        :type: str
        """
        # if url is None:
        #     raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if url is not None and len(url) > 100:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `100`")  # noqa: E501
        if url is not None and not re.search(r'^(?!\s*$).+', url):  # noqa: E501
            raise ValueError(r"Invalid value for `url`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._url = url

    @property
    def signature_date(self):
        """Gets the signature_date of this SepaMandate.  # noqa: E501

        Date of mandate signature.  # noqa: E501

        :return: The signature_date of this SepaMandate.  # noqa: E501
        :rtype: date
        """
        return self._signature_date

    @signature_date.setter
    def signature_date(self, signature_date):
        """Sets the signature_date of this SepaMandate.

        Date of mandate signature.  # noqa: E501

        :param signature_date: The signature_date of this SepaMandate.  # noqa: E501
        :type: date
        """
        # if signature_date is None:
        #     raise ValueError("Invalid value for `signature_date`, must not be `None`")  # noqa: E501

        self._signature_date = signature_date

    @property
    def type(self):
        """Gets the type of this SepaMandate.  # noqa: E501

        Sequence type of the direct debit. This defaults to 'SINGLE' if not provided.  # noqa: E501

        :return: The type of this SepaMandate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SepaMandate.

        Sequence type of the direct debit. This defaults to 'SINGLE' if not provided.  # noqa: E501

        :param type: The type of this SepaMandate.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["SINGLE", "FIRST_COLLECTION", "RECURRING_COLLECTION", "FINAL_COLLECTION"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, SepaMandate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
