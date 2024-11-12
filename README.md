Here's a complete `README.md` for your monitoring system project with Zabbix and Docker.

---

# Monitoring System Prototype with Zabbix and Docker

## Overview
This project demonstrates a Dockerized monitoring system using Zabbix. The system supports both agent-based and agentless monitoring methods to track server metrics, simulate user traffic, and analyze user activity. It includes a Python-based user authentication application and a traffic simulation script to test the monitoring setup under various load conditions.

## Technologies
- **Zabbix**: Monitors system performance, gathering metrics like CPU usage, memory, disk space, and network traffic.
- **Docker & Docker Compose**: Used to deploy Zabbix components in isolated, scalable containers. This includes MariaDB Galera Cluster, Zabbix Server, Zabbix Agent, and Zabbix Web Interface.
- **Python & FastAPI**: Used to create a REST API for user authentication with endpoints for registration, login, and logout.
- **MySQL**: Stores user data for the authentication app.

## Features
1. **Monitoring Setup**:
   - Deploys Zabbix in a Docker environment, ensuring consistency and ease of scaling.
   - Zabbix Agent gathers system metrics and sends them to the Zabbix Server, where they are stored in MariaDB and visualized in the Zabbix Web Interface.

2. **User Authentication App**:
   - REST API built with FastAPI, allowing users to register, login, and logout.
   - Stores user data, including name, email, password, role, and location, in a MySQL database.

3. **Traffic Simulation**:
   - A Python script simulates random login/logout actions to create system load and test monitoring accuracy.
   - Another script collects user activity metrics, sending this data to the Zabbix Server for monitoring and visualization.

## Setup Instructions

### Prerequisites
- **Docker** and **Docker Compose** installed on your system.
- **Python 3.x** and **FastAPI** installed for the user authentication app.

### Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set up Zabbix with Docker Compose**:
   - Ensure Docker and Docker Compose are installed.
   - Start the Zabbix services with the following command:
     ```bash
     docker-compose up -d
     ```
   - This command starts the Zabbix Server, Zabbix Agent, MariaDB Galera Cluster, and Zabbix Web Interface.

3. **Run the User Authentication App**:
   - Navigate to the authentication app folder:
     ```bash
     cd authentication_app
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the FastAPI app:
     ```bash
     uvicorn main:app --reload
     ```

4. **Simulate Traffic**:
   - Navigate to the simulation script folder:
     ```bash
     cd simulation_scripts
     ```
   - Run the traffic simulation script:
     ```bash
     python simulate_traffic.py
     ```
   - This script will randomly generate login/logout actions to create system load and send metrics to the Zabbix Server.

## Results
The Zabbix Web Interface provides real-time insights into system performance and user activity levels. By visualizing metrics like CPU usage, memory, and user activity, you can monitor the system’s behavior under different load conditions.

## Usage
1. Access the Zabbix Web Interface in your browser (typically at `http://localhost:8080` if using default Docker configuration).
2. Use the FastAPI user authentication app’s endpoints for testing registration, login, and logout functions.
3. Run the traffic simulation script to observe how the system handles user activity and load.

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like any additional details or modifications!
