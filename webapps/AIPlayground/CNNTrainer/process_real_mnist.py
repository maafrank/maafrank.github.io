#!/usr/bin/env python3
"""
Process REAL MNIST CSV files into a JavaScript subset for GitHub Pages
Uses the actual MNIST data you downloaded, not synthetic data
"""

import pandas as pd
import numpy as np
import os

def process_real_mnist():
    """Process the real MNIST CSV files"""
    
    train_path = "/Users/matthewfrank/Downloads/mnist_train.csv" 
    test_path = "/Users/matthewfrank/Downloads/mnist_test.csv"
    
    print("Loading REAL MNIST training data...")
    train_df = pd.read_csv(train_path, header=None)
    print(f"Loaded {len(train_df)} real training samples")
    
    print("Loading REAL MNIST test data...")
    test_df = pd.read_csv(test_path, header=None)
    print(f"Loaded {len(test_df)} real test samples")
    
    # Create balanced subset - 120 samples per digit for training, 30 for test
    print("Creating balanced subset from real data...")
    
    train_subset = []
    test_subset = []
    
    for digit in range(10):
        # Training subset - 120 real samples per digit
        digit_train = train_df[train_df.iloc[:, 0] == digit].head(120)
        train_subset.append(digit_train)
        print(f"Selected {len(digit_train)} real training samples for digit {digit}")
        
        # Test subset - 30 real samples per digit
        digit_test = test_df[test_df.iloc[:, 0] == digit].head(30)
        test_subset.append(digit_test)
        print(f"Selected {len(digit_test)} real test samples for digit {digit}")
    
    # Combine and shuffle
    train_subset_df = pd.concat(train_subset).sample(frac=1, random_state=42).reset_index(drop=True)
    test_subset_df = pd.concat(test_subset).sample(frac=1, random_state=42).reset_index(drop=True)
    
    print(f"Final real training subset: {len(train_subset_df)} samples")
    print(f"Final real test subset: {len(test_subset_df)} samples")
    
    return train_subset_df, test_subset_df

def create_js_file(train_df, test_df, output_file):
    """Create JavaScript file with real MNIST data"""
    
    print(f"Creating JavaScript file: {output_file}")
    
    with open(output_file, 'w') as f:
        f.write("// REAL MNIST Dataset Subset - Actual handwritten digits\n")
        f.write("// Source: http://yann.lecun.com/exdb/mnist/\n") 
        f.write("// NO SYNTHETIC DATA - These are real handwritten digits from the MNIST database\n")
        f.write(f"// {len(train_df)} training + {len(test_df)} test samples\n\n")
        
        f.write("window.REAL_MNIST_DATA = {\n")
        f.write("    metadata: {\n")
        f.write('        description: "Real MNIST handwritten digits - NO synthetic data",\n')
        f.write('        source: "http://yann.lecun.com/exdb/mnist/",\n')
        f.write(f'        total_samples: {len(train_df) + len(test_df)},\n')
        f.write(f'        train_samples: {len(train_df)},\n')
        f.write(f'        test_samples: {len(test_df)},\n')
        f.write('        note: "Real handwritten digits from MNIST database"\n')
        f.write("    },\n")
        
        # Training data
        f.write("    train: {\n")
        f.write("        images: [\n")
        
        for i, (_, row) in enumerate(train_df.iterrows()):
            if i > 0:
                f.write(",\n")
            
            # Extract pixels and normalize to 0-1
            pixels = [float(x) / 255.0 for x in row.iloc[1:].values]
            f.write("            [" + ",".join(f"{x:.3f}" for x in pixels) + "]")
            
            if i % 100 == 0:
                print(f"Written {i+1}/{len(train_df)} real training samples...")
        
        f.write("\n        ],\n")
        
        # Training labels
        train_labels = train_df.iloc[:, 0].tolist()
        f.write("        labels: [" + ",".join(map(str, train_labels)) + "]\n")
        f.write("    },\n")
        
        # Test data
        f.write("    test: {\n")
        f.write("        images: [\n")
        
        for i, (_, row) in enumerate(test_df.iterrows()):
            if i > 0:
                f.write(",\n")
            
            # Extract pixels and normalize to 0-1
            pixels = [float(x) / 255.0 for x in row.iloc[1:].values]
            f.write("            [" + ",".join(f"{x:.3f}" for x in pixels) + "]")
            
            if i % 50 == 0:
                print(f"Written {i+1}/{len(test_df)} real test samples...")
        
        f.write("\n        ],\n")
        
        # Test labels
        test_labels = test_df.iloc[:, 0].tolist()
        f.write("        labels: [" + ",".join(map(str, test_labels)) + "]\n")
        f.write("    }\n")
        f.write("};\n")
        
        f.write("\nconsole.log('Real MNIST data loaded:', window.REAL_MNIST_DATA.metadata);\n")

def main():
    print("Processing REAL MNIST data (NOT synthetic)...")
    print("=" * 50)
    
    # Process the real MNIST CSV files
    train_df, test_df = process_real_mnist()
    
    # Create JavaScript file
    output_file = "real_mnist_data_actual.js"
    create_js_file(train_df, test_df, output_file)
    
    # Check file size
    file_size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"\nReal MNIST dataset created successfully!")
    print(f"Output file: {output_file}")
    print(f"File size: {file_size_mb:.1f} MB")
    print(f"Training samples: {len(train_df)} (real handwritten digits)")
    print(f"Test samples: {len(test_df)} (real handwritten digits)")
    
    if file_size_mb > 90:
        print("⚠️  Warning: File may be close to GitHub's 100MB limit")
    else:
        print("✅ File size is safe for GitHub Pages")
    
    print("\n✅ SUCCESS: Created JavaScript file with REAL MNIST data")
    print("🚫 NO synthetic data was used - all samples are real handwritten digits")

if __name__ == "__main__":
    main()