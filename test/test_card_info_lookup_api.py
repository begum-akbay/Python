# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.10.1.20200226.002
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.card_info_lookup_api import CardInfoLookupApi  # noqa: E501
from openapi_client.rest import ApiException


class TestCardInfoLookupApi(unittest.TestCase):
    """CardInfoLookupApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.card_info_lookup_api.CardInfoLookupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_card_info_lookup(self):
        """Test case for card_info_lookup

        Card information lookup.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
