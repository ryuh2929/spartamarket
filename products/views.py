from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


# 홈화면 겸 등록 상품 목록
def index(request):
  products = Product.objects.all().order_by("-pk")
  context = {"products": products}
  return render(request, "products/index.html", context)

# 상세 페이지
def product_detail(request, pk):
  product = get_object_or_404(Product, pk=pk)
  product.views += 1
  product.save()
  context = {"product": product}
  return render(request, "products/product_detail.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def create(request):
  if request.method == "POST":
    form = ProductForm(request.POST)
    if form.is_valid():
      product = form.save()
      return redirect("products:product_detail", product.pk)
    return redirect("products:create")
  else:
    form = ProductForm()
  context = {"form": form}
  return render(request, "products/create.html", context)

# 글 삭제
@login_required
@require_POST
def delete(request, pk):
  product = Product.objects.get(pk=pk)
  product.delete()
  return redirect("index")

# 글 수정
@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
  if request.method == "POST":
    title = request.POST.get("title")
    content = request.POST.get("content")
    price = request.POST.get("price")

    product = Product.objects.get(pk=pk)
    product.title = title
    product.content = content
    product.price = price
    product.save()
    return redirect("products:product_detail", pk=product.pk)
  else:
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "products/update.html", context)