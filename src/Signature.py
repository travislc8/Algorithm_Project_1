class Signature:
    def __init__(self, data):
        self.data = data

    def generate_signature(self):
        # Placeholder for signature generation logic
        pass

    def verify_signature(self, signature):
        # Placeholder for signature verification logic
        pass

if __name__ == "__main__":
    data = "Sample data to sign"
    signature_instance = Signature(data)
    
    # Generate a signature
    signature = signature_instance.generate_signature()
    print(f"Generated Signature: {signature}")
    
    # Verify the signature
    is_valid = signature_instance.verify_signature(signature)
    print(f"Signature valid: {is_valid}")