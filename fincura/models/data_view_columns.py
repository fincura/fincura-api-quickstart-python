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


class DataViewColumns(object):
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
        'statement_date': 'datetime',
        'reporting_interval': 'str',
        'preparation_type': 'str',
        'prepared_by': 'str',
        'months_in_interval': 'int',
        'cells': 'list[DataViewCells]'
    }

    attribute_map = {
        'label': 'label',
        'statement_date': 'statement_date',
        'reporting_interval': 'reporting_interval',
        'preparation_type': 'preparation_type',
        'prepared_by': 'prepared_by',
        'months_in_interval': 'months_in_interval',
        'cells': 'cells'
    }

    def __init__(self, label=None, statement_date=None, reporting_interval=None, preparation_type=None, prepared_by=None, months_in_interval=None, cells=None, local_vars_configuration=None):  # noqa: E501
        """DataViewColumns - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._statement_date = None
        self._reporting_interval = None
        self._preparation_type = None
        self._prepared_by = None
        self._months_in_interval = None
        self._cells = None
        self.discriminator = None

        self.label = label
        self.statement_date = statement_date
        self.reporting_interval = reporting_interval
        self.preparation_type = preparation_type
        self.prepared_by = prepared_by
        self.months_in_interval = months_in_interval
        self.cells = cells

    @property
    def label(self):
        """Gets the label of this DataViewColumns.  # noqa: E501


        :return: The label of this DataViewColumns.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DataViewColumns.


        :param label: The label of this DataViewColumns.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def statement_date(self):
        """Gets the statement_date of this DataViewColumns.  # noqa: E501


        :return: The statement_date of this DataViewColumns.  # noqa: E501
        :rtype: datetime
        """
        return self._statement_date

    @statement_date.setter
    def statement_date(self, statement_date):
        """Sets the statement_date of this DataViewColumns.


        :param statement_date: The statement_date of this DataViewColumns.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and statement_date is None:  # noqa: E501
            raise ValueError("Invalid value for `statement_date`, must not be `None`")  # noqa: E501

        self._statement_date = statement_date

    @property
    def reporting_interval(self):
        """Gets the reporting_interval of this DataViewColumns.  # noqa: E501


        :return: The reporting_interval of this DataViewColumns.  # noqa: E501
        :rtype: str
        """
        return self._reporting_interval

    @reporting_interval.setter
    def reporting_interval(self, reporting_interval):
        """Sets the reporting_interval of this DataViewColumns.


        :param reporting_interval: The reporting_interval of this DataViewColumns.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reporting_interval is None:  # noqa: E501
            raise ValueError("Invalid value for `reporting_interval`, must not be `None`")  # noqa: E501

        self._reporting_interval = reporting_interval

    @property
    def preparation_type(self):
        """Gets the preparation_type of this DataViewColumns.  # noqa: E501


        :return: The preparation_type of this DataViewColumns.  # noqa: E501
        :rtype: str
        """
        return self._preparation_type

    @preparation_type.setter
    def preparation_type(self, preparation_type):
        """Sets the preparation_type of this DataViewColumns.


        :param preparation_type: The preparation_type of this DataViewColumns.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and preparation_type is None:  # noqa: E501
            raise ValueError("Invalid value for `preparation_type`, must not be `None`")  # noqa: E501

        self._preparation_type = preparation_type

    @property
    def prepared_by(self):
        """Gets the prepared_by of this DataViewColumns.  # noqa: E501


        :return: The prepared_by of this DataViewColumns.  # noqa: E501
        :rtype: str
        """
        return self._prepared_by

    @prepared_by.setter
    def prepared_by(self, prepared_by):
        """Sets the prepared_by of this DataViewColumns.


        :param prepared_by: The prepared_by of this DataViewColumns.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and prepared_by is None:  # noqa: E501
            raise ValueError("Invalid value for `prepared_by`, must not be `None`")  # noqa: E501

        self._prepared_by = prepared_by

    @property
    def months_in_interval(self):
        """Gets the months_in_interval of this DataViewColumns.  # noqa: E501


        :return: The months_in_interval of this DataViewColumns.  # noqa: E501
        :rtype: int
        """
        return self._months_in_interval

    @months_in_interval.setter
    def months_in_interval(self, months_in_interval):
        """Sets the months_in_interval of this DataViewColumns.


        :param months_in_interval: The months_in_interval of this DataViewColumns.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and months_in_interval is None:  # noqa: E501
            raise ValueError("Invalid value for `months_in_interval`, must not be `None`")  # noqa: E501

        self._months_in_interval = months_in_interval

    @property
    def cells(self):
        """Gets the cells of this DataViewColumns.  # noqa: E501


        :return: The cells of this DataViewColumns.  # noqa: E501
        :rtype: list[DataViewCells]
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        """Sets the cells of this DataViewColumns.


        :param cells: The cells of this DataViewColumns.  # noqa: E501
        :type: list[DataViewCells]
        """
        if self.local_vars_configuration.client_side_validation and cells is None:  # noqa: E501
            raise ValueError("Invalid value for `cells`, must not be `None`")  # noqa: E501

        self._cells = cells

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
        if not isinstance(other, DataViewColumns):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataViewColumns):
            return True

        return self.to_dict() != other.to_dict()
