import json

# Function to calculate Lagrange basis polynomials and interpolate
def lagrange_interpolation(points, x_val):
    def L(k, x):
        # Calculate the Lagrange basis polynomial L_k(x)
        result = 1
        x_k, _ = points[k]
        for i, (x_i, _) in enumerate(points):
            if i != k:
                result *= (x - x_i) / (x_k - x_i)
        return result

    # Summing up y_k * L_k(x_val) for all points
    result = 0
    for k, (_, y_k) in enumerate(points):
        result += y_k * L(k, x_val)
    
    return result

# Test Case 1 JSON input
json_input_1 = '''{
  "points": [
    {"x": 1, "y": 5},
    {"x": 2, "y": 9},
    {"x": 3, "y": 15}
  ]
}'''

# Test Case 2 JSON input
json_input_2 = '''{
  "points": [
    {"x": 1, "y": 4},
    {"x": 3, "y": 10},
    {"x": 5, "y": 18}
  ]
}'''

# Parse the JSON for Test Case 1
data_1 = json.loads(json_input_1)
points_1 = [(p['x'], p['y']) for p in data_1['points']]
# Find the constant term for Test Case 1
constant_term_1 = lagrange_interpolation(points_1, 0)
print(f"Test Case 1 - Constant term c is: {constant_term_1}")

# Parse the JSON for Test Case 2
data_2 = json.loads(json_input_2)
points_2 = [(p['x'], p['y']) for p in data_2['points']]
# Find the constant term for Test Case 2
constant_term_2 = lagrange_interpolation(points_2, 0)
print(f"Test Case 2 - Constant term c is: {constant_term_2}")
