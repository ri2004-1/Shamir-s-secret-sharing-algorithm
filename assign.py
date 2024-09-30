import json

# Function to decode Y values based on different bases
def decode_y_values(y_values, base):
    return [int(y, base) for y in y_values]

# Lagrange Interpolation function to find the polynomial value at a given x
def lagrange_interpolation(points, x_val):
    def L(k, x):
        result = 1
        x_k, _ = points[k]
        for i, (x_i, _) in enumerate(points):
            if i != k:
                result *= (x - x_i) / (x_k - x_i)
        return result

    result = 0
    for k, (_, y_k) in enumerate(points):
        result += y_k * L(k, x_val)
    
    return result

# Function to identify wrong points in a test case
def find_wrong_points(points):
    wrong_points = []
    for i, (x, y) in enumerate(points):
        interpolated_y = lagrange_interpolation(points, x)
        if abs(interpolated_y - y) > 1e-6:  # Allow small numerical differences
            wrong_points.append((x, y))
    return wrong_points

# Function to process each test case
def process_test_case(data):
    # Extract base and points
    base = data['base']
    points = [(p['x'], p['y']) for p in data['points']]
    
    # Decode the Y-values based on the given base
    decoded_points = [(x, int(y, base)) for x, y in points]

    # Calculate the secret (constant term) by evaluating at x = 0
    secret_c = lagrange_interpolation(decoded_points, 0)
    
    # If this is the second test case, we will check for wrong points
    wrong_points = find_wrong_points(decoded_points) if 'imposter_points' in data else []

    return secret_c, wrong_points

# Main function to handle multiple test cases
def main():
    # Test case 1 in JSON format
    test_case_1 = {
        "base": 10,
        "points": [
            {"x": 1, "y": "5"},
            {"x": 2, "y": "9"},
            {"x": 3, "y": "15"}
        ]
    }
    
    # Test case 2 in JSON format (with a hexadecimal base)
    test_case_2 = {
        "base": 16,
        "points": [
            {"x": 1, "y": "4"},
            {"x": 3, "y": "A"},  # Hexadecimal "A" = 10 in decimal
            {"x": 5, "y": "12"}
        ],
        "imposter_points": True
    }
    
    # Process test case 1
    secret_c_1, wrong_points_1 = process_test_case(test_case_1)
    print(f"Secret for test case 1: {secret_c_1}")
    
    # Process test case 2
    secret_c_2, wrong_points_2 = process_test_case(test_case_2)
    print(f"Secret for test case 2: {secret_c_2}")
    
    # If there are wrong points in test case 2, print them
    if wrong_points_2:
        print(f"Wrong points in test case 2: {wrong_points_2}")
    else:
        print(f"No wrong points in test case 2.")

if __name__ == "__main__":
    main()
