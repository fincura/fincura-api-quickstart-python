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


class DataViewCellFormat(object):
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
        'text_format': 'str'
    }

    attribute_map = {
        'text_format': 'text_format'
    }

    def __init__(self, text_format=None, local_vars_configuration=None):  # noqa: E501
        """DataViewCellFormat - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._text_format = None
        self.discriminator = None

        self.text_format = text_format

    @property
    def text_format(self):
        """Gets the text_format of this DataViewCellFormat.  # noqa: E501


        :return: The text_format of this DataViewCellFormat.  # noqa: E501
        :rtype: str
        """
        return self._text_format

    @text_format.setter
    def text_format(self, text_format):
        """Sets the text_format of this DataViewCellFormat.


        :param text_format: The text_format of this DataViewCellFormat.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text_format is None:  # noqa: E501
            raise ValueError("Invalid value for `text_format`, must not be `None`")  # noqa: E501
        allowed_values = ["PERCENT", "CURRENCY", "RATIO", "DAYS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and text_format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `text_format` ({0}), must be one of {1}"  # noqa: E501
                .format(text_format, allowed_values)
            )

        self._text_format = text_format

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
        if not isinstance(other, DataViewCellFormat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataViewCellFormat):
            return True

        return self.to_dict() != other.to_dict()
