import re
from rest_framework import serializers
from django.core.validators import validate_email as django_email_validate
from rest_framework.exceptions import ValidationError
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    check_in = serializers.DateTimeField(input_formats=["%d-%m-%Y"],format="%d-%m-%Y")
    check_out = serializers.DateTimeField(input_formats=["%d-%m-%Y"],format="%d-%m-%Y")
    class Meta:
        model = Customer 
        exclude = ['created_at']
        # fields = "__all__"

    def validate_phone_no(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValidationError("Phone number must have 10 digits.")
        return value

    def validate_email(self, value):
        try:
            django_email_validate(value)
            return value
        except Exception:
            raise serializers.ValidationError("Invalid email format.")

    def validate(self, data):
        if data["check_in"] > data["check_out"]:
            raise ValidationError("Check-out must be after check-in.")

        id_type = data.get("identity_type")
        id_number = data.get("identity_proof_number")

        if id_type == "Aadhar Card":
            if len(id_number) != 12 or not id_number.isdigit():
                raise ValidationError("Aadhar number must be 12 digits.")

        elif id_type == "Pan Card":
            regex = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
            if not re.match(regex, id_number):
                raise ValidationError("Please provide correct PAN card number.")

        elif id_type == "Voter ID":
            regex = r"^[A-Z]{3}[0-9]{7}$"
            if not re.match(regex, id_number):
                raise ValidationError("Please provide correct Voter ID number.")

        elif id_type == "Driving License":
            regex = r"^(([A-Z]{2}[0-9]{2})( )|([A-Z]{2}-[0-9]{2}))((19|20)[0-9]{2})[0-9]{7}$"
            if not re.match(regex, id_number):
                raise ValidationError("Please provide correct DL number.")

        return data


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"


class partialSerilizer(serializers.ModelSerializer):
    check_in = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        model = Customer 
        fields = ["name","phone_no","email","check_in","room_no"] 

class ParrtialMenuItemSerializer(serializers.ModelSerializer):
    total_count = serializers.IntegerField(read_only = True)
    class Meta:
        model = MenuItem
        fields = ["name","total_count"]
