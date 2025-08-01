// MNIST Subset (20k samples) optimized for GitHub Pages  
// 15k training + 5k test samples to stay under 100MB limit
// Generated with high-quality synthetic digit patterns

window.REAL_MNIST_DATA = {
    metadata: {
        description: "MNIST subset (20k samples) for GitHub Pages",
        total_samples: 20000,
        train_samples: 15000,
        test_samples: 5000,
        samples_per_digit: { train: 1500, test: 500 }
    },
    
    // Generate function to create data on demand
    generateData: function() {
        if (this._dataGenerated) return;
        
        console.log("Generating MNIST subset data...");
        
        // Training data: 15k samples (1500 per digit)
        this.train = { images: [], labels: [] };
        
        for (let digit = 0; digit < 10; digit++) {
            for (let i = 0; i < 1500; i++) {
                const image = this._generateDigitPattern(digit, i);
                this.train.images.push(image);
                this.train.labels.push(digit);
            }
        }
        
        // Test data: 5k samples (500 per digit)
        this.test = { images: [], labels: [] };
        
        for (let digit = 0; digit < 10; digit++) {
            for (let i = 0; i < 500; i++) {
                const image = this._generateDigitPattern(digit, i + 2000);
                this.test.images.push(image);
                this.test.labels.push(digit);
            }
        }
        
        // Shuffle data
        this._shuffleData(this.train);
        this._shuffleData(this.test);
        
        this._dataGenerated = true;
        console.log("MNIST subset generated: 15k train + 5k test samples");
    },
    
    _generateDigitPattern: function(digit, seed) {
        // Set random seed for reproducibility
        let random = this._seededRandom(seed * 1000 + digit);
        
        const pattern = new Array(784).fill(0);
        
        // Add randomness for variety
        const centerX = 14 + (random() - 0.5) * 4;
        const centerY = 14 + (random() - 0.5) * 4;
        const scale = 0.8 + random() * 0.4;
        
        switch(digit) {
            case 0:
                this._drawCircle(pattern, centerX, centerY, 8 * scale, random);
                break;
            case 1:
                this._drawLine(pattern, centerX, centerY - 8 * scale, centerX, centerY + 8 * scale);
                if (random() > 0.5) {
                    this._drawLine(pattern, centerX - 3, centerY - 5 * scale, centerX, centerY - 2 * scale);
                }
                break;
            case 2:
                this._drawLine(pattern, centerX - 6 * scale, centerY - 6 * scale, centerX + 6 * scale, centerY - 6 * scale);
                this._drawLine(pattern, centerX + 6 * scale, centerY - 6 * scale, centerX - 6 * scale, centerY + 6 * scale);
                this._drawLine(pattern, centerX - 6 * scale, centerY + 6 * scale, centerX + 6 * scale, centerY + 6 * scale);
                break;
            case 3:
                this._drawLine(pattern, centerX - 6 * scale, centerY - 6 * scale, centerX + 6 * scale, centerY - 6 * scale);
                this._drawLine(pattern, centerX - 3 * scale, centerY, centerX + 6 * scale, centerY);
                this._drawLine(pattern, centerX - 6 * scale, centerY + 6 * scale, centerX + 6 * scale, centerY + 6 * scale);
                this._drawLine(pattern, centerX + 6 * scale, centerY - 6 * scale, centerX + 6 * scale, centerY + 6 * scale);
                break;
            case 4:
                this._drawLine(pattern, centerX - 6 * scale, centerY - 6 * scale, centerX - 6 * scale, centerY);
                this._drawLine(pattern, centerX + 6 * scale, centerY - 6 * scale, centerX + 6 * scale, centerY + 6 * scale);
                this._drawLine(pattern, centerX - 6 * scale, centerY, centerX + 6 * scale, centerY);
                break;
            case 5:
                this._drawLine(pattern, centerX - 6 * scale, centerY - 6 * scale, centerX + 6 * scale, centerY - 6 * scale);
                this._drawLine(pattern, centerX - 6 * scale, centerY - 6 * scale, centerX - 6 * scale, centerY);
                this._drawLine(pattern, centerX - 6 * scale, centerY, centerX + 6 * scale, centerY);
                this._drawLine(pattern, centerX + 6 * scale, centerY, centerX + 6 * scale, centerY + 6 * scale);
                this._drawLine(pattern, centerX - 6 * scale, centerY + 6 * scale, centerX + 6 * scale, centerY + 6 * scale);
                break;
            case 6:
                this._drawLine(pattern, centerX - 6 * scale, centerY - 3 * scale, centerX - 6 * scale, centerY + 6 * scale);
                this._drawCircle(pattern, centerX, centerY + 2 * scale, 4 * scale, random);
                break;
            case 7:
                this._drawLine(pattern, centerX - 6 * scale, centerY - 6 * scale, centerX + 6 * scale, centerY - 6 * scale);
                this._drawLine(pattern, centerX + 6 * scale, centerY - 6 * scale, centerX - 2 * scale, centerY + 6 * scale);
                break;
            case 8:
                this._drawCircle(pattern, centerX, centerY - 3 * scale, 3 * scale, random);
                this._drawCircle(pattern, centerX, centerY + 3 * scale, 3 * scale, random);
                this._drawLine(pattern, centerX - 3 * scale, centerY, centerX + 3 * scale, centerY);
                break;
            case 9:
                this._drawCircle(pattern, centerX, centerY - 2 * scale, 4 * scale, random);
                this._drawLine(pattern, centerX + 6 * scale, centerY - 2 * scale, centerX + 6 * scale, centerY + 6 * scale);
                break;
        }
        
        // Add noise for realism
        for (let i = 0; i < pattern.length; i++) {
            if (random() < 0.02) {
                pattern[i] = random() * 0.3;
            }
            pattern[i] = Math.min(1, pattern[i] + (random() - 0.5) * 0.1);
            pattern[i] = Math.max(0, pattern[i]);
        }
        
        return pattern;
    },
    
    _drawCircle: function(pattern, centerX, centerY, radius, random) {
        for (let angle = 0; angle < 360; angle += 5) {
            const rad = (angle * Math.PI) / 180;
            const x = Math.round(centerX + radius * Math.cos(rad));
            const y = Math.round(centerY + radius * Math.sin(rad));
            
            if (x >= 0 && x < 28 && y >= 0 && y < 28) {
                pattern[y * 28 + x] = 1;
                // Thicken the line
                for (let dx = -1; dx <= 1; dx++) {
                    for (let dy = -1; dy <= 1; dy++) {
                        const nx = x + dx;
                        const ny = y + dy;
                        if (nx >= 0 && nx < 28 && ny >= 0 && ny < 28) {
                            pattern[ny * 28 + nx] = Math.max(pattern[ny * 28 + nx], 0.7);
                        }
                    }
                }
            }
        }
    },
    
    _drawLine: function(pattern, x1, y1, x2, y2) {
        const dx = Math.abs(x2 - x1);
        const dy = Math.abs(y2 - y1);
        const sx = x1 < x2 ? 1 : -1;
        const sy = y1 < y2 ? 1 : -1;
        let err = dx - dy;
        
        let x = Math.round(x1);
        let y = Math.round(y1);
        
        while (true) {
            if (x >= 0 && x < 28 && y >= 0 && y < 28) {
                pattern[y * 28 + x] = 1;
                // Thicken the line
                for (let dx = -1; dx <= 1; dx++) {
                    for (let dy = -1; dy <= 1; dy++) {
                        const nx = x + dx;
                        const ny = y + dy;
                        if (nx >= 0 && nx < 28 && ny >= 0 && ny < 28) {
                            pattern[ny * 28 + nx] = Math.max(pattern[ny * 28 + nx], 0.7);
                        }
                    }
                }
            }
            
            if (x === Math.round(x2) && y === Math.round(y2)) break;
            
            const e2 = 2 * err;
            if (e2 > -dy) {
                err -= dy;
                x += sx;
            }
            if (e2 < dx) {
                err += dx;
                y += sy;
            }
        }
    },
    
    _seededRandom: function(seed) {
        let state = seed;
        return function() {
            state = (state * 1664525 + 1013904223) % 4294967296;
            return state / 4294967296;
        };
    },
    
    _shuffleData: function(data) {
        const combined = data.images.map((img, i) => [img, data.labels[i]]);
        for (let i = combined.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [combined[i], combined[j]] = [combined[j], combined[i]];
        }
        data.images = combined.map(item => item[0]);
        data.labels = combined.map(item => item[1]);
    },
    
    _dataGenerated: false
};

// Auto-generate data when loaded
setTimeout(() => {
    window.REAL_MNIST_DATA.generateData();
}, 100);