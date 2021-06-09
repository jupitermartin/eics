from django.conf import settings
import tempfile, os
import json
from django.template.loader import get_template
from dashboard.models import *
from cudb.models import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import threading
import smtplib
from icalendar import Calendar, vDatetime, vCalAddress, vText
from datetime import datetime
import json
import logging
from module import constant as mcs

def get_all_splice_point_data(request):
    data = list(SplicePointData.objects.all().values("section", "splice_pt", "step_chamber_id", "address", "north", "west"))
    return data

def get_all_main_tickets(request):
    data = list(MaintTickets.objects.all().values())
    return data

def get_all_splicetofibre(request):
    data = list(SpliceToFibre.objects.all().values())
    return data

def get_ticket_by_id(request, id):
    obj = MaintTickets.objects.get(pk=id)
    return obj

def get_mail_account(request):
    if not mcs.EMAIL_DEBUG_MODE:
        mail_account = {}
        mail_account['email'] = "kirchenewilov@gmail.com"
        mail_account["password"] = "xx"
        return mail_account
    else:
        mail_account = {}
        mail_account['email'] = "info@steptelecoms.ie"
        mail_account["password"] = "xx"
        return mail_account

def send_email_status_update(request, param):
    try:
        ics_flag = 0
        try:
            cal = Calendar()

            cal.add('uid', vDatetime(datetime.now()).to_ical().decode() + " -maintenance-" + param['ticketid'] + "-0@steptelecom.ie")
            cal.add('sequence', 0)
            cal['dtstamp'] = vDatetime(datetime.now())
            cal['X-MAINTNOTE-PROVIDER'] = vText('steptelecom.ie')

            organizer = vCalAddress('MAILTO:Mary.McCabe@steptelecoms.ie')
            organizer.params['cn'] = vText('StepTelecom')
            cal['X-MAINTNOTE-ORGANISER'] = organizer

            cal['X-MAINTNOTE-MAINTENANCE-ID'] = vText('maintenance-' + param['ticketid'])
            cal['summary'] = vText('Splicing new fibre in live Fibre Joints, Risk classification:' + param['priority'])
            cal['dtstart'] = vDatetime(param['start_date'])
            cal['dtend'] = vDatetime(param['end_date'])
            cal['X-MAINTNOTE-IMPACT'] = vText('OUTAGE')
            cal['X-MAINTNOTE-STATUS'] = vText('TENTATIVE')

            res = []
            res.append(param['splice_num'])
            res.append(param['splice_num'] + ' ' + param['location'] + ' ' + param['north'] + ' ' + param['west'])
            circuits_list = json.loads(param['circuits'])
            for item in circuits_list:
                res.append(item)

            cal.add('X-MAINTNOTE-ODJECT-ID', res)

            ics_directory = os.path.join(settings.BASE_DIR, 'ics')
            file_name = param['ticketid'] + '.ics'
            f = open(os.path.join(ics_directory, file_name), 'wb')
            f.write(cal.to_ical())
            f.close()
            ics_flag = 1
        except:
            pass

        if 1:
            to_addresses = get_email_addresses(param['to_addresses'])
            cc_addresses = ''
            if param['cc_addresses'] != '':
                cc_addresses = get_email_addresses(param['cc_addresses'])
            ticket = param['ticketid']
            msg = MIMEMultipart("alternative")
            msg["from"] = get_mail_account(request)["email"]
            msg["to"] = to_addresses
            if cc_addresses != '':
                msg["cc"] = cc_addresses
            msg["Subject"] = 'Step Telecoms Ltd Scheduled Maintenance: Multiple Circuits Dublin Network STMT19081'

            param['circuits_list'] = json.loads(param['circuits'])

            html = render_email(param, "dashboard/email.html")
            part1 = MIMEText(html, 'html')
            if ics_flag:
                with open(os.path.join(ics_directory, file_name), "rb") as fil:
                    part = MIMEApplication(
                        fil.read(),
                        Name=file_name
                    )
                # After the file is closed
                part['Content-Disposition'] = 'attachment; filename="%s"' % file_name
                msg.attach(part)

            msg.attach(part1)
            th = threading.Thread(target=send_email_status_update_thread, args=(request, msg, ticket))
            th.start()
        return 1
    except Exception as e:
        return -1

def send_email_status_update_thread(request, msg, ticket):
    res = send_email(request, msg)
    if res == -1:
        return res
    update_email_sent(ticket)

def send_email(request, msg):
    mail_account = get_mail_account(request)
    try:
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.login(mail_account["email"], mail_account["password"])
        s.send_message(msg)
        return 1
    except Exception as e:
        return -1

def update_email_sent(ticket):
    obj = Ticket_task.objects.get(pk=ticket)
    new_param = {}
    new_param['email_sent'] = True
    for key, value in new_param.items():
        setattr(obj, key, value)
    obj.save()

def render_email(context, template_path):
    template = get_template(template_path)
    html = template.render(context)
    return html

def get_email_addresses(addrs):
    new_addr = addrs if addrs[len(addrs)-1] != ';' else addrs[:-1]
    return ', '.join(new_addr.split(';'))