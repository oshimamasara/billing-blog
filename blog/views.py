from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Sell
import stripe
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
def about(request):
    return HttpResponse('このブログサイトについて....')

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'post':post})

def index(request):
    posts = Post.objects.order_by('-created_datetime')
    return render(request, 'blog/index.html',{'posts':posts})

def fee_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    blog_price = post.price
    #stripe
    stripe.api_key = 'sk_test_L3ocIJYmmqbktHeyfNh9t9I600OpJsBvke'

    if request.method == "POST":
        try:
            user_email = request.POST['input_mail']
            #amount = 110   # amount in cents
            amount = blog_price
            customer = stripe.Customer.create(
                email = user_email,
                #email="customer@gamil.com",
                source=request.POST['stripeToken']
            )
            print("stripe.Customer.create()     OK!")

            paied = stripe.Charge.create(
                customer=customer.id,
                amount=amount,
                currency='jpy',
                description='ブログのdjangoでStripe中....',
                receipt_email=user_email,
            )
            print("stripe.Charge.create()     OK!")

            # SAVA DATABASE
            #print(paied)
            #print(paied.keys())
            #print(paied["status"])
            if paied["status"]=="succeeded":
                sells_data = Sell()
                sells_data.sold_blog = post
                sells_data.customer_mail = user_email
                sells_data.Date = timezone.now()
                sells_data.price = amount
                sells_data.save()
                return render(request, 'blog/paid_detail.html', {'post': post})
            else:
                # カード決済失敗時、決済付き画面に
                return render(request, 'blog/pay_error_detail.html', {'post': post})

                #return render(request, 'blog/paid_detail.html', {'post': post})
                #return HttpResponse("django blog で Stripe決済完了！")

        except stripe.error.StripeError:
            print("error......")

    else:
        sample_text = "Stripe上手くいくかな....."

    return render(request, 'blog/fee_detail.html', {'post': post})

    # first code
    #post = get_object_or_404(Post, slug=slug)
    #return render(request, 'blog/fee_detail.html', {'post':post})

