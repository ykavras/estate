from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Panorama, Screen, HotSpot


class IsAutheticatePermissionMixin:
    def has_permission(self):
        return self.request.user.is_authenticated


class PanoramaCreate(IsAutheticatePermissionMixin, PermissionRequiredMixin, CreateView):
    template_name = 'panorama-create.html'
    model = Panorama
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('screen:panorama-detail', kwargs={'pk': self.object.pk})


class PanoramaUpdate(IsAutheticatePermissionMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'panorama-update.html'
    model = Panorama
    fields = '__all__'


class PanoramaDelete(IsAutheticatePermissionMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'panorama-delete.html'
    model = Panorama
    success_url = reverse_lazy('screen:panorama-list')


class PanoramaList(IsAutheticatePermissionMixin, PermissionRequiredMixin, ListView):
    template_name = 'panorama-list.html'
    model = Panorama


class PanoramaDetail(IsAutheticatePermissionMixin, PermissionRequiredMixin, DetailView):
    template_name = 'panorama-detail.html'
    model = Panorama
