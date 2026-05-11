print("===== HOSPITAL / CLINIC APPOINTMENT SYSTEM =====")

# Doctor data
doctors = {
    1: {"name": "Dr. Smith", "specialty": "Dentist"},
    2: {"name": "Dr. John", "specialty": "Pediatrician"},
    3: {"name": "Dr. Emily", "specialty": "Cardiologist"}
}

# Appointment storage
appointments = {}

# Patient records
patient_records = {}

# Queue token
token_number = 1


# Function to display doctors
def show_doctors():
    print("\nAvailable Doctors:")
    for doc_id, details in doctors.items():
        print(f"{doc_id}. {details['name']} - {details['specialty']}")


# Function to book appointment
def book_appointment():
    global token_number

    show_doctors()

    doctor_id = int(input("\nSelect Doctor ID: "))

    if doctor_id not in doctors:
        print("Invalid Doctor ID!")
        return

    patient_name = input("Enter Patient Name: ")
    time_slot = input("Enter Time Slot (Example: 10AM): ")

    # Create doctor schedule if not exists
    if doctor_id not in appointments:
        appointments[doctor_id] = []

    # Check for double booking
    for appointment in appointments[doctor_id]:
        if appointment["time"] == time_slot:
            print("Sorry! This slot is already booked.")
            return

    # Assign token
    token = token_number
    token_number += 1

    # Book appointment
    appointment_data = {
        "patient": patient_name,
        "time": time_slot,
        "token": token
    }

    appointments[doctor_id].append(appointment_data)

    print("\nAppointment Booked Successfully!")
    print(f"Doctor: {doctors[doctor_id]['name']}")
    print(f"Time Slot: {time_slot}")
    print(f"Token Number: {token}")


# Function to add patient record
def add_patient_record():
    patient_name = input("Enter Patient Name: ")
    visit_reason = input("Enter Visit Reason: ")
    medicine = input("Enter Prescribed Medicine: ")

    record = {
        "visit_reason": visit_reason,
        "medicine": medicine
    }

    if patient_name not in patient_records:
        patient_records[patient_name] = []

    patient_records[patient_name].append(record)

    print("Patient record added successfully!")


# Function to view patient records
def view_patient_records():
    patient_name = input("Enter Patient Name: ")

    if patient_name in patient_records:
        print(f"\nRecords of {patient_name}:")

        for i, record in enumerate(patient_records[patient_name], start=1):
            print(f"\nVisit {i}")
            print("Reason:", record["visit_reason"])
            print("Medicine:", record["medicine"])

    else:
        print("No records found!")


# Function to view appointments
def view_appointments():
    show_doctors()

    doctor_id = int(input("\nEnter Doctor ID to view appointments: "))

    if doctor_id in appointments and appointments[doctor_id]:
        print(f"\nAppointments for {doctors[doctor_id]['name']}:")

        for appointment in appointments[doctor_id]:
            print(
                f"Patient: {appointment['patient']} | "
                f"Time: {appointment['time']} | "
                f"Token: {appointment['token']}"
            )

    else:
        print("No appointments found!")


# Main menu
while True:
    print("\n===== MENU =====")
    print("1. Show Doctors")
    print("2. Book Appointment")
    print("3. Add Patient Record")
    print("4. View Patient Records")
    print("5. View Appointments")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_doctors()

    elif choice == "2":
        book_appointment()

    elif choice == "3":
        add_patient_record()

    elif choice == "4":
        view_patient_records()

    elif choice == "5":
        view_appointments()

    elif choice == "6":
        print("Thank you for visiting our clinic!")
        break

    else:
        print("Invalid choice! Please try again.")