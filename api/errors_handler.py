from flask import jsonify


def resource_not_found(error):
    """resource not found"""
    response = jsonify({"message": "the requested resource could not be found on this server, check and try again"})
    response.status_code = 404
    return response


def server_error(error):
    """Handle 500 error."""
    response = jsonify({
        "message": " your request cannot be proccessed. the server experienced an error"
    })
    response.status_code = 500
    return response


def method_not_allowed(error):
    """Handle 405 error."""
    response = jsonify({"message": "Method not allowed, ensure correct method and try again"})
    response.status_code = 405
    return response

def bad_request(error):
    """Handle any 400 not checked."""
    response = jsonify({"message": "incorrect \
    data input format,provide data as {'keyword:'argument'}, with comma separated at the end of each pair"})
    response.status_code = 400
    return response