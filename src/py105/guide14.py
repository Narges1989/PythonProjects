from to_do import TODO


def guide14(scandinavia: dict[str, str]) -> dict[str, str]:
    Scandinavian_country = ['denmark', 'norway', 'sweden', 'finland', 'iceland', 'faroe islands', 'greenland', 'åland']
    countries = list(scandinavia.keys())
    # for country in countries:
    #     if country.lower() not in Scandinavian_country:
    #         del scandinavia[country]
    # return scandinavia

    #solution 2
    # result ={}
    # for country_name,language in scandinavia.items():
    #     if country_name.lower() in Scandinavian_country:
    #         result[country_name] = language
    # return result

    #solution3: dictionary comprehension
    #return {country_name: language for country_name,language in scandinavia.items() if country_name.lower() in Scandinavian_country}

    # solution4: filter
    return dict(filter(lambda items:items[0].lower() in Scandinavian_country,scandinavia.items()))