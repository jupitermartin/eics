from django.views.generic import TemplateView
from module import constant as mcs
from module import  common as mcm

class BaseView(TemplateView):
    def get_metadata(self):
        context = {}
        context['site_title'] = mcs.SITE_TITLE
        context['sendor'] = mcm.get_mail_account(self.request)['email']
        return context

    def get_free_ticket(self):
        all_tickets = mcm.get_all_main_tickets(self.request)
        free_ticket = None
        for ticket in all_tickets:
            if ticket['maint_tickets_task'] != '':
                continue
            free_ticket = ticket
            break

        return free_ticket

    def get_context(self):
        context = {}
        context['meta_info'] = self.get_metadata()
        context['free_ticket'] = self.get_free_ticket()
        context['splice_point_data'] = mcm.get_all_splice_point_data(self.request)
        return context