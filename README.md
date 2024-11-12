# Zabbix

# Zabbix Monitoring and User Authentication System

This project consists of two main components:

1. **Zabbix Monitoring System** - A Docker-based setup for monitoring the activity of users in a system across multiple regions, using Zabbix to collect metrics about active clients, active users, active administrators, and clients from different regions.
2. **User Authentication System** - A RESTful API built with FastAPI to handle user registration, login, and logout. It provides endpoints for managing users and their activity statuses.

---

## Table of Contents

- [Requirements](#requirements)
- [Docker Setup](#docker-setup)
  - [MariaDB Setup](#mariadb-setup)
  - [Zabbix Setup](#zabbix-setup)
  - [Zabbix Web Interface Setup](#zabbix-web-interface-setup)
- [API Endpoints](#api-endpoints)
  - [User Signup](#user-signup)
  - [User Login](#user-login)
  - [User Logout](#user-logout)
- [Enums](#enums)
- [Monitoring with Zabbix](#monitoring-with-zabbix)
- [Mock Traffic Simulation](#mock-traffic-simulation)
- [Utilities](#utilities)
- [License](#license)

---

## Requirements

1. **Docker** - To run the Zabbix and MariaDB containers.
2. **FastAPI** - Python web framework for the RESTful API.
3. **MySQL** - Database to store user information and authentication details.
4. **Python** - For the backend logic and traffic simulation.
5. **Zabbix** - Monitoring tool for collecting metrics and generating reports.

---

## Docker Setup

### MariaDB Setup

The project uses MariaDB for storing user and authentication data. The database is set up within the `docker-compose.yml` file as a `mariadb` container.

```yaml
mariadb:
  image: docker.io/bitnami/mariadb-galera:10.11
  environment:
    - MARIADB_ROOT_PASSWORD=12345
    - MARIADB_GALERA_MARIABACKUP_PASSWORD=12345
    - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://
    - MARIADB_CHARACTER_SET=utf8mb4
    - MARIADB_COLLATE=utf8mb4_bin
  ports:
    - '3306:3306'
    - '4444:4444'
    - '4567:4567'
    - '4568:4568'
  volumes:
    - mariadb_galera_data:/bitnami/mariadb
```

### Zabbix Setup

The Zabbix server is configured to work with MariaDB. The container `zabbix-server` connects to MariaDB for data storage.

```yaml
zabbix-server:
  image: zabbix/zabbix-server-mysql:ubuntu-6.4-latest
  environment:
    DB_SERVER_HOST: 'mariadb'
    MYSQL_USER: 'root'
    MYSQL_PASSWORD: '12345'
  ports:
    - "10051:10051"
  depends_on:
    - mariadb
```

### Zabbix Web Interface Setup

Zabbix web interface allows users to view monitoring data. It is set up using the `zabbix-web` container.

```yaml
zabbix-web:
  image: zabbix/zabbix-web-apache-mysql:ubuntu-6.4-latest
  environment:
    DB_SERVER_HOST: 'mariadb'
    MYSQL_USER: 'root'
    MYSQL_PASSWORD: '12345'
    ZBX_SERVER_HOST: 'zabbix-server'
    PHP_TZ: Europe/Kiev
  ports:
    - "80:8080"
    - "443:8443"
  depends_on:
    - mariadb
    - zabbix-server
```

---

## API Endpoints

### User Signup

- **Endpoint:** `/user/signup`
- **Method:** `POST`
- **Description:** Allows new users to register by providing their full name, email, password, role, and location.
- **Response:** Returns the user information upon successful registration.

### User Login

- **Endpoint:** `/user/login`
- **Method:** `POST`
- **Description:** Authenticates users based on email and password. Sets the user's status as active.
- **Response:** Returns user data upon successful login.

### User Logout

- **Endpoint:** `/user/logout`
- **Method:** `POST`
- **Description:** Logs out users and sets their status to inactive.
- **Response:** Returns user data upon successful logout.

---

## Enums

This project defines three `enum` classes to manage roles, locations, and metrics.

### Role Enum
Defines user roles:
- `USER`
- `ADMIN`

### Location Enum
Defines geographic locations:
- `EUROPE`
- `ASIA`
- `NORTH_AMERICA`

### Metrics Enum
Defines system monitoring metrics:
- `TOTAL_NUMBER_OF_ACTIVE_CLIENTS`
- `TOTAL_NUMBER_OF_ACTIVE_USERS`
- `TOTAL_NUMBER_OF_ACTIVE_ADMINS`
- `NUMBER_OF_CLIENTS_FROM_EUROPE`
- `NUMBER_OF_CLIENTS_FROM_ASIA`
- `NUMBER_OF_CLIENTS_FROM_NORTH_AMERICA`

---

## Monitoring with Zabbix

The monitoring system collects and sends various metrics to the Zabbix server, including:

- Total number of active clients
- Total number of active users
- Total number of active admins
- Active clients from specific regions

Each metric is sent to the Zabbix server for monitoring and report generation.

---

## Mock Traffic Simulation

The mock traffic simulation code simulates user logins and logouts over a specified period. This can be used for stress testing and monitoring system performance during high traffic.

```python
def mock_traffic():
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(minutes=5)
    while datetime.datetime.now() < end_time:
        login_users(count)
        logout_users(count)
```

---

## Utilities

The following utility functions are provided for handling database operations and user status updates:

- `run_query(query, param, is_update)` - Executes a database query.
- `check_user(data: UserLogin)` - Checks if a user exists.
- `set_active(user: UserLogin, value: bool)` - Sets the user's active status.

---

## License

This project is licensed under the MIT License.

---

### Notes

1. **Customizations:** You can customize the Docker setup to scale the Zabbix and MariaDB services or add additional metrics to monitor.
2. **Security:** Ensure that sensitive information, like passwords, is handled securely in production environments.
