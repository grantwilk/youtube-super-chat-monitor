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


class YTSCSupporterDetails:
    """
    Contains YouTube Super Chat supporter details.
    """

    """
    The supporter's YouTube channel ID.
    """
    __channel_id = None

    """
    The URL of the supporter's channel.
    """
    __channel_url = None

    """
    The display name of the supporter's channel.
    """
    __display_name = None

    """
    The avatar URL for the supporter's channel.
    """
    __profile_image_url = None

    def __init__(self, supporter_details):
        """
        Creates an object from a JSON supporter details object
        :param supporter_details - the JSON supporter details object
        """
        self.channel_id = supporter_details['channelId']
        self.channel_url = supporter_details['channelUrl']
        self.display_name = supporter_details['displayName']
        self.profile_image_url = supporter_details['profileImageUrl']

    def get_channel_id(self):
        return self.channel_id

    def get_channel_url(self):
        return self.channel_url

    def get_display_name(self):
        return self.display_name

    def get_profile_image_url(self):
        return self.profile_image_url
