from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Registration
from twilio.rest import Client

def send_whatsapp_message(name, district, qualification, whatsapp_number, occupation, preferred_exam):
    # Your Twilio Account SID and Auth Token
    account_sid = 'ACab062dc9af2ad20f3e2897945f46e973'
    auth_token = '34c874eb4040a7eeda8fd92b1ceb0f2c'
    client = Client(account_sid, auth_token)

    # WhatsApp number to send the message
    to_whatsapp_number = 'whatsapp:+919360540264'  # Replace with your number

    # Compose the message
    message = f"New Registration:\nName: {name}\nDistrict: {district}\nQualification: {qualification}\nWhatsApp Number: {whatsapp_number}\nOccupation: {occupation}\nPreferred Exam: {preferred_exam}"

    # Send the message
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',  # Twilio sandbox number
        to=to_whatsapp_number,
    )

    print(message.sid)

def index(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        district = request.POST.get('district')
        qualification = request.POST.get('qualification')
        whatsapp_number = request.POST.get('whatsapp_number')
        occupation = request.POST.get('occupation')
        preferred_exam = request.POST.get('preferred_exam')

        # Create a new Registration object and save it to the database
        Registration.objects.create(
            name=name,
            district=district,
            qualification=qualification,
            whatsapp_number=whatsapp_number,
            occupation=occupation,
            preferred_exam=preferred_exam,
        )

        # Send WhatsApp message
        send_whatsapp_message(name, district, qualification, whatsapp_number, occupation, preferred_exam)

        # Redirect or add any additional logic as needed
        return HttpResponseRedirect('/success')  # Redirect to a success page

    return render(request, 'main/index.html')

def success_view(request):
    # Your success view code, e.g., render a success template
    return render(request, 'main/success.html')