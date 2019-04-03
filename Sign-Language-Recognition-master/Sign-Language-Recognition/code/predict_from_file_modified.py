#!/usr/bin/env python2
import sys
import traceback
import os
import cv2
from sklearn.externals import joblib

from common.config import get_config
from common.image_transformation import apply_image_transformation


def main():
    model_name = sys.argv[1]
    if model_name not in ['svm', 'logistic', 'knn']:
        print("Invalid model-name '{}'!".format(model_name))
        return

    print("Using model '{}'...".format(model_name))

    model_serialized_path = get_config(
        'model_{}_serialized_path'.format(model_name))
    print("Model deserialized from path '{}'".format(model_serialized_path))
    for root , dir , filex in os.walk("C:/xampp/htdocs/file_upload_api/files/", topdown=True):
        image_path = "C:/xampp/htdocs/file_upload_api/files/" + filex[0]
        break
    frame = cv2.imread(image_path)
    try:
        frame = apply_image_transformation(frame)
        frame_flattened = frame.flatten()
        classifier_model = joblib.load(model_serialized_path)
        predicted_labels = classifier_model.predict(frame_flattened.reshape(1,-1))
        predicted_label = predicted_labels[1]
        print("Predicted labelx={}".format(predicted_label))
    except Exception:
        exception_traceback = traceback.format_exc()
        print("Error while applying image transformation on image path '{}' with the following exception trace:\n{}".format(image_path, exception_traceback))
    #os.remove(image_path)
    cv2.destroyAllWindows()
    print "The program completed successfully !!"


if __name__ == '__main__':
    main()
