from django.http import HttpResponse


def users(request, user_id=None):
    response = "Here must be user. "
    if user_id:
        response += f"User id is {user_id}."
    return HttpResponse(response)
