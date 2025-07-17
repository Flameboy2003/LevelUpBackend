from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Poll, Vote
from .serializers import PollSerializer, VoteSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def create_poll(request):
    serializer = PollSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Poll created successfully'})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_polls(request):
    polls = Poll.objects.all().order_by('-created_at')
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def save_vote(request):
    email = request.data.get("email")
    poll_id = request.data.get("poll_id")
    selected_options = request.data.get("selected_options", [])

    if not all([email, poll_id]):
        return Response({"error": "Missing required fields"}, status=400)

    vote, created = Vote.objects.get_or_create(
        user=email,
        poll_id=poll_id,
        defaults={"selected_options": selected_options}
    )

    if not created:
        vote.selected_options = selected_options
        vote.save()

    return Response({"success": True})
