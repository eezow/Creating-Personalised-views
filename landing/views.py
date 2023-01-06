from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from landing.models import User, AppUsage, Transactions
from django.db.models import Q


class LandingEndpoint(APIView):

    permission_classes = (IsAuthenticated,)

    # Endpoint: /landing/
    # Method: GET
    # Access: Private
    def get(self, request):

        # Verify user
        user = get_object_or_404(User, pk=request.user.id)

        # Retrieve past 30 days of transactions
        transactions = Transactions.objects.filter(
            Q(sender=user) | Q(recipient=user)
        ).values('timestamp', 'transaction_type', 'amount', 'status')

        # Calculate amount of time spent in mobile app
        app_usage = AppUsage.objects.filter(
            user=user
        )
        session_hours = sum([
            (i.session_end - i.session_start).total_seconds() / 60.0 / 60.0
            for i in app_usage
        ])

        # Format response
        response = {
            "transactions": transactions,
            "mobile_usage": f"{session_hours:.0f}",
            "first_name": user.first_name
        }
    
        return Response(response)
