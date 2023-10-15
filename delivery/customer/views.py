from datetime import datetime
import json
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib import messages
from customer import views
from .models import MenuItem, Category, OrderModel,Contact

class Index(View):
   def get(self,request, *args, **kwargs):
     return render(request,'customer/index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phno=phno,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your details has successfully added.")
        
    return render (request,'customer/contact.html')

def map_view(request):
    return render(request, 'customer/map.html')

class About(View):
   def get(self,request, *args, **kwargs):
     return render(request,'customer/about.html')

def chinese(request):
  return render(request,'customer/Chinese.html')

def terms(request):
  return render(request,'customer/terms.html')

class Category_Item(View):
   def get(self,request, *args, **kwargs):
     return render(request,'customer/category.html')


class Order(View):
  def get(self, request, *args, **kwargs):
    
    #get every item from each category

    snacks = MenuItem.objects.filter(category__name__contains='Snacks').order_by('name')
    chaat = MenuItem.objects.filter(category__name__contains='Chaat').order_by('name')
    chinese = MenuItem.objects.filter(category__name__contains='Chinese').order_by('name')
    southIndian = MenuItem.objects.filter(category__name__contains='South').order_by('name')
    bread = MenuItem.objects.filter(category__name__contains='Bread').order_by('name')
    northIndian = MenuItem.objects.filter(category__name__contains='North').order_by('name')
    bbq = MenuItem.objects.filter(category__name__contains='Barbecue').order_by('name')
    veg = MenuItem.objects.filter(category__name__contains='Veg').order_by('name')
    sea = MenuItem.objects.filter(category__name__contains='Sea').order_by('name')
    bakery = MenuItem.objects.filter(category__name__contains='Bakery').order_by('name')
    icecream = MenuItem.objects.filter(category__name__contains='IceCream').order_by('name')
    breakfast = MenuItem.objects.filter(category__name__contains='Breakfast').order_by('name')
    italian = MenuItem.objects.filter(category__name__contains='Italian').order_by('name')
    thali = MenuItem.objects.filter(category__name__contains='Thali').order_by('name')
    bengali = MenuItem.objects.filter(category__name__contains='Bengali').order_by('name')
    mughlai = MenuItem.objects.filter(category__name__contains='Mughlai').order_by('name')
    tandoor = MenuItem.objects.filter(category__name__contains='Tandoor').order_by('name')
    desserts = MenuItem.objects.filter(category__name__contains='Dessert').order_by('name')
    drinks = MenuItem.objects.filter(category__name__contains='Drink').order_by('name')

    #pass into context
    context={
    'Snacks': snacks,
    'Chaat': chaat,
    'Chinese':chinese,
    'South':southIndian,
    'North':northIndian,
    'Barbecue':bbq,
    'Veg':veg,
    'Sea':sea,
    'Bakery':bakery,
    'IceCream':icecream,
    'Breakfast':breakfast,
    'Italian':italian,
    'Thali':thali,
    'Bengali':bengali,
    'Mughlai':mughlai,
    'Tandoor':tandoor,
    'Bread':bread,
    'desserts': desserts,
    'drinks': drinks,
    }

    #render the template
    return render( request,'customer/order.html',context)

  def post(self, request, *args, **kwargs):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phoneno = request.POST.get('phno')
    street = request.POST.get('street')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zip_code = request.POST.get('zip')


    order_items = {
      'items': []
    }

    items = request.POST.getlist('items[]')

    for item in items:
      menu_item = MenuItem.objects.get(pk=int(item))
      item_data = {
        'id': menu_item.pk,
        'name': menu_item.name,
        'price': menu_item.price
      }

      order_items['items'].append(item_data)

      price = 0
      item_ids = []

    for item in order_items['items']:
      price += item['price']
      item_ids.append(item['id'])

      order = OrderModel.objects.create(
        price=price,
        name=name,
        email=email,
        phno = phoneno,
        street=street,
        city=city,
        state=state,
        zip_code=zip_code,

        )
      order.items.add(*item_ids)
      #After everything is done ,send confirmation email to the user
      
      body = ('Thank you for your order! your food is being made and will be deliverd soon!\n'
      f'Your Total: {price}\n'
      'Thank you again for your order!')

      send_mail(
        'Thank You For Your Order.',
        body,
        'example@example.com',
        [email],
        fail_silently=False
      )

      context = {
        'items': order_items['items'],
        'price' : price
      }

    return redirect('order-confirmation',pk=order.pk)
class OrderConfirmation(View):
      def get(self,request,pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context={
          'pk' : order.pk,
          'items' : order.items,
          'price' : order.price,
        }
        return render(request, 'customer/order_confirmation.html', context)
      def post(self,request,pk, *args, **kwargs):
        data =json.loads(request.body)
        
        if data['isPaid']:
          order = OrderModel.objects.get(pk=pk)
          order.is_paid = True
          order.save()

        return redirect('payment-confirmation')

class OrderPayConfirmation(View):
  def get(self,request, *args, **kwargs):
    return render(request,'customer/order_pay_confirmation.html')

class Menu(View):
  def get(self,request, *args, **kwargs):
    menu_items = MenuItem.objects.filter().order_by('name')

    context ={
      'menu_items': menu_items
      
    }

    return render(request,'customer/menu.html',context)

class MenuSearch(View):
  def get(self,request, *args, **kwargs):
    query = self.request.GET.get("q")

    menu_items = MenuItem.objects.filter(
      Q(name__icontains=query) |
      Q(price__icontains=query) |
      Q(description__icontains=query)
    )

    context = {
      'menu_items': menu_items
    }

    return render(request, 'customer/menu.html', context)