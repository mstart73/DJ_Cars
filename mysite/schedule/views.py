from django.shortcuts import render
from django.http import HttpResponse

from django.utils.timezone import now
from datetime import datetime
from datetime import timedelta
from .models import Schedule

from django.utils import timezone
from django.template import loader

from django.contrib.auth.decorators import login_required

from django.urls import reverse



def getmydate(daty, l):
    try:
        return datetime(daty[l][0], daty[l][1], daty[l][2])
    except:
        return l


def show_types(request):
    return HttpResponse("Hello, world. You're at the cars index.")


@login_required
def new_reservation(request):
    context=locals()

    return render( request,'new_reservation_form.html',context)


def show_schedule(request, dt=now().strftime('%Y-%m-%d %H:%M:%S')):





    # print("dt1",dt,type(dt))
    vins = {}
    vin_line = {}
    idcar = 0
    if type(dt) is str:
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')

    now_m_plus = (dt + timedelta(days=31)).strftime('%Y-%m-%d %H:%M:%S')
    now_w_plus = (dt + timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')

    now_m_minus = (dt + timedelta(days=-31)).strftime('%Y-%m-%d %H:%M:%S')
    now_w_minus = (dt + timedelta(days=-7)).strftime('%Y-%m-%d %H:%M:%S')

    dtt = {'now_m_minus': now_m_minus, 'now_w_minus': now_w_minus, 'now_w_plus': now_w_plus, 'now_m_plus': now_m_plus}

    #  print("dt2", dt,type(dt))
    # range of dates i scheduler -3 from now + 31
    # dt = datetime.datetime.now()
    daty = [((dt + timedelta(days=n)).year, \
             (dt + timedelta(days=n)).month, \
             (dt + timedelta(days=n)).day, \
             ) for n in range(-3, 31)]

    # min and max date
    dtmin = datetime(daty[0][0], daty[0][1], daty[0][2], tzinfo=timezone.get_current_timezone())
    dtmax = datetime(daty[-1][0], daty[-1][1], daty[-1][2], tzinfo=timezone.get_current_timezone())
    print('dtmin', dtmin)

    print('dtmax', dtmax)
    # offset - naive and offset - aware
    # datetimes

    # get data from db betwen  dtmin and dtmax
    # sch1 = db.session.query(Schedule.id_r,Schedule.date1_r,Schedule.date2_r,Schedule.days_r,Car.vin,Car.id_car,Schedule.typ_r,Car.description,Car.color_code, Client.name).join(Car,Schedule.id_car_r==Car.id_car).join(Client,Schedule.id_client_r==Client.id_client)\
    # //    .filter((or_(and_(Schedule.date1_r>=dtmin , Schedule.date1_r<=dtmax) , and_(Schedule.date2_r>=dtmin , Schedule.date2_r<=dtmax)))).all()

    # // sch1=Schedule.objects.all().values()

    sch1 = Schedule.objects.select_related().values(
        'id_r', 'date1_r', 'date2_r', 'days_r'
        , 'car__vin', 'car__id_car', 'Typ_dict_id',
        'car__description', 'car__color_code'
    )

    sch1 = ((Schedule.objects.select_related().filter(date1_r__gte=dtmin) &
             Schedule.objects.select_related().filter(date1_r__lte=dtmax)) | (Schedule.objects.select_related().filter(
        date2_r__gte=dtmin) & Schedule.objects.select_related().filter(date2_r__lte=dtmax))).values(
        'id_r','date1_r', 'date2_r', 'days_r'
        , 'car__vin', 'car__id_car', 'Typ_dict_id',
        'car__description', 'car__color_code'
    )

    print(list(sch1))
    lic = 0
    nag = '<tr><th style="width: 15% !important" ></th><th style="width: 20% !important"></th><th style="width: 6% !important"></th>'
    mirok = [f'{d[0]}-{d[1]}' for d in daty]
    for i in sorted(list(set(mirok))):
        nag += f'<th colspan={mirok.count(i)}>{i}</th>'

    nag += '</tr><tr><th style="width: 6% !important"><th><th style="width: 6% !important"></th>'
    for n in daty:
        nag += f'<th style="width: 2% !important">  {n[2]} </th>'
    nag += '</tr>'
    if sch1:
        vins = {r['car__vin']: [] for r in list(sch1)}

        # lines for vins
        for v in list(sch1):
            # value
            # 0 - id_r
            # 1 - date1_r or dtmin
            # 2 - date2_r or dtmax
            # 3 - id_car
            # 4 - typ_r
            # 5 - days_r
            # 6 - car description
            # 7 - car color

            vins[v['car__vin']] += [[v['id_r'], v['date1_r'] if v['date1_r'] >= dtmin else dtmin,
                                     v['date2_r'] if v['date2_r'] < dtmax else dtmax, v['car__id_car'],
                                     v['Typ_dict_id'], v['days_r'], v['car__description'], v['car__color_code'],
                                     'name']]

        # print(vins)
        # sorting row for vin  by date1_r
        for k, v in vins.items():
            sorted_values = sorted(v, key=lambda v: v[1])
            vins[k] = sorted_values

        # dict with preparing HTML by VIN
        vin_line = {}
        for k, v in vins.items():
            line = ''
            lic = 0
            # check empty fields on left of row
            d11 = datetime(vins[k][0][1].year, vins[k][0][1].month, vins[k][0][1].day,
                           tzinfo=timezone.get_current_timezone())
            d22 = dtmin
            betwen = (d11 - d22).days
            # add <td> * number betwen
            if betwen > 0:
                for d in range(0, betwen):
                    line += f'''<td class="typreservation0" onclick="shownew({0},'{getmydate(daty, lic)}',{idcar})"></td>'''
                    lic += 1
            # if vin has reservation do it
            idcar = v[0][3]
            for ri in range(1, len(v)):
                # update nb of days beetwen start to end of reservation
                vins[k][ri - 1][3] = (vins[k][ri - 1][2] - vins[k][ri - 1][1]).days + 1
                # count nb of days without reservation betwen reservations

                d11 = datetime(vins[k][ri][1].year, vins[k][ri][1].month, vins[k][ri][1].day)
                d22 = datetime(vins[k][ri - 1][2].year, vins[k][ri - 1][2].month, vins[k][ri - 1][2].day)

                betwen = (d11 - d22).days - 1

                lic += vins[k][ri - 1][3]
                # HTML for reservation without last for vin
                line += f'''<td colspan={vins[k][ri - 1][3]}  class="typreservation{vins[k][ri - 1][4]}" onclick="show({vins[k][ri - 1][0]},'{0}','{v[0][3]}')">{vins[k][ri - 1][8]} [{vins[k][ri - 1][0]}]</td>'''
                # if has empty fields beetwen reservations then do HTML for empty <td>
                if betwen > 0:
                    for d in range(0, betwen):
                        line += f'''<td  class="typreservation0"  onclick="shownew({0},'{getmydate(daty, lic)}','{idcar}')" ></td>'''  # * (betwen-1)
                        lic += 1
            # Do last reservation for VIN
            vins[k][len(v) - 1][3] = (vins[k][len(v) - 1][2] - vins[k][len(v) - 1][1]).days + 1

            # do HTML for last reservation
            line += f'''<td colspan={vins[k][len(v) - 1][3]}  class="typreservation{vins[k][len(v) - 1][4]}" onclick="show({vins[k][len(v) - 1][0]},'{0}','{vins[k][len(v) - 1][3]}')">{vins[k][len(v) - 1][8]}[{vins[k][len(v) - 1][0]}]</td>'''
            d11 = dtmax
            d22 = datetime(vins[k][len(v) - 1][2].year, vins[k][len(v) - 1][2].month, vins[k][len(v) - 1][2].day,
                           tzinfo=timezone.get_current_timezone())

            betwen = (d11 - d22).days

            lic += vins[k][len(v) - 1][3]
            # if has free <td> after last reservations count how many days in betwen
            if betwen > 0:
                # do HTML fro empty <td> on right side of row
                for d in range(0, betwen):
                    line += f'''<td class="typreservation0" onclick="shownew({0},'{getmydate(daty, lic)}','{idcar}')"></td>'''
                    # line += f'<td  class="typreservation0"></td>' * (betwen+1)
                    lic += 1

            # update dict for preparing HTML for ROW by VIN

            #  print(k,v)

            vin_line[k] = [line, v[0][6], v[0][7]]

    template = loader.get_template("schedule.html")


    context = {
        "sch": vin_line,
        "ilr": vins,
        "nag": nag,
        "dtime": dt,
        "dtt": dtt,
        "now_m_plus":now_m_plus,
        "now_w_plus":now_w_plus,
        "now_m_minus":now_m_minus,
        "now_w_minus":now_w_minus,




    }



    return HttpResponse(template.render(context, request))
