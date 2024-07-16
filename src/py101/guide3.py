from to_do import TODO


def guide3() -> str:
    return """
        INPUT please enter your country name
        IF country in Europe continent:
            OUTPUT Europe
        ELSE IF country in North America continent:
            OUTPUT North America
        ELSE IF country in South America continent:
            OUTPUT South America
        ELSE IF country in Asia continent:
            OUTPUT Asia
        ELSE IF country in Africa continent:
            OUTPUT Africa
        ELSE IF country in Oceania continent:
            OUTPUT Oceania
        ELSE country in Antartica continent:
            OUTPUT Antartica
        ELSE:
            Error
    """
