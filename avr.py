import time
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from collections import deque
import heapq

class DeliveryRobot:
    def __init__(self, map_data):
        self.map = map_data
        self.current_location = "Pharmacy"
        self.delivery_queue = deque()
        self.medication_log = []
        self.root = tk.Tk()
        self.root.title("AI Delivery Robot System")
        self.create_gui()

    def create_gui(self):
        self.tree = ttk.Treeview(self.root, columns=("Patient", "Room", "Medication"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.grid(row=0, column=0, columnspan=3, pady=10)

        tk.Button(self.root, text="Add Delivery", command=self.add_delivery).grid(row=1, column=0, padx=10)
        tk.Button(self.root, text="Start Delivery", command=self.start_delivery_thread).grid(row=1, column=1, padx=10)
        tk.Button(self.root, text="View Log", command=self.show_log).grid(row=1, column=2, padx=10)

    def add_delivery(self):
        patient_id = simpledialog.askstring("Patient ID", "Enter Patient ID:")
        room_number = simpledialog.askstring("Room Number", "Enter Room Number:")
        medication = simpledialog.askstring("Medication", "Enter Medication Name:")

        if patient_id and room_number and medication:
            delivery = {
                "patient_id": patient_id,
                "room": room_number,
                "medication": medication,
                "timestamp": time.time()
            }
            self.delivery_queue.append(delivery)
            self.tree.insert("", "end", values=(patient_id, room_number, medication))
            messagebox.showinfo("Loaded", f"Medication loaded for Patient {patient_id} in Room {room_number}.")
        else:
            messagebox.showwarning("Missing Info", "Please enter all delivery details.")

    def start_delivery_thread(self):
        if not self.delivery_queue:
            messagebox.showinfo("No Deliveries", "No deliveries in the queue.")
            return
        threading.Thread(target=self.deliver_medication).start()

    def navigate_to(self, destination):
        path = self.find_shortest_path(self.current_location, destination)
        for loc in path:
            print(f"Navigating to {loc}...")
            time.sleep(1)
        self.current_location = destination

    def deliver_medication(self):
        delivery = self.delivery_queue.popleft()
        start_time = time.time()

        self.navigate_to(delivery["room"])
        delivered_time = time.time()

        delivery["start_time"] = start_time
        delivery["delivered_time"] = delivered_time
        self.medication_log.append(delivery)

        messagebox.showinfo(
            "Delivered",
            f"Delivered {delivery['medication']} to Patient {delivery['patient_id']} in Room {delivery['room']}.\n"
            f"Start: {time.strftime('%H:%M:%S', time.localtime(start_time))}\n"
            f"Delivered: {time.strftime('%H:%M:%S', time.localtime(delivered_time))}"
        )

        self.navigate_to("Pharmacy")
        self.refresh_queue_display()

    def refresh_queue_display(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for delivery in self.delivery_queue:
            self.tree.insert("", "end", values=(delivery["patient_id"], delivery["room"], delivery["medication"]))

    def show_log(self):
        log_window = tk.Toplevel(self.root)
        log_window.title("Delivery Log")
        log_tree = ttk.Treeview(log_window, columns=("Patient", "Room", "Medication", "Start", "Delivered"), show="headings")
        for col in log_tree["columns"]:
            log_tree.heading(col, text=col)
        log_tree.pack(fill="both", expand=True)

        for entry in self.medication_log:
            log_tree.insert("", "end", values=(
                entry["patient_id"],
                entry["room"],
                entry["medication"],
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(entry["start_time"])),
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(entry["delivered_time"]))
            ))

    def find_shortest_path(self, start, end):
        # Dijkstra’s algorithm
        graph = self.map
        heap = [(0, start, [])]
        visited = set()

        while heap:
            (cost, node, path) = heapq.heappop(heap)
            if node in visited:
                continue
            path = path + [node]
            if node == end:
                return path
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + 1, neighbor, path))
        return []

    def run(self):
        self.root.mainloop()

# Example hospital map (bi-directional)
hospital_map = {
    "Pharmacy": ["Room101", "Room102", "Room103"],
    "Room101": ["Pharmacy", "Room102"],
    "Room102": ["Pharmacy", "Room101", "Room103"],
    "Room103": ["Pharmacy", "Room102"]
}

if __name__ == "__main__":
    robot = DeliveryRobot(hospital_map)
    robot.run()



