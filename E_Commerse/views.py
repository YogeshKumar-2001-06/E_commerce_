
# views.py
from datetime import timedelta, datetime
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  # If the form is submitted, get the data from POST
        if form.is_valid():  # Check if the form data is valid
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate the user with the provided credentials
            user = authenticate(request, username=username, password=password)
            
            if user is not None:  # If the user exists and credentials are correct
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to the user's profile page after successful login
            else:
                form.add_error(None, "Invalid username or password")  # Show an error if authentication fails
    else:
        form = LoginForm()  # If the request is a GET request, create an empty form
    
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create the user account
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Set the user's password
            user.save()  # Save the user object

            # Optionally, automatically log the user in after they sign up
            login(request, user)

            return redirect('login')  # Redirect to the profile page or another page
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def homepage(request):
    advertisement = Advertisement.objects.all()[:1]  
    categorys = Category.objects.all()
    NewProduct = ProductPost.objects.all()[:5]
    Products = ProductPost.objects.all()
    profile, created = CustomerProfile.objects.get_or_create(user=request.user,Email = request.user.email)
    for product in Products:
        original_price = product.Price
        discount_price = product.Discount_Price

        if original_price > 0:  # To avoid division by zero
            discount_percentage = ((original_price - discount_price) / original_price) * 100
            product.Discount_percentage = discount_percentage
        else:
            product.Discount_percentage = 0
        product.save()          
    cartitems = None
    if request.user.is_authenticated:
        try:
           
            cartitems = Cart.objects.prefetch_related('items__Product').get(Customer=request.user)
        except Cart.DoesNotExist:
            cartitems = None

    return render(request, 'newhome.html', {
        'Advertisement': advertisement,
        'Category': categorys,
        'NewProduct': NewProduct,
        'Products': Products,
        'cartitems': cartitems,
    })

@login_required
def productSearch(request):
    query = request.GET.get('query','')
    
    if query:
        products = ProductPost.objects.filter(Name__icontains=query)
    else:
        products = ProductPost.objects.all()
    
    product_count = products.count()
    
    return render (request , 'productsearch.html',{'products':products,'query':query,'product_count':product_count})

@login_required
def Productpage(request,product_id):
    Product = get_object_or_404(ProductPost,ID = product_id)
    feedbacks = Feedback.objects.filter(product=Product)
    categorys = Category.objects.all()
    related_products = ProductPost.objects.filter(Category=Product.Category).exclude(ID=Product.ID)
    
    if request.method == 'POST':
        feedBack_form = FeedbackForm(request.POST ,prefix='feedback')
        
        if feedBack_form.is_valid():
            feedback_instance = feedBack_form.save(commit=False) 
            feedback_instance.product = Product  
            feedback_instance.save()
        #return redirect('Productpage',product_id=product_id)
    else:
        feedBack_form = FeedbackForm(prefix='feedback')
        
    return render(request,'newproduct.html',{
        'Product':Product,
        'feedBack_form':feedBack_form,
        'feedback':feedbacks,
        'Category': categorys,
        'related_product':related_products
        })

@login_required  
def Categorypage(request, category_id):
    category = get_object_or_404(Category, ID=category_id)
    categorys = Category.objects.all()
    products = ProductPost.objects.filter(Category=category)
    products_count = products.count()
    sort_by = request.GET.get('sort_by', 'name')
    if sort_by == 'price-asc':
        products = ProductPost.objects.filter(Category=category).order_by('Price')
    elif sort_by == 'price-desc':
        products = ProductPost.objects.filter(Category=category).order_by('-Price')
    elif sort_by == 'popularity':
        products = ProductPost.objects.filter(Category=category).order_by('-popularity') 
    else:
        products = ProductPost.objects.filter(Category=category).order_by('Name')  

    return render(request, 'categorysearch.html',
                  {
                   'category': category,
                   'products': products, 
                   'Category': categorys,
                   'product_count':products_count,
                   })
