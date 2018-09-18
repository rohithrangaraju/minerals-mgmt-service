import flask
import uuid
from ..constants import BAD_REQUEST_STATUS_CODE


def standard_error_response(status=BAD_REQUEST_STATUS_CODE, title='Bad Request', detail=None, id=None, errors=None,
                            **extras):
    if not errors:
        errors = [dict(
            status=status,
            title=title,
            detail=detail,
            **extras
        )]
        if id:
            errors[0]['id'] = id

    if not errors[0].get('id'):
        errors[0]['id'] = str(uuid.uuid4())

    response = flask.jsonify(errors=errors)
    response.status_code = status
    response.error_id = errors[0]['id']
    response.error_code = errors[0].get('code', None)
    return response


class InvalidInput(Exception):
    status_code = BAD_REQUEST_STATUS_CODE
    title = 'Invalid Request Body'

    def __init__(self, detail='invalid payload request'):
        Exception.__init__(self)
        self.detail = detail


class InvalidHeaderValue(Exception):
    status_code = BAD_REQUEST_STATUS_CODE
    title = 'Invalid Headers'

    def __init__(self, **kwargs):
        self.detail = kwargs.get('detail')
        del kwargs['detail']
        self.errors = kwargs


class LargeRequestBody(Exception):
    status_code = BAD_REQUEST_STATUS_CODE
    title = 'Large Request Body'

    def __init__(self, **kwargs):
        self.detail = kwargs.get('A very large request body.')


class ExceptionHandlers(object):
    @staticmethod
    def handle_uncaught_exception(e):
        if not flask.request:
            raise e

        extras = {}
        extras['meta'] = {
            'exception': {
                'class': e.__class__.__name__,
                'message': str(e),
            }
        }

        return standard_error_response(
            title='Server Error',
            status=500,
            detail='Uncaught exception occurred',
            **extras
        )

    @staticmethod
    def handle_invalid_payload(error):
        return standard_error_response(title=error.title, status=error.status_code, detail=error.detail)

    @staticmethod
    def register_all(app):
        app.errorhandler(Exception)(ExceptionHandlers.handle_uncaught_exception)
        app.errorhandler(InvalidInput)(ExceptionHandlers.handle_invalid_payload)
