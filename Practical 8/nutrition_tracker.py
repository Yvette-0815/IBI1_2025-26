class FoodItem:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
    def __repr__(self):
        return (f"FoodItem(name = '{self.name}', calories = {self.calories}, "
                f"protein = {self.protein}, carbs = {self.carbs}, fat = {self.fat})")

def calculate_daily_nutrition(food_list):
    food_list: dict
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat
    print("=== 24-hour Mutritional Intake Summary ===")
    print(f"Total calories: {total_calories:.2f} kilocalories")
    print(f"Total protein: {total_protein:.2f} grams")
    print(f"Total carbs: {total_carbs:.2f} grams")
    print(f"Total fat: {total_fat:.2f} grams")
    WARNING_CALORIES = 2500
    WARNING_FAT = 90
    warnings = []
    if total_calories > WARNING_CALORIES:
        warnings.append(f"Warning: Caloric intake ({total_calories:.2f} kilocalories) exceeds the recommended level {WARNING_CALORIES} kilocalories.")
    if total_fat > WARNING_FAT:
        warnings.append(f"Warning: Fat intake ({total_fat:.2f} grams) exceeds the recommended level {WARNING_FAT} grams.")
    if warnings:
        print("\n--- Health Warning ---")            
        for warning in warnings:
            print(warning)
    else:
        print("Today's intake has not exceed the recommended limit.")
    return {
        'calories': total_calories,
        'protein': total_protein,
        'carbs': total_carbs,
        'fat': total_fat
        }

if __name__ == "__main__":
    apple = FoodItem("Apple", 60, 0.3, 15, 0.5)
    sandwich = FoodItem("Chicken Sandwich", 450, 25, 40, 20)
    pasta = FoodItem("Pasta with Sauce", 600, 18, 85, 22)
    salad = FoodItem("Greek Salad", 350, 12, 10, 28)
    pizza = FoodItem("Pizza Slice", 300, 12, 36, 12)
    daily_diet = [apple, sandwich, pasta, salad, pizza]
    totals = calculate_daily_nutrition(daily_diet)
    print("\nThe returned summary dictionary:\n", totals)

input("Press enter to exit.")