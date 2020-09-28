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


class DataViewRows(object):
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
        'label': 'str',
        'line_item': 'DataViewCalculatedValueLineItem',
        'indentation': 'int',
        'row_format': 'DataViewRowFormat',
        'cell_format': 'DataViewCellFormat'
    }

    attribute_map = {
        'label': 'label',
        'line_item': 'line_item',
        'indentation': 'indentation',
        'row_format': 'row_format',
        'cell_format': 'cell_format'
    }

    def __init__(self, label=None, line_item=None, indentation=None, row_format=None, cell_format=None, local_vars_configuration=None):  # noqa: E501
        """DataViewRows - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._line_item = None
        self._indentation = None
        self._row_format = None
        self._cell_format = None
        self.discriminator = None

        self.label = label
        self.line_item = line_item
        self.indentation = indentation
        self.row_format = row_format
        self.cell_format = cell_format

    @property
    def label(self):
        """Gets the label of this DataViewRows.  # noqa: E501


        :return: The label of this DataViewRows.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DataViewRows.


        :param label: The label of this DataViewRows.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def line_item(self):
        """Gets the line_item of this DataViewRows.  # noqa: E501


        :return: The line_item of this DataViewRows.  # noqa: E501
        :rtype: DataViewCalculatedValueLineItem
        """
        return self._line_item

    @line_item.setter
    def line_item(self, line_item):
        """Sets the line_item of this DataViewRows.


        :param line_item: The line_item of this DataViewRows.  # noqa: E501
        :type: DataViewCalculatedValueLineItem
        """
        if self.local_vars_configuration.client_side_validation and line_item is None:  # noqa: E501
            raise ValueError("Invalid value for `line_item`, must not be `None`")  # noqa: E501

        self._line_item = line_item

    @property
    def indentation(self):
        """Gets the indentation of this DataViewRows.  # noqa: E501


        :return: The indentation of this DataViewRows.  # noqa: E501
        :rtype: int
        """
        return self._indentation

    @indentation.setter
    def indentation(self, indentation):
        """Sets the indentation of this DataViewRows.


        :param indentation: The indentation of this DataViewRows.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and indentation is None:  # noqa: E501
            raise ValueError("Invalid value for `indentation`, must not be `None`")  # noqa: E501

        self._indentation = indentation

    @property
    def row_format(self):
        """Gets the row_format of this DataViewRows.  # noqa: E501


        :return: The row_format of this DataViewRows.  # noqa: E501
        :rtype: DataViewRowFormat
        """
        return self._row_format

    @row_format.setter
    def row_format(self, row_format):
        """Sets the row_format of this DataViewRows.


        :param row_format: The row_format of this DataViewRows.  # noqa: E501
        :type: DataViewRowFormat
        """
        if self.local_vars_configuration.client_side_validation and row_format is None:  # noqa: E501
            raise ValueError("Invalid value for `row_format`, must not be `None`")  # noqa: E501

        self._row_format = row_format

    @property
    def cell_format(self):
        """Gets the cell_format of this DataViewRows.  # noqa: E501


        :return: The cell_format of this DataViewRows.  # noqa: E501
        :rtype: DataViewCellFormat
        """
        return self._cell_format

    @cell_format.setter
    def cell_format(self, cell_format):
        """Sets the cell_format of this DataViewRows.


        :param cell_format: The cell_format of this DataViewRows.  # noqa: E501
        :type: DataViewCellFormat
        """
        if self.local_vars_configuration.client_side_validation and cell_format is None:  # noqa: E501
            raise ValueError("Invalid value for `cell_format`, must not be `None`")  # noqa: E501

        self._cell_format = cell_format

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
        if not isinstance(other, DataViewRows):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataViewRows):
            return True

        return self.to_dict() != other.to_dict()