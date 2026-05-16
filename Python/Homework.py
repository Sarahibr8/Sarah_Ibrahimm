seconds : 7384

hours = seconds // 3600
minutes = (seconds % 3600) // 60
leftover_seconde = seconds % 60

print (f"{seconds} seconds = {hours} hours , {minutes} minutes , {leftover_seconde} seconds")