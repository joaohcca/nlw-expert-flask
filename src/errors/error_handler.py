from src.views.https_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        #enviar para servico de log
        #disparar envio de email
        return HttpResponse(status_code=error.status_code, body={
            "errors": [{
                "title": error.name,
                "detail": error.message
            }]
        }
    )

    return HttpResponse(
        status_code=422,
        body={
            "errors": [{
            "title": "Server Error",
            "detail": str(error)
        }]
        }
    )
