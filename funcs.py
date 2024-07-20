def func_generator(point1: list|tuple[int|float,int|float,int|float], point2: list|tuple[int|float,int|float,int|float]) -> tuple[tuple[float,float],tuple[float,float],tuple[float,float]]:

    x1 = point1[0]
    y1 = point1[1]
    z1 = point1[2]
    
    x2 = point2[0]
    y2 = point2[1]
    z2 = point2[2]

    ax = (y1-y2)/(x1-x2)
    bx = y1 - ax*x1

    new_x1 = ax*x1+bx
    new_x2 = ax*x2+bx

    az = (new_x1-new_x2)/(z1-z2)
    bz = new_x1 - az*z1

    return ((ax,bx),(1,0),(az,bz))
