from typing import TYPE_CHECKING

from typing_extensions import override

from kozmoai.services.factory import ServiceFactory
from kozmoai.services.socket.service import SocketIOService

if TYPE_CHECKING:
    from kozmoai.services.cache.service import CacheService


class SocketIOFactory(ServiceFactory):
    def __init__(self) -> None:
        super().__init__(
            service_class=SocketIOService,
        )

    @override
    def create(self, cache_service: "CacheService"):
        return SocketIOService(cache_service)
