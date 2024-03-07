from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Customer, Product, Order
from .forms import CustomerForm, OrderForm, ProductForm
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'ecommerce/home.html'


class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'ecommerce/customer_list.html', {'customers': customers})

class CustomerDetailView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'ecommerce/customer_detail.html', {'customer': customer})

class CustomerCreateView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'ecommerce/customer_form.html', {'form': form})
    
    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'ecommerce/customer_form.html', {'form': form})

class CustomerUpdateView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(instance=customer)
        return render(request, 'ecommerce/customer_form.html', {'form': form})
    
    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'ecommerce/customer_form.html', {'form': form})


class CustomerDeleteView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'ecommerce/customer_confirm_delete.html', {'customer': customer})
    
    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect('customer_list')




class OrderListView(View):
    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'ecommerce/order_list.html', {'orders': orders})

class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        return render(request, 'ecommerce/order_detail.html', {'order': order})

class OrderCreateView(View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'ecommerce/order_form.html', {'form': form})
    
    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        return render(request, 'ecommerce/order_form.html', {'form': form})

class OrderUpdateView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(instance=order)
        return render(request, 'ecommerce/order_form.html', {'form': form})
    
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        return render(request, 'ecommerce/order_form.html', {'form': form})

class OrderDeleteView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        return render(request, 'ecommerce/order_confirm_delete.html', {'order': order})
    
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return redirect('order_list')




class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'ecommerce/product_list.html', {'products': products})

class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'ecommerce/product_detail.html', {'product': product})

class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'ecommerce/product_form.html', {'form': form})
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'ecommerce/product_form.html', {'form': form})

class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'ecommerce/product_form.html', {'form': form})
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'ecommerce/product_form.html', {'form': form})

class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'ecommerce/product_confirm_delete.html', {'product': product})
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('product_list')
