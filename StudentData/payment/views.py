from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import payment_info
from django.forms import MultiWidget
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.

class create_view(LoginRequiredMixin,CreateView):
    model = payment_info
    fields = '__all__'

    '''def form_valid(self, form):
        self.object = form.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        self.admission.Pending_fees = self.admission.Pending_fees - self.Amount
        return HttpResponseRedirect(self.get_success_url())
    '''
    '''def form_valid(self, form):
        response = super(create_view, self).form_valid(form)
        # do something with self.object
        self.admission.Pending_fees=self.admission.Pending_fees-self.Amount
        return response
    '''

class paymentListView(LoginRequiredMixin,ListView):
    model= payment_info
    fields ="__all__"
    context_object_name = "payment_list"

class paymentUpdateView(LoginRequiredMixin,UpdateView):
    model = payment_info
    fields = '__all__'

class detail_payment(LoginRequiredMixin,DetailView):
    model = payment_info
    template_name = 'payment/invoice_print.html'


class delete_payment(LoginRequiredMixin,DeleteView):
    model = payment_info
    success_url = '/payment/list'


#def student_payment(request,admision_id):
#    return redirect('payment-create',**kwargs={''})

