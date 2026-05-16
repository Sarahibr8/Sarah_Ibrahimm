# Ask user for total seconds
total_seconds = int(input("Enter total seconds: "))

# Convert
days = total_seconds // 86400
remaining = total_seconds % 86400

hours = remaining // 3600
remaining = remaining % 3600

minutes = remaining // 60
seconds = remaining % 60

# Output
print("Days:   ", days)
print("Hours:  ", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

# Formatted output
print(f"Formatted: {days}d {hours:02d}h {minutes:02d}m {seconds:02d}s")