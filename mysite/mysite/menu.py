from simple_menu import Menu, MenuItem
from django.urls import reverse

# Add two items to our main menu
Menu.add_item("main", MenuItem("Schedule",
                               reverse("show_schedule"),
                               weight=10,
                               icon="tools"))

Menu.add_item("main", MenuItem("Cars",
                               reverse("show_cars"),
                               weight=20,
                               icon="report"))
Menu.add_item("main", MenuItem("Clients",
                               reverse("show_clients"),
                               weight=20,
                               icon="report"))

print("dodano menu%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")