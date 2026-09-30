"""Application exception hierarchy, mapped to HTTP responses centrally."""


class AppException(Exception):
    """Base class for domain errors."""

    status_code = 500
    detail = "Internal server error"


class NotFoundError(AppException):
    status_code = 404
    detail = "Resource not found"


class PermissionDeniedError(AppException):
    status_code = 403
    detail = "Permission denied"


class ConflictError(AppException):
    status_code = 409
    detail = "Resource conflict"
