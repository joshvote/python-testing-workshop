from typing import Optional


class ViewUser:
    email: str = ''
    display_id: str = ''
    name: str = ''
    primary_address_line1: Optional[str] = ''
    primary_address_line2: Optional[str] = ''

    def __init__(self, email: str, display_id: str, name: str,
                 primary_address_line1: Optional[str], primary_address_line2: Optional[str]) -> None:
        self.email = email
        self.display_id = display_id
        self.name = name
        self.primary_address_line1 = primary_address_line1
        self.primary_address_line2 = primary_address_line2
