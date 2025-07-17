class CustomError(Exception):
    pass
class ValidationError(Exception):
    def __init__(self,msg,code='none'):
        super().__init__(msg)
        self.code=code
def validate_age(age):
    if age<0:
        raise ValidationError("age can not be negative",code="negative_age")
    if age>150:
        raise ValidationError("age seems unrealistic",code="unrealistic_age")
try:
    validate_age(-5)
except ValidationError as e:
    print(f"validation failed:{e}")
    print(f"error code:{e.code}")