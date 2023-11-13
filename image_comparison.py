# import required libraries
import cv2
import numpy as np

def mse(image1, image2, common_width, common_height):
    # Resize images to a common size
    image1 = cv2.resize(image1, (common_width, common_height))
    image2 = cv2.resize(image2, (common_width, common_height))

    # Compute the Mean Squared Error (MSE) between the two images
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])

    # Return the MSE and the difference image (optional)
    return err, image1 - image2

def compare_images(image_path1, image_path2):
    # load the input images
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    # Check if images are loaded successfully
    if img1 is None or img2 is None:
        print("Error: Unable to load images.")
        return

    # Ensure images have the same dimensions
    common_width = min(img1.shape[1], img2.shape[1])
    common_height = min(img1.shape[0], img2.shape[0])

    # Resize images to a common size
    img1 = cv2.resize(img1, (common_width, common_height))
    img2 = cv2.resize(img2, (common_width, common_height))

    # convert the images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    error, diff = mse(img1, img2, common_width, common_height)
    print("Image matching Error between the two images:",error)

    cv2.imshow("difference", diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()