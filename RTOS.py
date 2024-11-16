import streamlit as st
import threading
import time
import queue

# Task simulation for ADAS, ECUs, and Infotainment
def adaptive_cruise_control():
    while True:
        st.write("Adaptive Cruise Control: Maintaining safe distance and speed...")
        time.sleep(1)  # Simulating real-time task with 1-second intervals

def lane_keeping_assist():
    while True:
        st.write("Lane-Keeping Assist: Ensuring vehicle stays within lane...")
        time.sleep(1.5)  # Simulating real-time task with 1.5-second intervals

def airbag_deployment():
    st.write("Airbag Deployment: Monitoring for collision...")
    time.sleep(2)  # Simulate some delay before deploying airbags
    st.write("Airbag deployed! Safe!")
    return "Airbag deployed"  # Task result, used for critical response

def infotainment_system():
    while True:
        st.write("Infotainment System: Playing music and navigation...")
        time.sleep(3)  # Infotainment takes more time but is less critical

# RTOS-like task scheduler (using priority queues)
class RTOScheduler:
    def __init__(self):
        self.task_queue = queue.PriorityQueue()

    def add_task(self, priority, task_func):
        """ Add task with a given priority (lower value = higher priority) """
        self.task_queue.put((priority, task_func))

    def start(self):
        """ Simulate RTOS scheduling """
        while not self.task_queue.empty():
            priority, task_func = self.task_queue.get()
            st.write(f"Executing task with priority {priority}")
            task_thread = threading.Thread(target=task_func)
            task_thread.daemon = True  # Daemon threads will exit when main program exits
            task_thread.start()
            time.sleep(0.1)  # Adding a small delay before starting next task

# Streamlit UI
def main():
    st.title("Automotive Systems Real-Time Simulation")
    
    st.write("This application simulates various automotive systems such as Adaptive Cruise Control, Lane-Keeping Assist, Airbag Deployment, and Infotainment System.")
    
    if st.button("Start Simulation"):
        # Create an RTOS-like scheduler
        scheduler = RTOScheduler()

        # Adding critical tasks with high priority (lower priority number)
        scheduler.add_task(1, adaptive_cruise_control)
        scheduler.add_task(2, lane_keeping_assist)
        scheduler.add_task(3, airbag_deployment)

        # Adding infotainment system task with lower priority (higher priority number)
        scheduler.add_task(10, infotainment_system)

        # Start the scheduler to execute tasks
        scheduler.start()

        st.write("Simulation started. Monitoring tasks...")
    
    st.write("Note: This is a simulation. The tasks will run concurrently and continuously.")

if __name__ == "__main__":
    main()
