import mnist_loader
import matplotlib.pyplot as plt
import numpy as np

def visualize_MNIST(sample, title = None, cmap = "Greys"):
    """
    A function for visualizing data samples from the MNIST database
    
    Note that the greyscale is inversed, consequently the traditional black
    background is white.
    """
    if len(sample.shape) == 2:
        img = np.array(np.split(sample, 28))[:, :, 0]
    else:
        img = np.array(np.split(sample, 28))
    
    plt.matshow(img, cmap=cmap)
    plt.axis('off')
    if title:
        plt.title(title)

if __name__ == "__main__":
    train_data, val_data, test_data = mnist_loader.load_data_wrapper()
    sample = train_data[0][0]
    solution = np.argmax(train_data[0][1])
    visualize_MNIST(sample, title=f"Solution: {solution} - Prediction: ?")
    plt.savefig('img/sample.png')