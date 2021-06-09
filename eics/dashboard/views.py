from django.shortcuts import render
from django.views.generic import TemplateView
from module import views as bsv
from module import common as mcm
from module import constant as mcs
from datetime import datetime
from django.http import HttpResponse
from cudb.models import *
import json
from django.db import transaction

# Create your views here.
class WelcomeView(bsv.BaseView):
    template_name = 'dashboard/index.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['meta_info'] = self.get_metadata()
        context['header_title'] = 'Maintenance Ticket Menu'
        return context


class Create_planned_maintenance(bsv.BaseView):
    template_name = 'dashboard/create_planned_maintenance.html'
    def get_context_data(self, **kwargs):
        context = self.get_context()
        context['header_title'] = 'Planned Maintenance Ticket Entry Form'
        return context

class Update_planned_maintenance(bsv.BaseView):
    template_name = 'dashboard/update_planned_maintenance.html'
    def get_context_data(self, **kwargs):
        context = self.get_context()
        context['header_title'] = 'Planned Maintenance Ticket Entry Form'
        return context

class Create_reactive_maintenance(bsv.BaseView):
    template_name = 'dashboard/create_reactive_maintenance.html'
    def get_context_data(self, **kwargs):
        context = self.get_context()
        context['header_title'] = 'Reactive Maintenance Ticket Entry Form'
        return context

class Update_reactive_maintenance(bsv.BaseView):
    template_name = 'dashboard/update_reactive_maintenance.html'

    def get_context_data(self, **kwargs):
        context = self.get_context()
        context['header_title'] = 'Reactive Maintenance Ticket Entry Form'
        return context

class Maintain_splice_circuit(bsv.BaseView):
    template_name = 'dashboard/maintain_splice_circuit.html'
    def get_context_data(self, **kwargs):
        context = self.get_context()
        context['header_title'] = 'Maintain Splice and Circuit Data'

def submit_form(request):
    try:
        param = request.POST
        with transaction.atomic():
            new_param = {}
            new_param['to_addresses'] = param['to_addresses']
            new_param['cc_addresses'] = param['cc_addresses']
            new_param['ticketid'] = param['ticket']
            new_param['reason'] = param['reason']
            new_param['priority'] = param['priority']
            new_param['start_date'] = datetime.strptime(param['start_date'], '%d/%m/%Y %H:%M')
            new_param['end_date'] = datetime.strptime(param['end_date'], '%d/%m/%Y %H:%M')
            new_param['duration'] = get_duration(param['duration'])
            new_param['splice_num'] = param['splice_num']
            new_param['location'] = param['location']
            new_param['north'] = param['north']
            new_param['west'] = param['west']
            new_param['circuits'] = param['circuit_ids']
            new_param['status'] = mcs.COMPLETED
            obj = Ticket_task(**new_param)
            obj.save()

            new_param_ = {}
            new_param_['maint_tickets_task'] = 'enter task'
            obj = mcm.get_ticket_by_id(request, param['ticket'])
            for key, value in new_param_.items():
                setattr(obj, key, value)
            obj.save()

        res = mcm.send_email_status_update(request, new_param)
        if res == -1:
            return HttpResponse('emailerror')

        return HttpResponse('success')
    except:
        return HttpResponse('error')

def up_submit_form(request):
    try:
        param = request.POST
        with transaction.atomic():
            new_param = {}
            new_param['to_addresses'] = param['to_addresses']
            new_param['cc_addresses'] = param['cc_addresses']
            new_param['ticketid'] = param['ticket']
            new_param['reason'] = param['reason']
            new_param['priority'] = param['priority']
            new_param['start_date'] = datetime.strptime(param['start_date'], '%d/%m/%Y %H:%M')
            new_param['end_date'] = datetime.strptime(param['end_date'], '%d/%m/%Y %H:%M')
            new_param['duration'] = get_duration(param['duration'])
            new_param['splice_num'] = param['splice_num']
            new_param['location'] = param['location']
            new_param['north'] = param['north']
            new_param['west'] = param['west']
            new_param['circuits'] = param['circuit_ids']
            new_param['status'] = int(param['tk_status'])
            obj = Ticket_task(**new_param)
            obj.save()

            new_param_ = {}
            new_param_['maint_tickets_task'] = 'enter task'
            obj = mcm.get_ticket_by_id(request, param['ticket'])
            for key, value in new_param_.items():
                setattr(obj, key, value)
            obj.save()

        res = mcm.send_email_status_update(request, new_param)
        if res == -1:
            return HttpResponse('emailerror')

        return HttpResponse('success')
    except:
        return HttpResponse('error')

