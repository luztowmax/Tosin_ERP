from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product
from .serializers import ProductSerializer
from .models import Sale
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sale

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def by_barcode(self, request):
        barcode = request.query_params.get('barcode')
        try:
            product = Product.objects.get(barcode=barcode)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)

def generate_invoice(request):
    sale_id = request.POST.get('sale_id')
    sale = Sale.objects.get(id=sale_id)

    invoice_data = {
        'detail': f'Invoice for {sale.product.name} - {sale.quantity}',
    }
    return JsonResponse(invoice_data)
@api_view(['POST'])
def record_sale(request):
    # Handle sale recording logic here
    return Response({'status' : 'sale recorded successfully'})


