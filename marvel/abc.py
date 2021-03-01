import abc
import typing

from redbot.core import Config
from redbot.core.bot import Red

class MixinMeta(abc.ABC):

    def __init__(self, *_args):
        self.settings: Config
        self.bot: Red
        self.sanitize: typing.Dict[str, bool]