@login_required
def user_profile(request):
    username = request.user.username
    cartdata = None
    cartitems = None
    cart_count = 0
    pending = 0
    delivered = 0
    orders_count = 0
    orders = []  # Initialize orders with a default value
    address = None
    profile = None

    try:
        # Get the user's profile and cart items
        profile = CustomerProfile.objects.get(user=request.user)
        cartitems = Cart.objects.get(Customer=request.user)
        cartdata = CartItem.objects.filter(Cart=cartitems)
        address = Address.objects.filter(Customer=request.user)
        
        # Use the profile to filter orders instead of the User directly
        orders = Order.objects.filter(customer=profile)  # Filter orders using the profile

        for order in orders:
            orders_count += 1
            if order.status == 'Pending':
                pending += 1
            elif order.status == 'Delivered':
                delivered += 1
    except Address.DoesNotExist:
        address = None
    except CustomerProfile.DoesNotExist:
        profile = None
    except Cart.DoesNotExist:
        cartitems = None
        cartdata = []

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = CustomerProfileForm(instance=profile)

    cart_count = cartdata.count() if cartdata else 0

    return render(request, 'newprofile.html', {
        'profile': profile,
        'username': username,
        'cartitems': cartitems,
        'cart_count': cart_count,
        'pending': pending,
        'delivered': delivered,
        'orders': orders,
        'orders_count': orders_count,
        'address': address,
        'form': form,
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(ProductPost, ID=product_id)
    cart, created = Cart.objects.get_or_create(Customer=request.user)
    cart_item, created = CartItem.objects.get_or_create(Cart=cart, Product=product)
    
    if created:
        cart_item.Quantity = 1  # Set initial quantity if item is newly created
    else:
        cart_item.Quantity += 1  # Increment quantity if item already exists
    
    cart_item.save()
    return redirect('home')

@login_required
def remove_cart_item(request, item_id):
    # Fetch the cart item for the logged-in user's cart
    cart_item = get_object_or_404(CartItem, ID=item_id, Cart__Customer=request.user)

    # Delete the cart item
    cart_item.delete()

    # Redirect back to the cart or home page with a success message
    return redirect('home')

@login_required
def orderpage(request, product_id):
    # Fetch the product and profile
    product = get_object_or_404(ProductPost, ID=product_id)
    profile = CustomerProfile.objects.get(user=request.user)
    address = Address.objects.filter(Customer=profile.user)
    
    if request.method == "POST":
        # Fetch the selected address and payment method from the form
        address_id = request.POST.get('address')
        payment_mode = request.POST.get('payment')
        quantity = int(request.POST.get('quantity'))
        order_date = datetime.now()
        delivery_date = order_date+timedelta(days=7)
        shipaddress = Address.objects.get(ID=address_id)
        if product.Stock>=quantity:
            product.Stock-=quantity
            product.save()
        
        # Calculate the total amount (you can update this logic if necessary)
        totalamount = product.Discount_Price*quantity
        print(totalamount)
        
        # Create the order
        order = Order.objects.create(
            customer=profile,
            total_amount=totalamount,
            shipping_address=shipaddress,
            payment=payment_mode,
            delivery_date = delivery_date
        )
        order_item = OrderItem.objects.create(
            order = order,
            product = product,
            quantity = quantity,
            price = totalamount,
        )
        
        # Redirect to the order confirmation page
        return redirect('order_confirm', order_id=order.order_id)
    
    return render(request, 'orderpage.html', {
        'profile': profile,
        'product': product,
        'addres': address,
    })

@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(order_id=order_id)
    orderitem = OrderItem.objects.get(order=order)
    product = ProductPost.objects.get(Name=orderitem.product)
    
    return render(request,'order_confirm.html',{'order':order,'item':orderitem,'product':product})

@login_required
def add_address(request):
    if request.method == 'POST':
        form = addressform(request.POST, prefix='Address')  # Prefix applied here
        if form.is_valid():
            address = form.save(commit=False)  # Do not save yet
            address.Customer = request.user   # Assign logged-in user
            address.save()  # Save to database
            messages.success(request, 'Address added successfully!')
            return redirect('home')  # Replace 'home' with your desired redirect
        else:
            messages.error(request, 'There was an error with your form submission.')
    else:
        form = addressform(prefix='Address')  

    return render(request, 'addaddress.html', {'form': form}) 

@login_required
def vieworders(request):
    profile = CustomerProfile.objects.get(user=request.user)
    try:
        orders = Order.objects.filter(customer=profile)
    except Order.DoesNotExist:
        orders = None  

    return render( request,'vieworders.html',{'profile':profile,'orders':orders})

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def contact(request):
    return render(request,'contact.html')

@login_required
def new_arrival(request):
    product = ProductPost.objects.all()
    product_count = product.count()
    
    return render(request,'productslist.html',{'product':product,'product_count':product_count})    
 