from django.shortcuts import render, render_to_response, get_object_or_404
from orders.models import OrderItem, Order
from .forms import Order_Create_Form
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def Admin_Order_Detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

def Order_Create(request):

    cart = Cart(request)
    if request.method == 'POST':
        form = Order_Create_Form(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.cupon:
                order.cupon = cart.cupon
                order.discount = cart.cupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render_to_response( 'orders/order/created.html', {'order': order})
    else:
        form = Order_Create_Form()
        return render(request, 'orders/order/create.html', {'cart': cart,
                                                            'form': form})
