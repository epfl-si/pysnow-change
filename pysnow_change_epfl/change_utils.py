# -*- coding:utf-8 -*-

"""
(c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2018.
"""
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport
import datetime
import os
import re


def check_sciper():
    if os.environ.get('SCIPER') is None:
        raise Exception("Error: Environment variable SCIPER not found.")
    else:
        s = os.environ.get('SCIPER')
        if re.match(r"^[0-9]{6}$", s) is None:
            raise Exception(
                "Error: Not a valid SCIPER. Check your environment " +
                "variable SCIPER.")
    return


def check_pwd():
    if os.environ.get('SNOW_CHG_PWD') is None:
        raise Exception("Error: Environment variable SNOW_CHG_PWD not found.")
    return


def get_changelog_info(CHANGELOG_path):
    if not os.path.exists(CHANGELOG_path):
        raise Exception("Error: CHANGELOG file not found.")
    version_found = False
    description = ""
    info_previous_version = ['0', '0', '0']
    with open(CHANGELOG_path, "r") as f:
        for line in f:
            if "###" in line:
                if version_found:
                    info_previous_version = re.findall("([0-9]+)", line)
                    break
                info_version = re.findall("([0-9]+)", line)
                version_found = True
            elif version_found:
                description = description + line.lstrip(" ")
    impact_category = 'Minor'
    if info_version[0] != info_previous_version[0]:
        impact_category = 'Major'
    elif info_version[1] != info_previous_version[1]:
        impact_category = 'Significant'

    version_number = "v{0}.{1}.{2}".format(
        info_version[0], info_version[1], info_version[2])
    return version_number, description, impact_category


def create_change(service_id, snow_group, impact_category,
                  short_description, description, env='test'):

    host = 'support-test.epfl.ch'
    if env == 'prod':
        host = 'support.epfl.ch'

    sciper = os.environ.get('SCIPER')
    password_ws_idevelop = os.environ.get('SNOW_CHG_PWD')

    current_date = datetime.datetime.now()
    start_date = "{:%Y-%m-%d %H:%M:%S}".format(current_date)
    end_date = "{:%Y-%m-%d %H:%M:%S}".format(
        current_date + datetime.timedelta(minutes=1))

    import_set_run = '-'
    template_import_log = '-'
    u_assigned_to = sciper
    u_assignment_group = snow_group
    u_backout_plan = '-'
    u_business_service = service_id
    u_service_component = '-'
    u_change_plan = '-'
    u_change_type = 'Standard'
    u_configuration_item = '-'
    u_short_description = short_description
    u_description = description
    u_impact_category = impact_category    # 'Minor'/'Significant'/'Major'
    u_planned_start_date = start_date
    u_planned_end_date = end_date
    u_work_start = start_date
    u_work_end = end_date

    session = Session()
    session.auth = HTTPBasicAuth('idevelop_webservice', password_ws_idevelop)
    transport_with_basic_auth = Transport(session=session)

    client = Client(
        wsdl='https://{}/u_epfl_change_log.do?wsdl'.format(host),
        transport=transport_with_basic_auth
    )

    result = client.service.insert(
        import_set_run,
        template_import_log,
        u_assigned_to,
        u_assignment_group,
        u_backout_plan,
        u_business_service,
        u_change_plan,
        u_change_type,
        u_configuration_item,
        u_description,
        u_impact_category,
        u_planned_end_date,
        u_planned_start_date,
        u_service_component,
        u_short_description,
        u_work_end,
        u_work_start
    )

    if result.status == 'inserted':
        return "Change created and closed.\n" \
            "Number: {0}\nURL: https://{1}/backoffice/nav_to.do?" \
            "uri=change_request.do?sys_id={2}" \
            .format(result.display_value, host, result.sys_id)
    else:
        return "Error: {}".format(result.error_message)
