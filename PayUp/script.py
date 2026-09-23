print("Welcome to PayUp!")

event_name = input("What is the occasion? ")
cost = float(input("How much was it? "))
service_charge = int(input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%): ").strip("%"))
group_size = int(input("Size of the party: "))
grand_total = cost + cost * service_charge / 100
total_per_person = grand_total / 3

print()
print(f"Here's the breakdown for {event_name}:")
print()
print(f"Cost: ${cost:.2f}")
print(f"Service charges: ${(cost * service_charge / 100):.2f}")
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total:.2f}")
print()
print(f"Each person must PayUp: ${total_per_person:.2f}")