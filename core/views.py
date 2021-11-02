from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


def home(reqest):
    Bros = Message.objects.filter(msg='Bro!').count()
    Siss = Message.objects.filter(msg='Sis!').count()
    return render(reqest, 'core/index.html', {
        'title': 'Login',
        'bros': Bros,
        'siss': Siss
    })


def app(request):
    lastmsg = Message.objects.order_by('-id')[:1]
    Bros = Message.objects.filter(msg='Bro!').count()
    Siss = Message.objects.filter(msg='Sis!').count()

    form = MessageForm()
    context = {
        'title': 'App',
        'lastmsg': lastmsg,
        'form': form,
        'bros': Bros,
        'siss': Siss
    }
    if request.user.is_authenticated:
        if request.method == "POST":
            form = MessageForm(request.POST)
            form.instance.username = request.user
            form.instance.msg = request.POST.get('msg')
            form.save()
            return redirect('app')

        return render(request, 'core/app.html', context)
    else:
        return redirect('home')