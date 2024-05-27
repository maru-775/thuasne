class DeviceManager:
    def __init__(self):
        self.devices = {}
        self.patients = {}
        
    def declare_device(self, device_id, firmware):
        if device_id in self.devices:
            return f"KO: Device {device_id} is already declared"
        self.devices[device_id] = firmware
        return f"OK: Device {device_id} declared successfully"
    
    def associate_device_patient(self, device_id, patient_id):
        if device_id not in self.devices:
            return f"KO: Device {device_id} is not declared"
        if device_id in self.patients:
            return f"KO: Device {device_id} is already associated to {self.patients[device_id]}"    
        self.patients[device_id] = patient_id
        return f"OK: Device {device_id} associated to {patient_id}"
    
    def dissociate_device_patient(self, device_id, patient_id):
        if device_id not in self.patients or self.patients[device_id] != patient_id:
            return f"KO: Device {device_id} is not associated to {patient_id}"
        del self.patients[device_id]
        return f"OK: Device {device_id} dissociated from {patient_id}"
    
    def update_firmware(self, device_id, firmware):
        if device_id not in self.devices:
            return f"KO: Device {device_id} is not declared"
        self.devices[device_id] = firmware
        return f"OK: Device {device_id} firmware update succesfully to {firmware}"
    
    def list_devices(self):
        return self.devices
        
        
# Example usage
manager = DeviceManager()

# Declare devices
print("TEST: declare devices")
print(manager.declare_device('SLB-01', 'FW-01'))  # OK
print(manager.declare_device('SLB-01', 'FW-01'))  # KO (car on a déjà fait)
print(manager.declare_device('SLB-02', 'FW-01'))  # OK

# Associate devices with patients
print("\nTEST: associate devices with patients")
print(manager.associate_device_patient('SLB-01', 'User-01'))  # OK
print(manager.associate_device_patient('SLB-01', 'User-02'))  # KO (car on a déjà associe SLB-01 avec User-01)
print(manager.associate_device_patient('SLB-02', 'User-02'))  # OK

# Dissociate devices from patients
print("\nTEST: dissociate devices from patients")
print(manager.dissociate_device_patient('SLB-03', 'User-03'))  # KO (car on n’a pas associe SLB-03 avec User-03)
print(manager.dissociate_device_patient('SLB-01', 'User-01'))  # OK

# Update firmware
print("\nTEST: update firmware")
print(manager.update_firmware('SLB-01', 'FW-02'))  # OK
print(manager.update_firmware('SLB-02', 'FW-02'))  # OK

# List devices firmware
print("\nTEST: list devices")
print(manager.list_devices())
