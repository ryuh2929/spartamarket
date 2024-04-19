from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from .models import Product
from .forms import ProductForm


def index(request):
  products = Product.objects.all().order_by("-pk")
  context = {"products": products}
  return render(request, "products/index.html", context)

def product_detail(request, pk):
  product = get_object_or_404(Product, pk=pk)
  context = {"product": product}
  return render(request, "products/product_detail.html", context)

def new(request):
  form = ProductForm()
  context = {"form": form}
  return render(request, "products/new.html", context)

@require_http_methods(["GET", "POST"])
def create(request):
  if request.method == "POST":
    form = ProductForm(request.POST)
    if form.is_valid():
      product = form.save()
      return redirect("products:product_detail", product.pk)
    return redirect("new")
  else:
    form = ProductForm()
  return redirect("new")

@require_POST
def delete(request, pk):
  product = Product.objects.get(pk=pk)
  product.delete()
  return redirect("index")

# 수정
@require_http_methods(["GET", "POST"])
def update(request, pk):
  if request.method == "POST":
    product = Product.objects.get(pk=pk)
    product.save()
    return redirect("product_detail", pk=product.pk)
  else:
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "update.html", context)