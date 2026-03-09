#decorator group
import inspect
from functools import wraps
from django.http import HttpResponseForbidden


def group_required(*group_names):
    """
    Decorator that accepts one or more group names.
    Works with both function-based views and class-based views.
    For CBVs, wraps dispatch() so that .as_view() is preserved.
    """
    def decorator(view):
        # Class-based view: patch dispatch() so .as_view() stays intact
        if inspect.isclass(view):
            original_dispatch = view.dispatch

            def patched_dispatch(self, request, *args, **kwargs):
                if request.user.groups.filter(name__in=group_names).exists():
                    return original_dispatch(self, request, *args, **kwargs)
                return HttpResponseForbidden("Você não tem permissão para acessar esta página")

            view.dispatch = patched_dispatch
            return view

        # Function-based view: wrap normally
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=group_names).exists():
                return view(request, *args, **kwargs)
            return HttpResponseForbidden("Você não tem permissão para acessar esta página")

        return wrapper

    return decorator