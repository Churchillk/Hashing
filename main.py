import hashlib

def hash_email(email):
    hashed_email = hashlib.sha256(email.encode()).hexdigest()
    return hashed_email

def hash_phone_number(phone_number):
    hashed_phone_number = hashlib.sha256(phone_number.encode()).hexdigest()
    return hashed_phone_number
