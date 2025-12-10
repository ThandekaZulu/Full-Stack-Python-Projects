age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 18 :
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(18):
    print("You are allowed to drive")
else:
    print("You are not allowed to drive")