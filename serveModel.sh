
# Location of demo models
TESTDATA="$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata"

# Start TensorFlow Serving container and open the REST API port
docker run -p 8501:8501 --name crypto \
--mount type=bind,source=/Users/jonathantiritilli/tmp,target=/models/crypto \
-e MODEL_NAME=crypto -t tensorflow/serving

# Query the model using the predict API
# curl -d '{"instances": [1.0, 2.0, 5.0]}' \
#     -X POST http://localhost:8501/v1/models/crypto:predict

# Returns => { "predictions": [2.5, 3.0, 4.5] }