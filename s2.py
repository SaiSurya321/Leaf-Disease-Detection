import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('D:/PROJECT SPRING 2025/models_codes/models/best_model_fold_banana5.keras')

# Verify the model loaded by printing a summary
model.summary()
