# coding: utf-8

"""
    Fincura Integration API

    This [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer) allows you to interact with the Fincura processing and insights engine.   # Authentication  This API uses API keys generated from a Fincura User account. To get access to your User account, speak with you Fincura account manager.  # Accepted Media Types  | File&nbsp;Type&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Extension(s)     | Content-Type(s) | | -------------------------------- |-------------- | ------------ | | PDF File | .pdf | `application/pdf` , `application/x-pdf` | | Excel File | .xls | `application/vnd.ms-excel`  | | Excel File | .xlsx | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`  | | PNG Image | .png | `image/png`  | | GIF Image | .gif | `image/gif`  | | JPG Image | .jpg, .jpeg | `image/jpeg`  | | GIF Image | .gif | `image/gif`  |   # Getting Started  1. [Create a Borrower](#operation/createBorrower)  2. [Add a file](#operation/createDocumentFile) for that Borrower. 3. Analyze in the Fincura App  ****  # noqa: E501

    The version of the OpenAPI document: 1.2.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fincura.configuration import Configuration


class LoanFinancialsCells(object):
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
        'line_item_id': 'int',
        'ref': 'str',
        'calculated_value': 'LoanFinancialsCalculatedValue'
    }

    attribute_map = {
        'line_item_id': 'line_item_id',
        'ref': 'ref',
        'calculated_value': 'calculated_value'
    }

    def __init__(self, line_item_id=None, ref=None, calculated_value=None, local_vars_configuration=None):  # noqa: E501
        """LoanFinancialsCells - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._line_item_id = None
        self._ref = None
        self._calculated_value = None
        self.discriminator = None

        if line_item_id is not None:
            self.line_item_id = line_item_id
        if ref is not None:
            self.ref = ref
        if calculated_value is not None:
            self.calculated_value = calculated_value

    @property
    def line_item_id(self):
        """Gets the line_item_id of this LoanFinancialsCells.  # noqa: E501


        :return: The line_item_id of this LoanFinancialsCells.  # noqa: E501
        :rtype: int
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this LoanFinancialsCells.


        :param line_item_id: The line_item_id of this LoanFinancialsCells.  # noqa: E501
        :type: int
        """

        self._line_item_id = line_item_id

    @property
    def ref(self):
        """Gets the ref of this LoanFinancialsCells.  # noqa: E501


        :return: The ref of this LoanFinancialsCells.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this LoanFinancialsCells.


        :param ref: The ref of this LoanFinancialsCells.  # noqa: E501
        :type: str
        """

        self._ref = ref

    @property
    def calculated_value(self):
        """Gets the calculated_value of this LoanFinancialsCells.  # noqa: E501


        :return: The calculated_value of this LoanFinancialsCells.  # noqa: E501
        :rtype: LoanFinancialsCalculatedValue
        """
        return self._calculated_value

    @calculated_value.setter
    def calculated_value(self, calculated_value):
        """Sets the calculated_value of this LoanFinancialsCells.


        :param calculated_value: The calculated_value of this LoanFinancialsCells.  # noqa: E501
        :type: LoanFinancialsCalculatedValue
        """

        self._calculated_value = calculated_value

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
        if not isinstance(other, LoanFinancialsCells):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoanFinancialsCells):
            return True

        return self.to_dict() != other.to_dict()
