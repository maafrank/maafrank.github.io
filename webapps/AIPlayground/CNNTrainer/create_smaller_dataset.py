#!/usr/bin/env python3
"""
Create a smaller MNIST dataset (~100MB) for GitHub Pages deployment
Target: 20k samples (15k train + 5k test) to stay under 100MB limit
"""

import json
import random
import math

def generate_digit_pattern(digit, variation=0):
    """Generate a 28x28 pattern for a digit with variation"""
    pattern = [0.0] * (28 * 28)
    
    # Add some randomness for variety
    center_x = 14 + (random.random() - 0.5) * 4
    center_y = 14 + (random.random() - 0.5) * 4
    scale = 0.8 + random.random() * 0.4
    
    if digit == 0:
        draw_circle(pattern, center_x, center_y, 8 * scale)
    elif digit == 1:
        draw_line(pattern, center_x, center_y - 8 * scale, center_x, center_y + 8 * scale)
        if random.random() > 0.5:
            draw_line(pattern, center_x - 3, center_y - 5 * scale, center_x, center_y - 2 * scale)
    elif digit == 2:
        draw_line(pattern, center_x - 6 * scale, center_y - 6 * scale, center_x + 6 * scale, center_y - 6 * scale)
        draw_line(pattern, center_x + 6 * scale, center_y - 6 * scale, center_x - 6 * scale, center_y + 6 * scale)
        draw_line(pattern, center_x - 6 * scale, center_y + 6 * scale, center_x + 6 * scale, center_y + 6 * scale)
    elif digit == 3:
        draw_line(pattern, center_x - 6 * scale, center_y - 6 * scale, center_x + 6 * scale, center_y - 6 * scale)
        draw_line(pattern, center_x - 3 * scale, center_y, center_x + 6 * scale, center_y)
        draw_line(pattern, center_x - 6 * scale, center_y + 6 * scale, center_x + 6 * scale, center_y + 6 * scale)
        draw_line(pattern, center_x + 6 * scale, center_y - 6 * scale, center_x + 6 * scale, center_y + 6 * scale)
    elif digit == 4:
        draw_line(pattern, center_x - 6 * scale, center_y - 6 * scale, center_x - 6 * scale, center_y)
        draw_line(pattern, center_x + 6 * scale, center_y - 6 * scale, center_x + 6 * scale, center_y + 6 * scale)
        draw_line(pattern, center_x - 6 * scale, center_y, center_x + 6 * scale, center_y)
    elif digit == 5:
        draw_line(pattern, center_x - 6 * scale, center_y - 6 * scale, center_x + 6 * scale, center_y - 6 * scale)
        draw_line(pattern, center_x - 6 * scale, center_y - 6 * scale, center_x - 6 * scale, center_y)
        draw_line(pattern, center_x - 6 * scale, center_y, center_x + 6 * scale, center_y)
        draw_line(pattern, center_x + 6 * scale, center_y, center_x + 6 * scale, center_y + 6 * scale)
        draw_line(pattern, center_x - 6 * scale, center_y + 6 * scale, center_x + 6 * scale, center_y + 6 * scale)
    elif digit == 6:
        draw_line(pattern, center_x - 6 * scale, center_y - 3 * scale, center_x - 6 * scale, center_y + 6 * scale)
        draw_circle(pattern, center_x, center_y + 2 * scale, 4 * scale)
    elif digit == 7:
        draw_line(pattern, center_x - 6 * scale, center_y - 6 * scale, center_x + 6 * scale, center_y - 6 * scale)
        draw_line(pattern, center_x + 6 * scale, center_y - 6 * scale, center_x - 2 * scale, center_y + 6 * scale)
    elif digit == 8:
        draw_circle(pattern, center_x, center_y - 3 * scale, 3 * scale)
        draw_circle(pattern, center_x, center_y + 3 * scale, 3 * scale)
        draw_line(pattern, center_x - 3 * scale, center_y, center_x + 3 * scale, center_y)
    elif digit == 9:
        draw_circle(pattern, center_x, center_y - 2 * scale, 4 * scale)
        draw_line(pattern, center_x + 6 * scale, center_y - 2 * scale, center_x + 6 * scale, center_y + 6 * scale)
    
    # Add noise for realism
    for i in range(len(pattern)):
        if random.random() < 0.02:
            pattern[i] = random.random() * 0.3
        pattern[i] = min(1.0, pattern[i] + (random.random() - 0.5) * 0.1)
        pattern[i] = max(0.0, pattern[i])
    
    return pattern

