from flask import jsonify, make_response


def response(status, message, status_code):
    """
    Make an http response helper
    :param status: Status message
    :param message: Response Message
    :param status_code: Http response code
    :return:
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code
