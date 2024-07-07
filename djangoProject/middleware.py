# green_marketplace/middleware.py
from datetime import datetime, timedelta
from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions.models import Session

class UserHistoryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            if 'last_visit' in request.session:
                last_visit_time = datetime.strptime(request.session['last_visit'], '%Y-%m-%d %H:%M:%S')
                if (datetime.now() - last_visit_time).seconds > 3600:  # Track hourly visits
                    request.session['visits'] = request.session.get('visits', 0) + 1
                    request.session['last_visit'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            else:
                request.session['last_visit'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                request.session['visits'] = 1

def get_active_sessions():
    return Session.objects.filter(expire_date__gte=datetime.now()).count()
