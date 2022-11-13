from collections import deque

def main():
    #add code here
    foods = deque(maxlen=5)
    foods.append("STA001")
    ordered_foods = ["DESCO3", "STA002", "ENTO04", "ENTO01"]
    foods.extend(ordered_foods)
    foods.append("DES002")
    print(foods)
    return

if __name__ == "__main__":
    main()