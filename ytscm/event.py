"""
YouTube Super Chat Monitor
Copyright (C) 2020 Remington Creative

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from ytscm.supporter import YTSCSupporterDetails


class YTSCEvent:
    """
    Contains YouTube Super Chat event attributes.
    """

    """
    The ID that YouTube assigns to uniquely identify the Super Chat event.
    """
    __id = None

    """
    The YouTube channel ID that identifies the channel that broadcast the live 
    stream associated with the Super Chat event.
    """
    __channel_id = None

    """
    Details about the supporter's channel.
    """
    __supporter_details = None

    """
    The text content of the supporter's comment.
    """
    __comment_text = None

    """
    The date and time when the Super Chat was purchased. The value is specified 
    in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.
    """
    __created_at = None

    """
    The purchase amount, in micros of the purchase currency.
    """
    __amount_micros = None

    """
    The currency in which the purchase was made. The value is an ISO 4217 
    currency code.
    """
    __currency = None

    """
    A string, like $1.00, that shows the purchase amount and currency.
    """
    __display_string = None

    """
    The tier for the paid message.
    """
    __message_type = None

    def __init__(self, super_chat_json):
        """
        Creates an object from a JSON super chat event object
        :param super_chat_json: the JSON super chat event
        """

        self.__id = super_chat_json['id']

        self.__channel_id = super_chat_json['snippet']['channelId']

        self.__supporter_details = YTSCSupporterDetails(
            super_chat_json['snippet']['supporterDetails']
        )

        self.__comment_text = super_chat_json['snippet']['commentText']

        self.__created_at = super_chat_json['snippet']['createdAt']

        self.__amount_micros = super_chat_json['snippet']['amountMicros']

        self.__currency = super_chat_json['snippet']['currency']

        self.__currency = super_chat_json['snippet']['currency']

        self.__display_string = super_chat_json['snippet']['displayString']

    def get_id(self):
        return self.__id

    def get_channel_id(self):
        return self.__channel_id

    def get_supporter_details(self):
        return self.__supporter_details

    def get_comment_text(self):
        return self.__comment_text

    def get_created_at(self):
        return self.__created_at

    def get_amount_micros(self):
        return self.__amount_micros

    def get_currency(self):
        return self.__currency

    def get_display_string(self):
        return self.__display_string

    def get_message_type(self):
        return self.__message_type

    def __eq__(self, other):
        return self.__id == other.__id
