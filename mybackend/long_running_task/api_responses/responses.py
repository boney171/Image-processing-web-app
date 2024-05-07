from rest_framework.response import Response
from rest_framework import status

def standard_response(data=None, message=None, errors=None, status_code=status.HTTP_200_OK):
    return Response({
        "message": message,
        "data": data,
        "errors": errors
    }, status=status_code)

def long_running_task_response( task_id, status, created_at, location, status_code):
    return Response({
        "taskId": task_id,
        "status": status,
        "createdAt": created_at,
        "location": location,
    }, status=status_code)