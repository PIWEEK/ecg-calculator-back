import sys
import os
import settings


def setup_anillo_app():
    from anillo.app import application
    from anillo.utils.common import chain
    from anillo.middlewares.json import wrap_json_body, wrap_json_response
    from anillo.middlewares.cors import wrap_cors, DEFAULT_HEADERS
    from anillo.middlewares.default_headers import wrap_default_headers
    from anillo.middlewares.params import wrap_query_params
    # from .middlewares import wrap_error_handler

    from tools.camelize.middlewares import wrap_camelize_response_body
    from tools.camelize.middlewares import wrap_underscoreize_request_body

    from .router import router

    handler = chain(
        wrap_cors(allow_headers=list(DEFAULT_HEADERS) + ["x-session-id", "accept-language", "authorization"]),
        # wrap_error_handler,
        wrap_json_body(),
        wrap_underscoreize_request_body,
        wrap_json_response,
        wrap_camelize_response_body,
        wrap_default_headers({}, {"Content-Type": "application/json"}),
        wrap_query_params,
        router
    )

    return application(handler)


def runserver():
    app = setup_anillo_app()
    from anillo import serving
    serving.run_simple(app, port=5500, host='0.0.0.0', threaded=True)

