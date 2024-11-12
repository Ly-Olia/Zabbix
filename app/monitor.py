"""
This code is a Python script that sets up monitoring for a system with users located in different regions.
The script uses the Zabbix monitoring tool to collect metrics about active clients, active users,
active admins, and the number of clients from specific regions.
"""
import datetime
import time
from pyzabbix import ZabbixSender, ZabbixMetric
from app.utils import run_query

from app.enums import Role, Location, Metrics


# the total number of clients who are active
def get_login_clients():
    query = "SELECT COUNT(*) FROM users WHERE is_active = 1"
    return run_query(query, [], False)


# the number of clients who are active and have a specific role
def get_login_clients_by_role(role):
    query = "SELECT COUNT(*) FROM users WHERE role=%s AND is_active = 1"
    return run_query(query, (role,), False)


# the number of clients who are active and located in a specific region
def get_login_clients_by_location(location):
    query = "SELECT COUNT(*) FROM users WHERE location=%s AND is_active = 1"
    return run_query(query, (location,), False)


# Define a class for Zabbix monitoring
class ZabbixMonitoring:
    # Constructor function to initialize the class with the necessary hostname values
    def __init__(self):
        self.zabbix_hostname = 'Zabbix server'
        self.agent_hostname = 'localhost'

    # Function to send a metric to Zabbix server
    def send_metric(self, metric_name: Metrics, metric_value):
        zbx = ZabbixSender(self.agent_hostname)
        metric = [ZabbixMetric(self.zabbix_hostname, metric_name.value, metric_value), ]
        print(f"{metric_name.value} {zbx.send(metric)}")

    # Function to collect the total number of active clients and send it as a metric to Zabbix server
    def collect_total_clients(self):
        # Set the start and end time for monitoring
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=6)
        while datetime.datetime.now() < end_time:
            print("Monitoring clients...")
            num_list = get_login_clients()
            num_active_clients = num_list[0][0]
            self.send_metric(Metrics.TOTAL_NUMBER_OF_ACTIVE_CLIENTS, num_active_clients)
            # Wait for 20 seconds before monitoring again
            time.sleep(20)

    # Function to collect the total number of active users and send it as a metric to Zabbix server
    def collect_total_users(self):
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=6)
        while datetime.datetime.now() < end_time:
            print("Monitoring users...")
            num_list = get_login_clients_by_role(Role.USER.value)
            num_active_users = num_list[0][0]
            self.send_metric(Metrics.TOTAL_NUMBER_OF_ACTIVE_USERS, num_active_users)
            time.sleep(15)

    # Function to collect the total number of active admins and send it as a metric to Zabbix server
    def collect_total_admins(self):
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=6)
        while datetime.datetime.now() < end_time:
            print("Monitoring admins...")
            num_list = get_login_clients_by_role(Role.ADMIN.value)
            num_active_admins = num_list[0][0]
            self.send_metric(Metrics.TOTAL_NUMBER_OF_ACTIVE_ADMINS, num_active_admins)
            time.sleep(15)

    # Function to collect the total number of active clients from Europe and send it as a metric to Zabbix server
    def collect_total_clients_from_europe(self):
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=6)
        while datetime.datetime.now() < end_time:
            print("Monitoring europe...")
            num_list = get_login_clients_by_location(Location.EUROPE.value)
            num_clients_from_europe = num_list[0][0]
            self.send_metric(Metrics.NUMBER_OF_CLIENTS_FROM_EUROPE, num_clients_from_europe)
            time.sleep(15)

    # Function to collect the total number of active clients from Asia and send it as a metric to Zabbix server
    def collect_total_clients_from_asia(self):
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=6)
        while datetime.datetime.now() < end_time:
            print("Monitoring asia...")
            num_list = get_login_clients_by_location(Location.ASIA.value)
            num_clients_from_asia = num_list[0][0]
            self.send_metric(Metrics.NUMBER_OF_CLIENTS_FROM_ASIA, num_clients_from_asia)
            time.sleep(15)

    # Function to collect the total number of active clients from North America and send it as a metric to Zabbix server
    def collect_total_clients_from_north_america(self):
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=6)
        while datetime.datetime.now() < end_time:
            print("Monitoring north america...")
            num_list = get_login_clients_by_location(Location.NORTH_AMERICA.value)
            num_clients_from_north_america = num_list[0][0]
            self.send_metric(Metrics.NUMBER_OF_CLIENTS_FROM_NORTH_AMERICA, num_clients_from_north_america)
            time.sleep(15)


# Create a list of monitoring methods to be executed
monitoring_methods = [
    ZabbixMonitoring().collect_total_clients,
    ZabbixMonitoring().collect_total_users,
    ZabbixMonitoring().collect_total_admins,
    ZabbixMonitoring().collect_total_clients_from_europe,
    ZabbixMonitoring().collect_total_clients_from_asia,
    ZabbixMonitoring().collect_total_clients_from_north_america
]
