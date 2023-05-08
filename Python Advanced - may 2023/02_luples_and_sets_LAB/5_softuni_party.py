number_of_guests = int(input())
guest_list = {input() for _ in range(number_of_guests)}
command = input()
came_guest = set()
while command != "END":
    came_guest.add(command)
    command = input()
guests_didn_come = guest_list.difference(came_guest)
ordered_didn_come_list = sorted(guests_didn_come)
print(len(guests_didn_come))
print('\n'.join(ordered_didn_come_list))


