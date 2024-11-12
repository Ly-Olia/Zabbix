"""
This code defines three separate enum classes (Role, Location, and Metrics)
which are used to define and enforce sets of constants with a fixed set of possible values.
"""
import enum


# define Role enum with two possible values
class Role(enum.Enum):
    USER = "user"
    ADMIN = "admin"


# define Location enum with three possible values
class Location(enum.Enum):
    EUROPE = "europe"
    ASIA = "asia"
    NORTH_AMERICA = "north america"


# define Metrics enum with different metrics that can be used to evaluate the system
class Metrics(enum.Enum):
    TOTAL_NUMBER_OF_ACTIVE_CLIENTS = "total_number_of_active_clients"
    TOTAL_NUMBER_OF_ACTIVE_USERS = "total_number_of_active_users"
    TOTAL_NUMBER_OF_ACTIVE_ADMINS = "total_number_of_active_admins"
    NUMBER_OF_CLIENTS_FROM_EUROPE = "number_of_clients_from_europe"
    NUMBER_OF_CLIENTS_FROM_ASIA = "number_of_clients_from_asia"
    NUMBER_OF_CLIENTS_FROM_NORTH_AMERICA = "number_of_clients_from_north_america"
