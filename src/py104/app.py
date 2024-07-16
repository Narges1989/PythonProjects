if __name__ == "__main__":
    # create a variable
    country = 'Panama'
    print(f'My country is {country}')

    # collection of countries
    countries = ['Panama','Sweden','Spain']
    print(f'My favourite countries are {countries}')

    # how to create lists
    # method 1: []
    capitals = ['Panama','Stockholm']
    print(f'A campital from each country= {capitals}')

    #method 2: list()
    cities = list(('Colon','Gbg','Valencia'))
    print(f'A city from each country= {cities}')


    countries.append('Intaly')
    print(f'My favourite countries are {countries}')
