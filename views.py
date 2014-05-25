# coding=utf-8
from django.views.generic import (
    TemplateView, DetailView
)
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect

from braces.views import LoginRequiredMixin

