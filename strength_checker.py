import math,string
def calculate_entropy(password):
    charset=0
    if any(c.islower() for c in password): charset+=26
    if any(c.isupper() for c in password): charset+=26
    if any(c.isdigit() for c in password): charset+=10
    if any(c in string.punctuation for c in password): charset+=32
    if charset==0: return 0
    return round(len(password)*math.log2(charset),2)

def check_password_strength(password):
    score=0
    if len(password)>=8: score+=2
    if len(password)>=12: score+=2
    if any(c.islower() for c in password): score+=1
    if any(c.isupper() for c in password): score+=1
    if any(c.isdigit() for c in password): score+=1
    if any(not c.isalnum() for c in password): score+=1
    entropy=calculate_entropy(password)
    strength="Weak" if score<=3 else "Medium" if score<=6 else "Strong"
    return {"Strength":strength,"Score":f"{score}/8","Entropy":f"{entropy} bits"}
