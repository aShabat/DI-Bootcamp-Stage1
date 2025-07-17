print({key: value for key, value in [("name", "Elie"), ("job", "Instructor")]})

print(
    {
        key: value
        for key, value in zip(
            ["CA", "NJ", "RI"], ["California", "New Jersey", "Rhode Island"]
        )
    }
)

print({c: 0 for c in "aoeui"})

import string

print({i: c for i, c in enumerate(string.ascii_uppercase)})
