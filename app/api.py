from app import models
from django.shortcuts import get_object_or_404
from  .models import UsersModel, VerificationModel

def verify_otp_and_store_password(email, entered_otp):
    verification = get_object_or_404(VerificationModel, email=email)

    if verification.otp == entered_otp:
        # Store the already hashed password (DO NOT hash again)
        user = UsersModel.objects.create(
            first_name=verification.full_name,
            email=verification.email,
            password=verification.password  # Use as is (already hashed)
        )

        # Optional: Delete verification record after successful verification
        verification.delete()

        return "OTP verified, user registered successfully!"

    return "Invalid OTP. Try again."