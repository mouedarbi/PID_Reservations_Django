from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from catalogue.models import *
from django.http import JsonResponse
from datetime import datetime, timedelta
from decimal import Decimal


class AdminDashboardView(TemplateView):
    template_name = 'admin/index.html'
    
    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Données pour le tableau de bord
        context['total_reservations'] = Reservation.objects.count()
        context['total_revenue'] = self.calculate_total_revenue()
        context['revenue_growth'] = self.calculate_revenue_growth()
        context['total_tickets_sold'] = self.calculate_total_tickets_sold()
        context['tickets_growth'] = self.calculate_tickets_growth()
        context['tickets_today'] = self.calculate_tickets_today()
        context['active_shows'] = Show.objects.filter(bookable=True).count()
        context['upcoming_shows'] = self.get_upcoming_shows_count()
        context['total_customers'] = self.get_total_customers()
        context['new_customers_month'] = self.get_new_customers_this_month()
        context['customers_growth'] = self.calculate_customers_growth()
        context['conversion_rate'] = self.calculate_conversion_rate()
        context['conversion_growth'] = self.calculate_conversion_growth()
        context['remaining_conversion'] = 100 - context['conversion_rate']
        context['activity_data'] = self.get_activity_data()
        context['revenue_data'] = self.get_revenue_data()
        context['tickets_data'] = self.get_tickets_data()
        context['top_shows'] = self.get_top_shows()
        context['recent_activities'] = self.get_recent_activities()
        context['upcoming_shows_list'] = self.get_upcoming_shows_list()
        
        return context
    
    def calculate_total_revenue(self):
        # Calculer le revenu total à partir des réservations
        representations_reservations = RepresentationReservation.objects.all()
        total = sum(rr.quantity * float(rr.price.price) for rr in representations_reservations)
        return round(total, 2)
    
    def calculate_revenue_growth(self):
        # Calculer la croissance du revenu (simplifié)
        return 12.5  # Valeur factice pour l'instant
    
    def calculate_total_tickets_sold(self):
        # Calculer le nombre total de billets vendus
        representations_reservations = RepresentationReservation.objects.all()
        return sum(rr.quantity for rr in representations_reservations)
    
    def calculate_tickets_growth(self):
        # Calculer la croissance des billets vendus (simplifié)
        return 8.2  # Valeur factice pour l'instant
    
    def calculate_tickets_today(self):
        # Calculer les billets vendus aujourd'hui
        today = datetime.now().date()
        representations_reservations = RepresentationReservation.objects.filter(
            reservation__booking_date__date=today
        )
        return sum(rr.quantity for rr in representations_reservations)
    
    def get_upcoming_shows_count(self):
        # Obtenir le nombre de spectacles à venir
        now = datetime.now()
        return Representation.objects.filter(schedule__gte=now).count()
    
    def get_total_customers(self):
        # Obtenir le nombre total de clients
        return Reservation.objects.values('user').distinct().count()
    
    def get_new_customers_this_month(self):
        # Obtenir le nombre de nouveaux clients ce mois-ci
        start_of_month = datetime.now().replace(day=1)
        return Reservation.objects.filter(
            booking_date__gte=start_of_month
        ).values('user').distinct().count()
    
    def calculate_customers_growth(self):
        # Calculer la croissance des clients (simplifié)
        return 15.3  # Valeur factice pour l'instant
    
    def calculate_conversion_rate(self):
        # Calculer le taux de conversion (simplifié)
        return 73.5  # Valeur factice pour l'instant
    
    def calculate_conversion_growth(self):
        # Calculer la croissance du taux de conversion (simplifié)
        return 2.3  # Valeur factice pour l'instant
    
    def get_activity_data(self):
        # Données pour le graphique d'activité (simplifié)
        return [65, 59, 80, 81, 56, 55, 40]
    
    def get_revenue_data(self):
        # Données pour le graphique de revenus (simplifié)
        return [4000, 6000, 8000, 7000]
    
    def get_tickets_data(self):
        # Données pour le graphique des billets (simplifié)
        return [120, 180, 250, 200]
    
    def get_top_shows(self):
        # Obtenir les meilleurs spectacles (simplifié)
        shows = Show.objects.all()[:3]  # Prendre les 3 premiers
        top_shows = []
        for show in shows:
            # Simuler des données pour l'affichage
            top_shows.append({
                'title': show.title,
                'tickets_sold': 789 if show.id == 1 else (892 if show.id == 2 else 456),
                'capacity': 1200 if show.id == 1 else (1000 if show.id == 2 else 800),
                'revenue': '35K' if show.id == 1 else ('44K' if show.id == 2 else '18K')
            })
        return top_shows
    
    def get_recent_activities(self):
        # Obtenir les activités récentes (simplifié)
        return [
            {
                'title': 'Nouvel achat de billet',
                'description': 'Sarah Johnson a acheté 2 billets VIP',
                'timestamp': datetime.now() - timedelta(minutes=2),
                'status': 'done'
            },
            {
                'title': 'Événement publié',
                'description': 'Carnaval de la nourriture 2025 est en ligne',
                'timestamp': datetime.now() - timedelta(minutes=15),
                'status': 'info'
            },
            {
                'title': 'Avertissement de capacité',
                'description': 'Sommet technologique est rempli à 89%',
                'timestamp': datetime.now() - timedelta(hours=1),
                'status': 'warning'
            },
            {
                'title': 'Paiement traité',
                'description': 'Paiement de 2150€ complété',
                'timestamp': datetime.now() - timedelta(hours=2),
                'status': 'done'
            },
            {
                'title': 'Remboursement demandé',
                'description': 'Commande #12342 nécessite une révision',
                'timestamp': datetime.now() - timedelta(hours=3),
                'status': 'error'
            }
        ]
    
    def get_upcoming_shows_list(self):
        # Obtenir la liste des spectacles à venir (simplifié)
        representations = Representation.objects.filter(
            schedule__gte=datetime.now()
        )[:4]  # Prendre les 4 prochains
        
        upcoming_shows = []
        for rep in representations:
            sold_percentage = int((rep.show.representations.count() / 1200) * 100) if hasattr(rep.show, 'representations') else 65
            upcoming_shows.append({
                'title': rep.show.title,
                'date': rep.schedule.date(),
                'time': rep.schedule.time(),
                'tickets_sold': 789 if rep.id == 1 else (456 if rep.id == 2 else (234 if rep.id == 3 else 0)),
                'capacity': 1200 if rep.id == 1 else (800 if rep.id == 2 else (500 if rep.id == 3 else 1500)),
                'sold_percentage': sold_percentage
            })
        return upcoming_shows


# Vue pour la page principale de l'admin
@login_required
def admin_home(request):
    if not request.user.is_staff:
        return redirect('admin:login')
    
    # Données pour le tableau de bord
    total_reservations = Reservation.objects.count()
    total_revenue = 0  # À calculer selon votre logique
    
    # Calculer le revenu total
    representations_reservations = RepresentationReservation.objects.all()
    for rr in representations_reservations:
        total_revenue += rr.quantity * float(rr.price.price)
    
    context = {
        'total_reservations': total_reservations,
        'total_revenue': round(total_revenue, 2),
        'revenue_growth': 12.5,
        'total_tickets_sold': sum(rr.quantity for rr in representations_reservations),
        'tickets_growth': 8.2,
        'tickets_today': sum(
            rr.quantity for rr in representations_reservations 
            if rr.reservation.booking_date.date() == datetime.now().date()
        ),
        'active_shows': Show.objects.filter(bookable=True).count(),
        'upcoming_shows': Representation.objects.filter(
            schedule__gte=datetime.now()
        ).count(),
    }
    
    return render(request, 'admin/index.html', context)