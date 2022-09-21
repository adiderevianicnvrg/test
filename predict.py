def predict(sentence):
    encoded = encode_sentence(sentence)
    pred = np.array([encoded])
    pred = vectorize_sequences(pred)
    a = model.predict(pred)
    return str(a[0][0])
