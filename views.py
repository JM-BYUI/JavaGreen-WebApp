import math
import io
import random
from django.shortcuts import render
from pypdf import PdfReader, PdfWriter
from professions import PROFESSIONS
from bonus import BONUS

def generate_agent(request):
    if request.method == "POST":
        name = request.POST.get("agent_name", "").strip()
        profession = request.POST.get("profession")

        # ERROR CHECKING:
        if len(name) < 2:
            return render(request, "creator.html", {"error": "Agent name is too short!"})
        if not profession:
            return render(request, "creator.html", {"error": "You must select a profession."})