import math

def sobel_edges(image: list) -> list:
    """
    Returns the zero-padded Sobel gradient magnitude at every pixel.
    """
    # Write code here
    
    Kx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    Ky = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]

    rows = len(image)
    cols = len(image[0])

    output = [[0] * cols for _ in range(rows)]

    padded = [[0] * (cols + 2) for _ in range(rows + 2)]

    for i in range(rows):
        for j in range(cols):
            padded[i + 1][j + 1] = image[i][j]

    for i in range(rows):
        for j in range(cols):

            Gx = 0
            Gy = 0

            for a in range(3):
                for b in range(3):
                    pixel = padded[i + a][j + b]

                    Gx += Kx[a][b] * pixel
                    Gy += Ky[a][b] * pixel

            G = math.sqrt(Gx ** 2 + Gy ** 2)

            output[i][j] = G

    return output
    pass