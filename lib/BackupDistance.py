while True:
    try:
        print((sonar.distance,))
        if (sonar.distance < 5):
             print("less than 5")
        if (sonar.distance > 5):
             print("less than 5")     
        if (sonar.distance > 5):
             print("more than 5")  
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)