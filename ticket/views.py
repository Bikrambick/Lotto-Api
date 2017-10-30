from django.shortcuts import render
from .models import Ticket

# Create your views here.
def createTicket(request):

    ticket = Ticket(
    name = 'adolfo', 
    numbers='1, 22, 31, 23',
    draw = 'asdasdasd' 
    )

    ticket.save()

    return render(request, '../templates/ticket_generator.html', { ticket: ticket})