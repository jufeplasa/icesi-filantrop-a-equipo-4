import factory
from crmModule.models import Official, Event, Sponsor,Sponsor_Event



class sponsorFactory(factory.Factory):
    class Meta:
        model = Sponsor
    
    name = "Carvajal"
    personType = "J"
    contact_number="315471353"
    email = "Carv@gmail.com"
    previousColab = "True"

class eventFactory(factory.Factory):
    class Meta:
        model = Event
    name = "Almuerzo Manuelita"
    date = "20230218"
    time = "13:00"
    event_Type = "F"

        

