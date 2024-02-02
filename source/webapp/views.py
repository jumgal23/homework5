from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def perform_operation(request, operation):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            A = float(data.get("A"))
            B = float(data.get("B"))

            if operation == 'add':
                result = A + B
            elif operation == 'subtract':
                result = A - B
            elif operation == 'multiply':
                result = A * B
            elif operation == 'divide':
                if B == 0:
                    raise ZeroDivisionError("Division by zero!")
                result = A / B
            else:
                return JsonResponse({"error": "Invalid operation!"}, status=400)

            return JsonResponse({"answer": result})
        except (ValueError, TypeError) as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid method!"}, status=400)
