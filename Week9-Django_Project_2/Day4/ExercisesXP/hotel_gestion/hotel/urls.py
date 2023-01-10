from django.urls import path
from hotel.views import homepage,add_avis,reservation,voir_avis,ma_reservation,editer_reservation,editer_chambre,all_reservation,suprimer_avis,message,modifier_message,mes_messages,suprimer_message,suprimer_reservation,lesmessages


urlpatterns = [
path('',homepage,name='homepage'),
path('addAvis',add_avis,name='addAvis'),
path('reservation',reservation,name='reservation'),
path('avis',voir_avis,name='voir_avis'),
path('ma_reservation/<int:user_id>',ma_reservation,name='ma_reservation'),
path('reservation/<int:reservation_id>',editer_reservation,name="editer_Reservation"),
path('chambre/<int:id>',editer_chambre,name='editer_chambre'),
path('reservations',all_reservation,name='all_reservation'),
path('suprimer/<int:avis_id>',suprimer_avis,name='suprimer_avis'),
path('message',message,name='envoyer_message'),
path('mes_messages/<int:user_id>',mes_messages,name='mes_messages'),
path('modifier_message/<int:message_id>',modifier_message,name='modifier_message'),
path('suprimer_message/<int:message_id>',suprimer_message,name='suprimer_message'),
path('suprimer_reservation/<int:reservationId>',suprimer_reservation,name='suprimer_reservation'),
path('messages',lesmessages,name='messages'),

]