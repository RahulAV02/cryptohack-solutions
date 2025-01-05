import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import random
import time


class CryptographicSystem:
    def __init__(self):
        self.key_public = random.randint(100, 999)
        self.key_private = random.randint(100, 999)
        self.mod_value = random.randint(1000, 2000)

    def encrypt_data(self, plaintext):
        return (plaintext * self.key_public) % self.mod_value

    def decrypt_data(self, ciphertext):
        return (ciphertext * self.key_private) % self.mod_value

    def add_encrypted_data(self, c1, c2):
        return (c1 + c2) % self.mod_value

    def multiply_encrypted_data(self, c1, c2):
        return (c1 * c2) % self.mod_value


class KeyRotationSystem:
    def __init__(self):
        self.rotation_interval = 10  # Seconds
        self.start_time = time.time()

    def rotate_keys_if_needed(self, crypto_system):
        if time.time() - self.start_time > self.rotation_interval:
            crypto_system.key_public = random.randint(100, 999)
            crypto_system.key_private = random.randint(100, 999)
            self.start_time = time.time()
            return True
        return False


class CaseManagementSystem:
    def __init__(self):
        self.case_list = []

    def add_new_case(self, case_identifier, encrypted_data):
        self.case_list.append({"case_identifier": case_identifier, "data": encrypted_data})

    def process_all_cases(self, crypto_system):
        results = []
        for case in self.case_list:
            decrypted_data = crypto_system.decrypt_data(case["data"])
            results.append((case["case_identifier"], decrypted_data))
        return results



def generate_performance_charts(encryption_durations, execution_durations):
    plt.figure(figsize=(10, 5))



    plt.subplot(1, 2, 1)
    plt.plot(range(len(encryption_durations)), encryption_durations, marker='o')
    plt.title("Encryption Durations")
    plt.xlabel("Operation")
    plt.ylabel("Time (ms)")



    plt.subplot(1, 2, 2)
    plt.plot(range(len(execution_durations)), execution_durations, marker='o', color='orange')
    plt.title("Execution Durations")
    plt.xlabel("Operation")
    plt.ylabel("Time (ms)")

    plt.tight_layout()
    plt.show()




class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Homomorphic Encryption with Key Rotation and Case Management")
        self.crypto_system = CryptographicSystem()
        self.key_rotation_system = KeyRotationSystem()
        self.case_management_system = CaseManagementSystem()
        self.encryption_durations = []
        self.execution_durations = []

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Homomorphic Encryption").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.root, text="Enter Plaintext:").grid(row=1, column=0, padx=10, pady=5)
        self.plaintext_input = ttk.Entry(self.root)
        self.plaintext_input.grid(row=1, column=1, padx=10, pady=5)

        self.encrypt_and_add_button = ttk.Button(self.root, text="Encrypt & Add Case", command=self.encrypt_and_add_case)
        self.encrypt_and_add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.process_cases_button = ttk.Button(self.root, text="Process Cases", command=self.process_cases)
        self.process_cases_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.show_graph_button = ttk.Button(self.root, text="Show Performance Charts", command=self.show_charts)
        self.show_graph_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.output_display = ttk.Label(self.root, text="", foreground="blue")
        self.output_display.grid(row=5, column=0, columnspan=2, pady=10)

    def encrypt_and_add_case(self):
        try:
            plaintext = int(self.plaintext_input.get())
            start_time = time.time()
            encrypted_data = self.crypto_system.encrypt_data(plaintext)
            encryption_duration = (time.time() - start_time) * 1000  # ms
            self.encryption_durations.append(encryption_duration)

            self.case_management_system.add_new_case(len(self.case_management_system.case_list) + 1, encrypted_data)
            self.output_display.config(text=f"Encrypted and added case {len(self.case_management_system.case_list)}")
        except ValueError:
            self.output_display.config(text="Please enter a valid integer.")


        self.key_rotation_system.rotate_keys_if_needed(self.crypto_system)

    def process_cases(self):
        start_time = time.time()
        results = self.case_management_system.process_all_cases(self.crypto_system)
        execution_duration = (time.time() - start_time) * 1000  # ms
        self.execution_durations.append(execution_duration)

        output = "\n".join([f"Case {case_id}: {data}" for case_id, data in results])
        self.output_display.config(text=f"Processed Cases:\n{output}")

    def show_charts(self):
        generate_performance_charts(self.encryption_durations, self.execution_durations)

 


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()