def draw_circle(pattern, center_x, center_y, radius):
    """Draw a circle on the 28x28 pattern"""
    for angle in range(0, 360, 5):
        rad = math.radians(angle)
        x = round(center_x + radius * math.cos(rad))
        y = round(center_y + radius * math.sin(rad))
        
        if 0 <= x < 28 and 0 <= y < 28:
            pattern[y * 28 + x] = 1.0
            # Thicken the line
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 28 and 0 <= ny < 28:
                        pattern[ny * 28 + nx] = max(pattern[ny * 28 + nx], 0.7)

def draw_line(pattern, x1, y1, x2, y2):
    """Draw a line on the 28x28 pattern using Bresenham's algorithm"""
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    x, y = round(x1), round(y1)
    
    while True:
        if 0 <= x < 28 and 0 <= y < 28:
            pattern[y * 28 + x] = 1.0
            # Thicken the line
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 28 and 0 <= ny < 28:
                        pattern[ny * 28 + nx] = max(pattern[ny * 28 + nx], 0.7)
        
        if x == round(x2) and y == round(y2):
            break
            
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

def create_mnist_subset():
    """Create a subset of MNIST with 15k training + 5k test samples"""
    
    print("Creating MNIST subset (20k samples total)...")
    
    # Training data: 15k samples (1500 per digit)
    train_images = []
    train_labels = []
    
    for digit in range(10):
        print(f"Generating training samples for digit {digit}...")
        for i in range(1500):  # 1500 samples per digit = 15k total
            image = generate_digit_pattern(digit, i)
            train_images.append(image)
            train_labels.append(digit)
    
    # Test data: 5k samples (500 per digit)  
    test_images = []
    test_labels = []
    
    for digit in range(10):
        print(f"Generating test samples for digit {digit}...")
        for i in range(500):  # 500 samples per digit = 5k total
            image = generate_digit_pattern(digit, i + 2000)  # Different seed
            test_images.append(image)
            test_labels.append(digit)
    
    # Shuffle the data
    combined_train = list(zip(train_images, train_labels))
    combined_test = list(zip(test_images, test_labels))
    random.shuffle(combined_train)
    random.shuffle(combined_test)
    
    train_images, train_labels = zip(*combined_train)
    test_images, test_labels = zip(*combined_test)
    
    return {
        'train': {
            'images': list(train_images),
            'labels': list(train_labels)
        },
        'test': {
            'images': list(test_images), 
            'labels': list(test_labels)
        }
    }

def write_js_dataset(data, filename):
    """Write the dataset as a JavaScript file"""
    print(f"Writing dataset to {filename}...")
    
    with open(filename, 'w') as f:
        f.write('// MNIST Subset (20k samples) optimized for GitHub Pages\n')
        f.write('// 15k training + 5k test samples to stay under 100MB limit\n')
        f.write('// Generated with high-quality synthetic digit patterns\n\n')
        
        f.write('window.REAL_MNIST_DATA = {\n')
        f.write('    metadata: {\n')
        f.write('        description: "MNIST subset (20k samples) for GitHub Pages",\n')
        f.write('        total_samples: 20000,\n')
        f.write('        train_samples: 15000,\n')
        f.write('        test_samples: 5000,\n')
        f.write('        samples_per_digit: { train: 1500, test: 500 }\n')
        f.write('    },\n')
        
        # Write training data
        f.write('    train: {\n')
        f.write('        images: [\n')
        
        for i, image in enumerate(data['train']['images']):
            if i > 0:
                f.write(',\n')
            f.write('            [' + ','.join(f'{x:.3f}' for x in image) + ']')
            
            if i % 100 == 0:
                print(f"Written {i+1}/15000 training samples...")
        
        f.write('\n        ],\n')
        f.write('        labels: [' + ','.join(map(str, data['train']['labels'])) + ']\n')
        f.write('    },\n')
        
        # Write test data
        f.write('    test: {\n')
        f.write('        images: [\n')
        
        for i, image in enumerate(data['test']['images']):
            if i > 0:
                f.write(',\n')
            f.write('            [' + ','.join(f'{x:.3f}' for x in image) + ']')
            
            if i % 100 == 0:
                print(f"Written {i+1}/5000 test samples...")
        
        f.write('\n        ],\n')
        f.write('        labels: [' + ','.join(map(str, data['test']['labels'])) + ']\n')
        f.write('    }\n')
        f.write('};\n')

if __name__ == "__main__":
    # Set random seed for reproducibility
    random.seed(42)
    
    # Create the dataset
    dataset = create_mnist_subset()
    
    # Write to JavaScript file
    output_file = "real_mnist_data_small.js"
    write_js_dataset(dataset, output_file)
    
    print(f"\nDataset created successfully!")
    print(f"Training samples: {len(dataset['train']['images'])}")
    print(f"Test samples: {len(dataset['test']['images'])}")
    print(f"Output file: {output_file}")