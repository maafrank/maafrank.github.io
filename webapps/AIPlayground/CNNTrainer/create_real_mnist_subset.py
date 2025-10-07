#!/usr/bin/env python3
"""
Create a real MNIST subset from actual MNIST data
Downloads the real CSV files and creates a subset to stay under GitHub's 100MB limit
"""

import pandas as pd
import requests
import json
import os

def download_mnist_csv():
    """Download real MNIST CSV files"""
    train_url = "https://pjreddie.com/media/files/mnist_train.csv"
    test_url = "https://pjreddie.com/media/files/mnist_test.csv"
    
    print("Downloading real MNIST training data...")
    train_response = requests.get(train_url)
    with open("mnist_train.csv", "wb") as f:
        f.write(train_response.content)
    
    print("Downloading real MNIST test data...")
    test_response = requests.get(test_url)
    with open("mnist_test.csv", "wb") as f:
        f.write(test_response.content)
    
    print("Download complete!")

def create_real_mnist_subset():
    """Create subset from real MNIST data"""
    
    # Check if CSV files exist, download if not
    if not os.path.exists("mnist_train.csv") or not os.path.exists("mnist_test.csv"):
        download_mnist_csv()
    
    print("Loading real MNIST training data...")
    train_df = pd.read_csv("mnist_train.csv", header=None)
    
    print("Loading real MNIST test data...")  
    test_df = pd.read_csv("mnist_test.csv", header=None)
    
    # Take subset to stay under 100MB
    # Target: ~1200 training samples (120 per digit) + 300 test samples (30 per digit)
    train_subset = []
    test_subset = []
    
    # Training subset - 120 samples per digit
    for digit in range(10):
        digit_samples = train_df[train_df.iloc[:, 0] == digit].head(120)
        train_subset.append(digit_samples)
    
    train_subset_df = pd.concat(train_subset).sample(frac=1).reset_index(drop=True)
    
    # Test subset - 30 samples per digit  
    for digit in range(10):
        digit_samples = test_df[test_df.iloc[:, 0] == digit].head(30)
        test_subset.append(digit_samples)
        
    test_subset_df = pd.concat(test_subset).sample(frac=1).reset_index(drop=True)
    
    print(f"Created training subset: {len(train_subset_df)} samples")
    print(f"Created test subset: {len(test_subset_df)} samples")
    
    return train_subset_df, test_subset_df

def create_js_dataset(train_df, test_df):
    """Convert to JavaScript format"""
    
    train_images = []
    train_labels = []
    
    for _, row in train_df.iterrows():
        label = int(row.iloc[0])
        pixels = [float(x)/255.0 for x in row.iloc[1:].values]  # Normalize to 0-1
        train_images.append(pixels)
        train_labels.append(label)
    
    test_images = []
    test_labels = []
    
    for _, row in test_df.iterrows():
        label = int(row.iloc[0])
        pixels = [float(x)/255.0 for x in row.iloc[1:].values]  # Normalize to 0-1
        test_images.append(pixels)
        test_labels.append(label)
    
    # Write JavaScript file
    with open("real_mnist_data_subset.js", "w") as f:
        f.write("// REAL MNIST Dataset Subset - Actual handwritten digits from MNIST database\n")
        f.write("// Source: http://yann.lecun.com/exdb/mnist/\n")
        f.write(f"// {len(train_images)} training + {len(test_images)} test samples\n\n")
        
        f.write("window.REAL_MNIST_DATA = {\n")
        f.write("    metadata: {\n")
        f.write('        description: "Real MNIST handwritten digits subset",\n')
        f.write('        source: "http://yann.lecun.com/exdb/mnist/",\n')
        f.write(f'        total_samples: {len(train_images) + len(test_images)},\n')
        f.write(f'        train_samples: {len(train_images)},\n')
        f.write(f'        test_samples: {len(test_images)}\n')
        f.write("    },\n")
        
        # Training data
        f.write("    train: {\n")
        f.write("        images: [\n")
        
        for i, image in enumerate(train_images):
            if i > 0:
                f.write(",\n")
            f.write("            [" + ",".join(f"{x:.3f}" for x in image) + "]")
            
            if i % 50 == 0:
                print(f"Written {i+1}/{len(train_images)} training samples...")
        
        f.write("\n        ],\n")
        f.write("        labels: [" + ",".join(map(str, train_labels)) + "]\n")
        f.write("    },\n")
        
        # Test data
        f.write("    test: {\n")
        f.write("        images: [\n")
        
        for i, image in enumerate(test_images):
            if i > 0:
                f.write(",\n")
            f.write("            [" + ",".join(f"{x:.3f}" for x in image) + "]")
            
            if i % 50 == 0:
                print(f"Written {i+1}/{len(test_images)} test samples...")
        
        f.write("\n        ],\n")
        f.write("        labels: [" + ",".join(map(str, test_labels)) + "]\n")
        f.write("    }\n")
        f.write("};\n")

if __name__ == "__main__":
    print("Creating REAL MNIST subset for GitHub Pages...")
    
    train_df, test_df = create_real_mnist_subset()
    create_js_dataset(train_df, test_df)
    
    print(f"\nReal MNIST subset created successfully!")
    print(f"File: real_mnist_data_subset.js")
    
    # Check file size
    size_mb = os.path.getsize("real_mnist_data_subset.js") / (1024 * 1024)
    print(f"File size: {size_mb:.1f} MB")
    
    if size_mb > 90:
        print("⚠️  Warning: File may be close to GitHub's 100MB limit")
    else:
        print("✅ File size is safe for GitHub Pages")