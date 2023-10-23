import pytest
from django.test import Client
from django.urls import reverse
from crmModule.models import Event
from crmModule.models import Sponsor_Event


@pytest.mark.django_db
def test_register_event():
    # Configura el cliente de prueba de Django
    client = Client()

    # Define los datos de prueba
    data = {
        'name': 'Evento de Ejemplo',
        'date': '2023-11-15',
        'event_Type': 'F',  # Puedes usar 'F' para FLORECIMIENTO o 'O' para ORGANIZACIONAL
        'sponsor_name': 'Sponsor de Prueba',
        'participation': 'Patrocinio Platino'
    }

    # Realiza una solicitud POST a la vista register_event
    response = client.post(reverse('register_event'), data, follow=True)

    # Verifica que la solicitud se haya procesado correctamente (código de estado 200)
 

    # Aquí puedes realizar más afirmaciones para verificar el comportamiento de la vista

    # Por ejemplo, puedes verificar si se ha creado el evento y su relación con el patrocinador

    # Verifica que el evento se haya creado correctamente
    assert Event.objects.filter(name=data['name']).exists()

    # Verifica que la relación con Sponsor_Event se haya establecido correctamente
    assert Sponsor_Event.objects.filter(Sponsor_id__name=data['sponsor_name'], participation=data['participation']).exists()