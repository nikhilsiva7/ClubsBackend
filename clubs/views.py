from django.shortcuts import render,get_object_or_404
from .models import Clubs
from django.contrib.auth.decorators import login_required
from events.models import Events
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClubSerializer
from rest_framework.permissions import IsAuthenticated




@login_required
def clubs(request):
    query = request.GET.get('q')
    if query:
        clubs=Clubs.objects.filter( Q(name__icontains=query))
    else:
        clubs=Clubs.objects.all()

    return render(request,'clubs.html',{"clubs":clubs,"query":query})

@login_required
def club_details(request,pk):
    club=get_object_or_404(Clubs,pk=pk)
    events=Events.objects.filter(club_id=club).order_by('-date')
    return render(request,'club_details.html',{"club":club,"events":events})





class ClubListView(APIView):
    
    def get(self, request):
        clubs = Clubs.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)
