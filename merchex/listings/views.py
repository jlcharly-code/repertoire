from django.shortcuts import render, get_object_or_404
from listings.models import Band
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm, ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(
        request,
        'listings/band_list.html',
        {'bands': bands}
    )

def band_detail(request, id):
    # Fetch the specific band or return a 404 error if not found
    band = get_object_or_404(Band, pk=id)
    return render(
        request,
        'listings/band_detail.html',
        {'band': band}
    )

def about(request):
    return HttpResponse('<h1>Répertoire</h1> <p>Groupes et chanteurs </p>')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['jlcharly@gmail.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def band_create(request):
    if request.method == 'POST':
       form = BandForm(request.POST)
       if form.is_valid():
            # create a new `Band` and save it to the db
            band = form.save()
            return redirect('band-detail', band.id)
        
    else:
        form = BandForm()

    return render(request,
                'listings/band_create.html',
                {'form': form})

def band_update(request, id):
    band = get_object_or_404(Band, pk=id)  

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})