from django.db import models
from django.contrib.auth.models import User




#Customer Table
class CustomerProfile(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(null=True,blank=True,max_length=50)
    Last_Name = models.CharField(null=True,blank=True,max_length=50)
    Gender = models.CharField(null=True,blank=True,max_length=10,choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    Email = models.EmailField(null=True,blank=True)
    Phone_Number = models.CharField(blank=True,null=True,max_length=15)
    
    def __str__(self):
        return self.user.username  




# Category Table
class Category(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=225)
    Description = models.TextField(blank=True,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='category_image/')
    
    def __str__(self):
        return self.Name
    
#product Table  
class ProductPost(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=225)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Discount_Price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    Discount_percentage = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    Stock = models.IntegerField()
    Image = models.ImageField(null=True,blank=True,upload_to='product_images/')
    Category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='products')
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Name
# Advertisement Post table
class Advertisement(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=225)
    Slogan = models.TextField()
    Discount = models.IntegerField()
    image = models.ImageField(null=True,blank=True, upload_to='advertisement_images/')
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='advertisement')
    Created_at = models.DateTimeField(auto_now_add=True) 
    End_Date = models.DateTimeField(null=True) 
   
    def __str__(self):
        return self.Title

class Address(models.Model):
    INDIAN_STATES = [ ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CT', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UT', 'Uttarakhand'), ('WB', 'West Bengal'), ] 
    ID = models.AutoField(primary_key=True) 
    Customer = models.ForeignKey(User, on_delete=models.CASCADE) 
    Name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    Address_Line1 = models.CharField(max_length=255) 
    Address_Line2 = models.CharField(max_length=255, blank=True, null=True) 
    City = models.CharField(max_length=200) 
    State = models.CharField(max_length=2, choices=INDIAN_STATES) 
    Zip_Code = models.CharField(max_length=10) 
    Pin_Code = models.CharField(max_length=6)
    
    def __str__(self):
        return f"{self.Address_Line1}, {self.City}, {self.State}, {self.Zip_Code}, {self.Pin_Code}"
class Order(models.Model):
    ORDER_STATUS_CHOICES = [ ('Pending', 'Pending'),
                            ('Shipped', 'Shipped'), 
                            ('Delivered', 'Delivered'), 
                            ('Cancelled', 'Cancelled'), ]
    PAYMENT_MODE_CHOICES = [ 
                            ('Credit Card','Credit Card'), 
                            ('Debit Card', 'Debit Card'),
                            ('PayPal', 'PayPal'), 
                            ('Net Banking', 'Net Banking'), 
                            ('Cash on Delivery', 'Cash on Delivery'),
                            ]
    order_id = models.AutoField(primary_key=True) 
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE) 
    order_date = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending') 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) 
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True) 
    delivery_date = models.DateTimeField(null=True, blank=True)
    payment = models.CharField(max_length=50,choices=PAYMENT_MODE_CHOICES,null=False)

    
    def __str__(self): 
        return f'Order {self.order_id}' 

class OrderItem(models.Model): 
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE) 
    product = models.ForeignKey('ProductPost', on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField() 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    def __str__(self): 
        return f'{self.quantity} of {self.product}'   

# Cart Table
class Cart(models.Model):
    ID = models.AutoField(primary_key=True)
    Customer = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.Customer.username}"

# CartItem Table
class CartItem(models.Model):
    ID = models.AutoField(primary_key=True)
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    Product = models.ForeignKey(ProductPost, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.Quantity} x {self.Product.Name} in Cart"
    
#feed back table
class Feedback(models.Model):
    product = models.ForeignKey('ProductPost', on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')])
    comment = models.TextField(blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return f'{self.name} - {self.rating} Stars'
    
