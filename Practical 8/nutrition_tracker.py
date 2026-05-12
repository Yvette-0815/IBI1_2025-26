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
    print(f"Total calories: {total_calories:.2f} kcal")
    print(f"Total protein: {total_protein:.2f} g")
    print(f"Total carbs: {total_carbs:.2f} g")
    print(f"Total fat: {total_fat:.2f} g")
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
    daily_diet = []
    print("=== Daily Nutrition Tracker ===")
    print("Please enter the foods you ate today.")
    print("Type 'done' when you have finished entering all foods.")
    print("-" * 30)
    while True:
        name = input("Enter food name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            calories = float(input("Enter calories (kcal): "))
            protein = float(input("Enter protein (g): "))
            carbs = float(input("Enter carbohydrates (g): "))
            fat = float(input("Enter fat (g): "))
            new_food = FoodItem(name, calories, protein, carbs, fat)
            daily_diet.append(new_food)
        except ValueError:
            print("Invalid input. Please enter numbers for nutrition values.")
        totals = calculate_daily_nutrition(daily_diet)
        print("<br/>Calculation complete.")
        print("\nThe returned summary dictionary:\n", totals)

input("Press enter to exit.")
