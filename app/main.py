import ssl

from fastapi import FastAPI

from app.api.v1.hello_ow import hello_ow
from app.core.config import settings

app = FastAPI()
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(
    f"{settings.SSL_CERT_PATH}",
    keyfile=f"{settings.SSL_KEY_PATH}",
)


app.include_router(hello_ow.router)
