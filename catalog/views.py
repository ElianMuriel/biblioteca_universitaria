from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.models import Libro
from catalog.serializers import LibroSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


@api_view(['POST'])
def prestamos_semana(request):
    data = request.data
    prestamos_por_dia = data.get('prestamosPorDia')

    if not isinstance(prestamos_por_dia, list) or len(prestamos_por_dia) != 7:
        return Response(
            {"error": "prestamosPorDia debe ser un arreglo de 7 números."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        prestamos_por_dia = [int(x) for x in prestamos_por_dia]
    except (TypeError, ValueError):
        return Response(
            {"error": "Todos los valores de prestamosPorDia deben ser números enteros."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    total_prestamos = sum(prestamos_por_dia)
    promedio_diario = total_prestamos / 7 if prestamos_por_dia else 0

    if total_prestamos < 10:
        mensaje = "Poca actividad de préstamo"
    elif 10 <= total_prestamos <= 30:
        mensaje = "Actividad normal"
    else:
        mensaje = "Alta demanda de libros"

    return Response(
        {
            "totalPrestamos": total_prestamos,
            "promedioDiario": round(promedio_diario, 2),
            "mensaje": mensaje,
        }
    )


@api_view(['POST'])
def calcular_multa(request):
    data = request.data
    dias_retraso = data.get('diasRetraso')
    multa_por_dia = data.get('multaPorDia')

    try:
        dias_retraso = float(dias_retraso)
        multa_por_dia = float(multa_por_dia)
    except (TypeError, ValueError):
        return Response(
            {"error": "diasRetraso y multaPorDia deben ser numéricos."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if dias_retraso <= 0:
        multa = 0.0
        mensaje = "Sin retraso"
    else:
        multa = dias_retraso * multa_por_dia
        if multa <= 5:
            mensaje = "Retraso leve"
        elif multa <= 15:
            mensaje = "Retraso moderado"
        else:
            mensaje = "Retraso grave, revisar con administración"

    return Response(
        {
            "diasRetraso": dias_retraso,
            "multa": round(multa, 2),
            "mensaje": mensaje,
        }
    )
