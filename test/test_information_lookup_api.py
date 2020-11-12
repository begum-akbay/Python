# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.14.0.20201015.001
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.information_lookup_api import InformationLookupApi  # noqa: E501
from openapi_client.rest import ApiException


class TestInformationLookupApi(unittest.TestCase):
    """InformationLookupApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.information_lookup_api.InformationLookupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_card_info_lookup(self):
        """Test case for card_info_lookup

        Card information lookup.  # noqa: E501
        """
        pass

    def test_lookup_account(self):
        """Test case for lookup_account

        Account information lookup.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
