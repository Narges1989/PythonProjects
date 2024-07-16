from to_do import TODO


def task11(guests: list[str]) -> int:
    return len(guests)

if __name__ == "__main__":
    guest_list = [
        "Stéphanie-A",
        "Edmée-K",
        "Maëlla-K",
        "Océanne-K",
        "Géraldine-K",
        "Maëline-K",
    ]

    # NOTE: Uncomment the code below when you are ready to test your answers
    print(f"The event has a total of {task11(guest_list)} guests.")
