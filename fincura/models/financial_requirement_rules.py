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


class FinancialRequirementRules(object):
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
        'uuid': 'str',
        'threshold_value': 'float',
        'comparer': 'str',
        'start_date': 'date',
        'end_date': 'date'
    }

    attribute_map = {
        'uuid': 'uuid',
        'threshold_value': 'threshold_value',
        'comparer': 'comparer',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, uuid=None, threshold_value=None, comparer=None, start_date=None, end_date=None, local_vars_configuration=None):  # noqa: E501
        """FinancialRequirementRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._threshold_value = None
        self._comparer = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        self.threshold_value = threshold_value
        if comparer is not None:
            self.comparer = comparer
        self.start_date = start_date
        self.end_date = end_date

    @property
    def uuid(self):
        """Gets the uuid of this FinancialRequirementRules.  # noqa: E501


        :return: The uuid of this FinancialRequirementRules.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this FinancialRequirementRules.


        :param uuid: The uuid of this FinancialRequirementRules.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def threshold_value(self):
        """Gets the threshold_value of this FinancialRequirementRules.  # noqa: E501


        :return: The threshold_value of this FinancialRequirementRules.  # noqa: E501
        :rtype: float
        """
        return self._threshold_value

    @threshold_value.setter
    def threshold_value(self, threshold_value):
        """Sets the threshold_value of this FinancialRequirementRules.


        :param threshold_value: The threshold_value of this FinancialRequirementRules.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and threshold_value is None:  # noqa: E501
            raise ValueError("Invalid value for `threshold_value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                threshold_value is not None and threshold_value > 1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `threshold_value`, must be a value less than or equal to `1000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                threshold_value is not None and threshold_value < -1000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `threshold_value`, must be a value greater than or equal to `-1000000000000000000`")  # noqa: E501

        self._threshold_value = threshold_value

    @property
    def comparer(self):
        """Gets the comparer of this FinancialRequirementRules.  # noqa: E501


        :return: The comparer of this FinancialRequirementRules.  # noqa: E501
        :rtype: str
        """
        return self._comparer

    @comparer.setter
    def comparer(self, comparer):
        """Sets the comparer of this FinancialRequirementRules.


        :param comparer: The comparer of this FinancialRequirementRules.  # noqa: E501
        :type: str
        """
        allowed_values = ["==", "!=", ">", "<", ">=", "<="]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and comparer not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `comparer` ({0}), must be one of {1}"  # noqa: E501
                .format(comparer, allowed_values)
            )

        self._comparer = comparer

    @property
    def start_date(self):
        """Gets the start_date of this FinancialRequirementRules.  # noqa: E501


        :return: The start_date of this FinancialRequirementRules.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FinancialRequirementRules.


        :param start_date: The start_date of this FinancialRequirementRules.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this FinancialRequirementRules.  # noqa: E501


        :return: The end_date of this FinancialRequirementRules.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this FinancialRequirementRules.


        :param end_date: The end_date of this FinancialRequirementRules.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

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
        if not isinstance(other, FinancialRequirementRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FinancialRequirementRules):
            return True

        return self.to_dict() != other.to_dict()
