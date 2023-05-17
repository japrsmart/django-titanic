def fake_predict(user_age):
    if user_age > 10:
        prediction = "survive >10"
    else:
        prediction = "super survive <10"
    return prediction
