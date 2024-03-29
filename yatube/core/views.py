from django.shortcuts import render

from http import HTTPStatus


def page_not_found(request, exception):
    return render(
        request, 'core/404.html',
        {'path': request.path},
        status=HTTPStatus.NOT_FOUND
    )


def csrf_failure(request, reason=''):
    return render(
        request, 'core/403csrf.html',
        {'path': request.path},
        status=HTTPStatus.FORBIDDEN
    )


def server_error(request, reason=''):
    return render(
        request, 'core/500.html',
        {'path': request.path},
        status=HTTPStatus.INTERNAL_SERVER_ERROR
    )
