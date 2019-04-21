from matplotlib import pyplot as plt

def draw_dataset(res, data,theta0, theta1):

     # line = theta0 * x + theta1
    x1 = 0
    y1 = theta1*x1 + theta0
    print(data['max_y'])
    x2 = data['max_y']
    y2 = theta1*x2 + theta0
    plt.title("ft_linear_regression", fontsize=20)
    plt.xlabel('Km')
    plt.ylabel('Price')
    km, mileage = zip(*res.items())
    plt.plot(km, mileage, "b*")
    plt.plot([y1, y2], [x1, x2], "y")
    plt.show()
