from django.db import models

class MenuItem(models.Model):
    name= models.CharField(max_length=1000,null=False,blank=False)
    description = models.TextField(null=True,blank=False)
    image = models.ImageField(upload_to='menu_image/')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ManyToManyField('Category',related_name='item')

    def __str__(self):
        return self.name

class Category(models.Model):
    name =  models.CharField(max_length = 100)

    def __str__(self):
        return (self.name)

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7,decimal_places = 2)
    items = models.ManyToManyField(
        'MenuItem',related_name='order', blank=True)
    name = models.CharField(max_length=50,blank=True)
    email = models.CharField(max_length=50,blank=True)
    phno = models.CharField(max_length=15,blank=True)
    street = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=15,blank=True)
    state = models.CharField(max_length=15,blank=True)
    zip_code = models.IntegerField(blank=True,null=True)
    paid = models.BooleanField(default = False )
    shipped = models.BooleanField(default = False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=300)
    phno=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self) -> str:
        return self.name
