import falcon
from spectree import Response
from spectree import SpecTree
from serializers.serializers import MetaSerializer, CarSerializer

api = SpecTree(
    "falcon",
    title="Falcon Docs",
    path="docs"
)


class RootViews:
    @api.validate(
        resp=Response(
            HTTP_200=MetaSerializer,
        ), tags=['Meta']
    )
    def on_get(self, request, response, **kwargs):
        """
        Root of host
        """
        output = {
            'message': 'Falcon API'
        }
        response.status = falcon.HTTP_200
        response.media = output


class HealthView:
    @api.validate(
        resp=Response(
            HTTP_200=MetaSerializer,
        ),
        tags=['Meta']
    )
    def on_get(self, request, response, **kwargs):
        """
        Check health of service
        """
        output = {
            "message": "Status OK",
        }
        response.status = falcon.HTTP_200
        response.media = output


class APIViews:
    @api.validate(
        json=CarSerializer,
        resp=Response(
            HTTP_200=None,
        ),
        tags=['API']
    )
    def on_post(self, request, response, **kwargs):
        """
        Check health of service
        """
        a = request.media

        response.status = falcon.HTTP_200
        response.media = a
