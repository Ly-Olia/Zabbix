"""The code creates a new thread for each monitoring method
in the monitoring_methods list and starts it.
It then runs the app using uvicorn on localhost and port 8001.
This code is running the app and simultaneously monitoring
certain aspects of its current state."""
from threading import Thread

import uvicorn

from app.api import app
from app.monitor import monitoring_methods

if __name__ == '__main__':
    # For each monitoring method in the monitoring_methods list, create a new Thread object and start it
    for monitoring_method in monitoring_methods:
        thread = Thread(target=monitoring_method, daemon=True)
        thread.start()
    # Start the app using uvicorn on localhost and port 8001
    uvicorn.run(app, host="localhost", port=8001)
