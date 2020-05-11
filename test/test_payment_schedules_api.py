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
from openapi_client.api.payment_schedules_api import PaymentSchedulesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPaymentSchedulesApi(unittest.TestCase):
    """PaymentSchedulesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.payment_schedules_api.PaymentSchedulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_payment_schedule(self):
        """Test case for cancel_payment_schedule

        Cancel a gateway payment schedule.  # noqa: E501
        """
        pass

    def test_create_payment_schedule(self):
        """Test case for create_payment_schedule

        Create gateway payment schedule.  # noqa: E501
        """
        pass

    def test_inquiry_payment_schedule(self):
        """Test case for inquiry_payment_schedule

        View a gateway payment schedule.  # noqa: E501
        """
        pass

    def test_update_payment_schedule(self):
        """Test case for update_payment_schedule

        Update a gateway payment schedule.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
