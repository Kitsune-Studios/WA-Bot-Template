"""Module for the custom middleware."""

from collections.abc import Awaitable, Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class CustomMiddleware(BaseHTTPMiddleware):
    """A custom middleware that processes requests."""

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        """Dispatch the incoming request and return the response.

        Args:
            request (Request): The incoming HTTP request.
            call_next (Callable): The next callable in the middleware stack.

        Returns:
            The HTTP response.

        """
        return await call_next(request)
