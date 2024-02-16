mock text:                  "Lorem ipsum dolor sit amet"
mock phone:                 "345-345-3455"
mock email:                 "person.name@testmail.com"
mock social:                "454-54-4545"
mock VA [file] [number]:    "111223333"
mock first:                 "Person"
mock middle:                "Middle"
mock last:                  "LastName"
mock [full] name:           "Person\tMiddle\tLastName"
mock street:                "1234 Main St"
mock city:                  "City"
mock (zip | postal):        "12345"

mock address full:
    key(down tab)
    "1234 Main St\t\t\tCity\t"
    key(down tab)
    "12345"

mock address mid:
    key(down tab)
    "1234 Main St\t\tCity\t"
    key(down tab)
    "12345"

mock address:
    key(down tab)
    "1234 Main St\tCity"
    sleep(400ms)
    key(tab)
    sleep(400ms)
    key(down tab)
    "12345"

mock date [<number>]:
    key(down tab)
    insert(3)
    key(tab)
    insert(number or "1999")

mock employment:
    # mimic("click do you have any employment")
    key(tab space tab:2 enter)
    sleep(500ms)
    key(tab)
    insert("Employer")
    key(tab)
    sleep(500ms)
    key(down)
    sleep(50ms)
    key(tab)
    sleep(50ms)
    "1234 Main St\tCity"
    sleep(400ms)
    key(tab)
    sleep(400ms)
    key(down tab)
    "12345"
    key(tab:2 enter)
