from starlette.middleware.base import BaseHTTPMiddleware


class RequestLoggerMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        with open(
            "logs.txt",
            "a"
        ) as log:

            log.write(
                f"{request.method} "
                f"{request.url}\n"
            )

        response = await call_next(
            request
        )

        return response