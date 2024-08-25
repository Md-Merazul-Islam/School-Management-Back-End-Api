# from rest_framework import serializers
# from .models import Fee
# import uuid
# import logging
# from datetime import datetime
# from django.db import transaction
# from sslcommerz_lib import SSLCOMMERZ
# from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _

# def generate_transaction_id():
#     timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#     unique_id = uuid.uuid4().hex[:6].upper()
#     return f'TXN-{timestamp}-{unique_id}'

# class FeePaymentSerializer(serializers.Serializer):
#     MONTH_CHOICES = [
#         ('January', 'January'),
#         ('February', 'February'),
#         ('March', 'March'),
#         ('April', 'April'),
#         ('May', 'May'),
#         ('June', 'June'),
#         ('July', 'July'),
#         ('August', 'August'),
#         ('September', 'September'),
#         ('October', 'October'),
#         ('November', 'November'),
#         ('December', 'December'),
#     ]

#     CLASS_CHOICES = [
#         ('1st Grade', '1st Grade'),
#         ('2nd Grade', '2nd Grade'),
#         ('3rd Grade', '3rd Grade'),
#         ('4th Grade', '4th Grade'),
#         ('5th Grade', '5th Grade'),
#         ('6th Grade', '6th Grade'),
#         ('7th Grade', '7th Grade'),
#         ('8th Grade', '8th Grade'),
#         ('9th Grade', '9th Grade'),
#         ('10th Grade', '10th Grade'),
#         ('11th Grade', '11th Grade'),
#         ('12th Grade', '12th Grade'),
#     ]

#     student_id = serializers.IntegerField()
#     amount = serializers.DecimalField(max_digits=10, decimal_places=2)  # This will be updated based on the number of months
#     month_names = serializers.ListField(child=serializers.ChoiceField(choices=MONTH_CHOICES))
#     class_name = serializers.ChoiceField(choices=CLASS_CHOICES)

#     def validate(self, data):
#         student_id = data.get('student_id')
#         amount = data.get('amount')
#         month_names = data.get('month_names')

#         try:
#             student = User.objects.get(id=student_id)
#         except User.DoesNotExist:
#             raise serializers.ValidationError({'error': _('Student does not exist')})

#         # Validate amount (e.g., it should be positive)
#         if amount <= 0:
#             raise serializers.ValidationError({'error': _('Invalid payment amount')})

#         # Optionally: calculate the total amount based on months
#         number_of_months = len(month_names)
#         expected_amount = 1500 * number_of_months  # Assuming 1500 is the fee per month
#         if amount != expected_amount:
#             raise serializers.ValidationError({'error': _('Amount does not match the number of months selected')})

#         data['student'] = student
#         return data

#     def create(self, validated_data):
#         try:
#             student = validated_data['student']
#             amount = validated_data['amount']
#             month_names = validated_data['month_names']
#             class_name = validated_data['class_name']

#             with transaction.atomic():
#                 transaction_id = generate_transaction_id()
#                 settings = {
#                     'store_id': 'bookh668dde6d76e0c',
#                     'store_pass': 'bookh668dde6d76e0c@ssl',
#                     'issandbox': True
#                 }
#                 sslcz = SSLCOMMERZ(settings)
#                 post_body = {
#                     'total_amount': amount,
#                     'currency': "BDT",
#                     'tran_id': transaction_id,
#                     'success_url': 'https://yourdomain.com/payment/success/',
#                     'fail_url': 'https://yourdomain.com/payment/fail/',
#                     'cancel_url': 'https://yourdomain.com/payment/cancel/',
#                     'emi_option': 0,
#                     'cus_name': student.first_name,  # Assuming the User model has these fields
#                     'cus_email': student.email,
#                     'cus_phone': student.profile.phone_number,  # Adjust based on your User model
#                     'cus_add1': student.profile.address,  # Adjust based on your User model
#                     'cus_city': student.profile.city,  # Adjust based on your User model
#                     'cus_country': "Bangladesh",
#                     'shipping_method': "NO",
#                     'num_of_item': 1,
#                     'product_name': f"Fee Payment for {', '.join(month_names)} ({class_name})",
#                     'product_category': "Education",
#                     'product_profile': "general"
#                 }

#                 response = sslcz.createSession(post_body)

#                 if response.get('status') == 'SUCCESS':
#                     gateway_url = response['GatewayPageURL']
#                     # Log the payment details
#                     Fee.objects.create(
#                         student=student,
#                         amount=amount,
#                         due_date=datetime.now(),  # Set a relevant due date
#                         status='Unpaid',
#                         transaction_id=transaction_id,
#                         month_names=month_names  # Save months if needed
#                     )
#                     return {
#                         'payment_url': gateway_url,
#                         'transaction_id': transaction_id
#                     }
#                 else:
#                     raise serializers.ValidationError({'error': _('Failed to create payment session')})

#         except Exception as e:
#             logging.error(f"Payment processing failed: {e}")
#             raise serializers.ValidationError({'error': _('Failed to process payment.')})
