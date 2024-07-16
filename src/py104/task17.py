from to_do import TODO


def task17(customers: list[str]) -> list[str]:
    result = []
    for email in customers:
        if customers.count(email)>1 and email not in result:
            result.append(email)
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

    print(
        f"The customers that purchased multiple times include: {task17(customer_list)}"
    )
