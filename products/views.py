from django.views.generic import ListView,DetailView
from .models import Product, ProductsImages
# Create your views here.

class ProductsList(ListView):
    model = Product


class ProcuctDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context['images'] = ProductsImages.objects.filter(product=myproduct)
        context['related'] = Product.objects.filter(category=myproduct.category)[:10]
        return context