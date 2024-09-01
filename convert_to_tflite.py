import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('fall_detection_model.h5')

# Convert the model to TensorFlow Lite with Select_TF_OPS
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,tf.lite.OpsSet.SELECT_TF_OPS]


#Experimental options to handle TensorflowListReserve issue
converter.experimental_lower_tensor_list_ops = False
converter.experimental_enable_resource_variables = True

#Convert the model
tflite_model = converter.convert()

#Save the TensorFlow Lite model
with open('fall_detection_model.tflite', 'wb') as f:
    f.write(tflite_model)
