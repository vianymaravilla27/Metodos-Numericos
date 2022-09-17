# Definimos ahora las cuadraturas que emplearemos, tanto abiertas como cerradas

# Cuadraturas cerradas
def cerrada1(fx, a, b):
    
    # Número de puntos
    n = 1
    
    # Calculamos h, es decir, la distancia entre los puntos:
    h = (b - a) / n
    
    # Evaluamos los puntos
    eval = [fx(a + i * h) for i in range(n + 1)]
    
    # Calculamos la cuadratura
    cuadratura = (eval[0] + eval[1]) * (h / 2)
    
    return cuadratura

# Cuadraturas cerradas
def cerrada2(fx, a, b):
    
    # Número de puntos
    n = 2
    
    # Calculamos h, es decir, la distancia entre los puntos:
    h = (b - a) / n
    
    # Evaluamos los puntos
    eval = [fx(a + i * h) for i in range(n + 1)]
    
    # Calculamos la cuadratura
    cuadratura = (eval[0] + 4 * eval[1] + eval[2]) * (h / 3)
    
    return cuadratura

# Cuadraturas cerradas
def cerrada3(fx, a, b):
    
    # Número de puntos
    n = 3
    
    # Calculamos h, es decir, la distancia entre los puntos:
    h = (b - a) / n
    
    # Evaluamos los puntos
    eval = [fx(a + i * h) for i in range(n + 1)]
    
    # Calculamos la cuadratura
    cuadratura = (eval[0] + 3 * eval[1] + 3 * eval[2] + eval[3]) * (3 * h / 8)
    
    return cuadratura

def cerrada4(fx, a, b):
    
    # Número de puntos
    n = 4
    
    # Calculamos h, es decir, la distancia entre los puntos:
    h = (b - a) / n
    
    # Evaluamos los puntos
    eval = [fx(a + i * h) for i in range(n + 1)]
    
    # Calculamos la cuadratura
    cuadratura = (7 * eval[0] + 32 * eval[1] + 12 * eval[2] + 32 * eval[3] + 7 * eval[4]) * (2 * h / 45)
    
    return cuadratura

# Cuadraturas abiertas
def abierta1(fx, a, b):
    
    # Número de puntos
    n = 0
    
    # Calculamos h, es decir, la distancia entre los puntos:
    h = (b - a) / (n + 2)
    
    # Evaluamos los puntos
    eval = [fx(a + i * h) for i in range(1, n + 2)]
    
    # Calculamos la cuadratura
    cuadratura = eval[0] * (2 * h)
    
    return cuadratura

# Cuadraturas cerradas
def abierta2(fx, a, b):
    
    # Número de puntos
    n = 1
    
    # Calculamos h, es decir, la distancia entre los puntos:
    h = (b - a) / (n + 2)
    
    # Evaluamos los puntos
    eval = [fx(a + i * h) for i in range(1, n + 2)]
    
    # Calculamos la cuadratura
    cuadratura = (eval[0] + eval[1]) * (3 * h / 2)
    
    return cuadratura

# Cuadraturas cerradas
def abierta3(fx, a, b):
    
    # Número de puntos
    n = 2
    
    # Calculamos h, es decir, la distancia entre los puntos:
    h = (b - a) / (n + 2)
    
    # Evaluamos los puntos
    eval = [fx(a + i * h) for i in range(1, n + 2)]
    
    # Calculamos la cuadratura
    cuadratura = (2 * eval[0] - eval[1] + 2 * eval[2]) * (4 * h / 3)
    
    return cuadratura

def abierta4(fx, a, b):
    
    # Número de puntos
    n = 3
    
    # Calculamos h, es decir, la distancia entre los puntos:
    h = (b - a) / (n + 2)
    
    # Evaluamos los puntos
    eval = [fx(a + i * h) for i in range(1, n + 2)]
    
    # Calculamos la cuadratura
    cuadratura = (11 * eval[0] + eval[1] + eval[2] + 11 * eval[3]) * (5 * h / 24)
    
    return cuadratura