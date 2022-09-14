phones = ["iPhone 14", "iPhone 14 Plus", "iPhone 14 Pro", "iPhone 14 Pro Max"]


def do_some_operation_on_phone_list(phone_list):
    phone_list[0] = "iPhone 14 Mini"
    print(phone_list)


do_some_operation_on_phone_list(list(phones))
print(phones)
