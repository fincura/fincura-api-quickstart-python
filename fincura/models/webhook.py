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


class Webhook(object):
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
        'event_type': 'str',
        'webhook_url': 'str',
        'webhook_method': 'str',
        'external_id': 'str',
        'signing_key': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'event_type': 'event_type',
        'webhook_url': 'webhook_url',
        'webhook_method': 'webhook_method',
        'external_id': 'external_id',
        'signing_key': 'signing_key'
    }

    def __init__(self, uuid=None, event_type=None, webhook_url=None, webhook_method='POST', external_id=None, signing_key=None, local_vars_configuration=None):  # noqa: E501
        """Webhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._event_type = None
        self._webhook_url = None
        self._webhook_method = None
        self._external_id = None
        self._signing_key = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        self.event_type = event_type
        self.webhook_url = webhook_url
        if webhook_method is not None:
            self.webhook_method = webhook_method
        if external_id is not None:
            self.external_id = external_id
        if signing_key is not None:
            self.signing_key = signing_key

    @property
    def uuid(self):
        """Gets the uuid of this Webhook.  # noqa: E501


        :return: The uuid of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Webhook.


        :param uuid: The uuid of this Webhook.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def event_type(self):
        """Gets the event_type of this Webhook.  # noqa: E501


        :return: The event_type of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Webhook.


        :param event_type: The event_type of this Webhook.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DocumentFile.Received", "DocumentFile.Processing", "DocumentFile.HumanRequired", "DocumentFile.SpreadComplete", "*"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def webhook_url(self):
        """Gets the webhook_url of this Webhook.  # noqa: E501


        :return: The webhook_url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """Sets the webhook_url of this Webhook.


        :param webhook_url: The webhook_url of this Webhook.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and webhook_url is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                webhook_url is not None and len(webhook_url) > 2500):
            raise ValueError("Invalid value for `webhook_url`, length must be less than or equal to `2500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                webhook_url is not None and not re.search(r'^(?:[a-z0-9\.\-\+]*):\/\/(?:[^\s:@\/]+(?::[^\s:@\/]*)?@)?(?:(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}|\[[0-9a-f:\.]+\]|([a-z¡-￿0-9](?:[a-z¡-￿0-9-]{0,61}[a-z¡-￿0-9])?(?:\.(?!-)[a-z¡-￿0-9-]{1,63}(?<!-))*\.(?!-)(?:[a-z¡-￿-]{2,63}|xn--[a-z0-9]{1,59})(?<!-)\.?|localhost))(?::\d{2,5})?(?:[\/?#][^\s]*)?\Z', webhook_url)):  # noqa: E501
            raise ValueError(r"Invalid value for `webhook_url`, must be a follow pattern or equal to `/^(?:[a-z0-9\.\-\+]*):\/\/(?:[^\s:@\/]+(?::[^\s:@\/]*)?@)?(?:(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}|\[[0-9a-f:\.]+\]|([a-z¡-￿0-9](?:[a-z¡-￿0-9-]{0,61}[a-z¡-￿0-9])?(?:\.(?!-)[a-z¡-￿0-9-]{1,63}(?<!-))*\.(?!-)(?:[a-z¡-￿-]{2,63}|xn--[a-z0-9]{1,59})(?<!-)\.?|localhost))(?::\d{2,5})?(?:[\/?#][^\s]*)?\Z/`")  # noqa: E501

        self._webhook_url = webhook_url

    @property
    def webhook_method(self):
        """Gets the webhook_method of this Webhook.  # noqa: E501


        :return: The webhook_method of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_method

    @webhook_method.setter
    def webhook_method(self, webhook_method):
        """Sets the webhook_method of this Webhook.


        :param webhook_method: The webhook_method of this Webhook.  # noqa: E501
        :type: str
        """
        allowed_values = ["GET", "POST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and webhook_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `webhook_method` ({0}), must be one of {1}"  # noqa: E501
                .format(webhook_method, allowed_values)
            )

        self._webhook_method = webhook_method

    @property
    def external_id(self):
        """Gets the external_id of this Webhook.  # noqa: E501

        External ID is used to uniquely identify a record from your system in our system. Must be unique across records.  # noqa: E501

        :return: The external_id of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Webhook.

        External ID is used to uniquely identify a record from your system in our system. Must be unique across records.  # noqa: E501

        :param external_id: The external_id of this Webhook.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) > 255):
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `255`")  # noqa: E501

        self._external_id = external_id

    @property
    def signing_key(self):
        """Gets the signing_key of this Webhook.  # noqa: E501


        :return: The signing_key of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._signing_key

    @signing_key.setter
    def signing_key(self, signing_key):
        """Sets the signing_key of this Webhook.


        :param signing_key: The signing_key of this Webhook.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                signing_key is not None and len(signing_key) > 200):
            raise ValueError("Invalid value for `signing_key`, length must be less than or equal to `200`")  # noqa: E501

        self._signing_key = signing_key

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
        if not isinstance(other, Webhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Webhook):
            return True

        return self.to_dict() != other.to_dict()