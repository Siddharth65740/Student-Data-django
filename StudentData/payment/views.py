
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

    def form_valid(self, form):
        self.object = form.save()
        self.object.admission.Pending_fees=int(self.object.admission.Pending_fees) -  self.object.Amount
        self.object.admission.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())

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

