from to_do import TODO


def task18(customers: list[str]) -> list[str]:
    result = []
    for email in customers:
        splited_email = email.split('@')[1]

        if splited_email.split('.')[0] not in result:
            result.append(splited_email.split('.')[0])
    return result


if __name__ == "__main__":
    customer_list = [
        "tgundrey1l@prlog.org",
        "bgrix1u@apache.org",
        "mbreakspear1v@wordpress.com",
        "cdalli1w@ft.com",
        "rclayborn1x@mtv.com",
        "rclayborn1x@mtv.com",
        "jchidlow1y@nasa.gov",
        "jchidlow1y@nasa.gov",
        "kovell1z@washingtonpost.com",
        "kovell1z@washingtonpost.com",
        "kovell1z@washingtonpost.com",
    ]

    print(f"The companies that purchased from you include: {task18(customer_list)}")
