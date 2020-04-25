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

from threading import Timer
from ytscm.event import YTSCEvent

import google_auth_oauthlib.flow as oauth
import googleapiclient.discovery
import googleapiclient.errors


class YTSCMonitor:
    """
    Monitors YouTube Super Chat events and triggers an update function if a
    new Super Chat is received.
    """

    # youtube client
    __youtube = None

    # dictionary of super chats from the most recent fetch
    __super_chat_events = []

    # update function
    __update = None

    # autofetch timer
    __autofetch_timer = None

    def __init__(self, client_secrets_file, update_function=None):
        """
        Creates a new super chat monitor from a client secrets file
        :param client_secrets_file: the client secrets file
        :param update_function: the function to call when a new Super Chat is
        received
        """

        # api context
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        api_service_name = "youtube"
        api_version = "v3"

        # instantiate credentials
        flow = oauth.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file=client_secrets_file,
            scopes=scopes,
        )

        credentials = flow.run_console()

        # get youtube client
        self.__youtube = googleapiclient.discovery.build(
            api_service_name,
            api_version,
            credentials=credentials
        )

        # fetch the initial list of super chats
        self.fetch()

        # set update function (must come after initial fetch)
        self.__update = update_function

    def fetch(self):
        """
        Fetches a new list of super chats from the YouTube client
        """

        # create request
        request = self.__youtube.superChatEvents().list(
            part="snippet"
        )

        # execute request
        response = request.execute()

        # iterate through super chats
        for super_chat_json in response['items']:

            # create a new super chat object
            super_chat_event = YTSCEvent(super_chat_json)

            # if its not already in our list
            if super_chat_event not in self.__super_chat_events:

                # add it to our list
                self.__super_chat_events.append(super_chat_event)

                # call our update function and pass the super chat event
                if self.__update is not None:
                    self.__update(super_chat_event)

    def start(self, interval):
        """
        Begins automatically fetching and monitoring new super chats
        at a specified interval
        :param interval - the amount of time in seconds between fetches
        """
        self.__autofetch_timer = self.__AutoFetchTimer(interval, self.fetch)
        self.__autofetch_timer.start()
        print("Started monitoring Super Chats!")

    def stop(self):
        """
        Stops automatically fetching and monitoring new super chats
        """
        if self.__autofetch_timer is not None:
            self.__autofetch_timer.cancel()
        print("Stopped monitoring Super Chats!")

    class __AutoFetchTimer:
        """
        Repeating timer for autofetch functionality
        """

        def __init__(self, seconds, target):
            self._should_continue = False
            self.is_running = False
            self.seconds = seconds
            self.target = target
            self.thread = None

        def _handle_target(self):
            self.is_running = True
            self.target()
            self.is_running = False
            self._start_timer()

        def _start_timer(self):
            if self._should_continue:
                self.thread = Timer(self.seconds, self._handle_target)
                self.thread.start()

        def start(self):
            if not self._should_continue and not self.is_running:
                self._should_continue = True
                self._start_timer()

        def cancel(self):
            if self.thread is not None:
                self._should_continue = False
            self.thread.cancel()
