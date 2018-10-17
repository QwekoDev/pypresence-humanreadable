from typing import Union

import dateparser
from pypresence import Client, Presence

from .exceptions import *

ALLOWED_CLIENT_TYPES = (Client, Presence)


class HumanPresence:
    def __init__(self, client: Union[Client, Presence]):
        if not isinstance(client, ALLOWED_CLIENT_TYPES):
            raise BadArgument('Union[Client, Presence]', type(client))

        self.client = client

    def _parse(self, *humanstr):
        humanstr = "".join(humanstr)


    def set_start(self, when_it_started):
        pass
