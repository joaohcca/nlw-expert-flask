from src.views.https_types.http_request import HttpRequest
from src.views.https_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    '''
        responsability for interacting with HTTP protocol
    '''

    def validate_and_create(self, http_requests: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        #entrada de dados via HTTP
        body = http_requests.body
        product_code = body["product_code"]

        #Lógica de Regra de Negocio
        formatted_response = tag_creator_controller.create(product_code)

        #Retorno HTTP
        return HttpResponse(status_code=200, body=formatted_response)