def cr_submit_form(request):
    try:
        param = request.POST
        with transaction.atomic():
            new_param = {}
            new_param['to_addresses'] = param['to_addresses']
            new_param['cc_addresses'] = param['cc_addresses']
            new_param['ticketid'] = param['ticket']
            new_param['reason'] = param['issue']
            new_param['priority'] = param['priority']
            new_param['start_date'] = datetime.strptime(param['start_date'], '%d/%m/%Y %H:%M')
            new_param['splice_num'] = param['splice_num']
            new_param['location'] = param['location']
            new_param['north'] = param['north']
            new_param['west'] = param['west']
            new_param['circuits'] = param['circuit_ids']
            new_param['status'] = mcs.NEW
            obj = Ticket_task(**new_param)
            obj.save()

            new_param_ = {}
            new_param_['maint_tickets_task'] = 'enter task'
            obj = mcm.get_ticket_by_id(request, param['ticket'])
            for key, value in new_param_.items():
                setattr(obj, key, value)
            obj.save()

        res = mcm.send_email_status_update(request, new_param)
        if res == -1:
            return HttpResponse('emailerror')

        return HttpResponse('success')
    except Exception as e:
        return HttpResponse('error')

def ur_submit_form(request):
    try:
        param = request.POST
        with transaction.atomic():
            new_param = {}
            new_param['to_addresses'] = param['to_addresses']
            new_param['cc_addresses'] = param['cc_addresses']
            new_param['ticketid'] = param['ticket']
            new_param['reason'] = param['issue']
            new_param['priority'] = param['priority']
            new_param['start_date'] = datetime.strptime(param['start_date'], '%d/%m/%Y %H:%M')
            new_param['end_date'] = datetime.strptime(param['end_date'], '%d/%m/%Y %H:%M')
            new_param['duration'] = get_duration(param['duration'])
            new_param['splice_num'] = param['splice_num']
            new_param['location'] = param['location']
            new_param['north'] = param['north']
            new_param['west'] = param['west']
            new_param['circuits'] = param['circuit_ids']
            new_param['status'] = mcs.COMPLETED
            obj = Ticket_task(**new_param)
            obj.save()

            new_param_ = {}
            new_param_['maint_tickets_task'] = 'enter task'
            obj = mcm.get_ticket_by_id(request, param['ticket'])
            for key, value in new_param_.items():
                setattr(obj, key, value)
            obj.save()

        res = mcm.send_email_status_update(request, new_param)
        if res == -1:
            return HttpResponse('emailerror')

        return HttpResponse('success')
    except:
        return HttpResponse('error')

def get_duration(duration_str):
    try:
        res = duration_str.split(':')
        return int(res[0]) * 60 + int(res[1])
    except:
        return 0


def calc_duration(request):
    param = request.POST
    start_date_ = param['start_date']
    end_date_ = param['end_date']
    try:
        start_date = datetime.strptime(start_date_, "%d/%m/%Y %H:%M")
        end_date = datetime.strptime(end_date_, '%d/%m/%Y %H:%M')
    except:
        return HttpResponse('timeformaterror')

    time_delta = (end_date - start_date).total_seconds()
    if time_delta < 0:
        return HttpResponse('timeformaterror')
    hours = time_delta // 3600
    mins = (time_delta % 3600) // 60
    res = {'hours': hours, 'mins': mins}
    return HttpResponse(json.dumps(res))

def auto_load_extra(request):
    param = request.POST
    splice_num = param['splice_num']
    splice_point_data = mcm.get_all_splice_point_data(request)
    res = {}
    sl_item = None
    for item in splice_point_data:
        if splice_num == item['splice_pt']:
            sl_item = item
    if sl_item != None:
        res['north'] = sl_item['north']
        res['west'] = sl_item['west']
        res['address'] = sl_item['address']

    splice_to_fibre_data = mcm.get_all_splicetofibre(request)
    DF_numbers = []
    for item in splice_to_fibre_data:
        if splice_num + ' ' in item['splice']:
            DF_numbers.append(item['fibre'])

    DF_numbers_ = list(dict.fromkeys(DF_numbers))
    res['circuits'] = DF_numbers_
    return render(request, 'dashboard/auto_load.html', res)