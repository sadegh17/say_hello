from django.core.exceptions import ValidationError

def email_valid(value):
    email =value
    if ".edu" in email:
        raise ValidationError(" gi bakher shefte kes") 


