from django.shortcuts import render, redirect
from django.views.generic import View

from . import models
from apps.threads.forms import ThreadForm

# class Thread(View):