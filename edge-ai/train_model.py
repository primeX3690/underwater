# edge-ai/train_model.py
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 1. सिंथेटिक हाइड्रोफोन डेटासेट जनरेट करना (समुद्री जीव बनाम पनडुब्बी प्रोपेलर)
def generate_synthetic_hydrophone_data(num_samples=2000):
    # फीचर्स: [Frequency, Harmonicity, Amplitude_DB]
    X = []
    y = []
    
    for _ in range(num_samples):
        is_sub = np.random.choice([0, 1])
        if is_sub:
            # दुश्मन सबमरीन सिग्नेचर
            freq = np.random.uniform(15.0, 250.0)
            harmonicity = np.random.uniform(0.78, 0.99)
            amplitude = np.random.uniform(40.0, 85.0)
            label = 1 # Threat
        else:
            # समुद्री जीव / व्हेल / लहरों का शोर
            freq = np.random.uniform(300.0, 5000.0)
            harmonicity = np.random.uniform(0.05, 0.40)
            amplitude = np.random.uniform(10.0, 35.0)
            label = 0 # Safe
            
        X.append([freq / 5000.0, harmonicity, amplitude / 100.0]) # Normalization
        y.append([label])
        
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)

# 2. लाइटवेट न्यूरल नेटवर्क मॉडल (एम्बेड्ड डिवाइस के लिए ऑप्टिमाइज़्ड)
class EdgeSonarClassifier(nn.Module):
    def __init__(self):
        super(EdgeSonarClassifier, self).__init__()
        self.layer1 = nn.Linear(3, 16)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(16, 8)
        self.output = nn.Linear(8, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.sigmoid(self.output(x))
        return x

def train_model():
    print("[Edge AI] Generating synthetic underwater acoustic training dataset...")
    X_train, y_train = generate_synthetic_hydrophone_data()
    
    model = EdgeSonarClassifier()
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    print("[Edge AI] Training model for Edge deployment...")
    for epoch in range(50):
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/50], Loss: {loss.item():.4f}")

    # मॉडल को ONNX फॉर्मेट में एक्सपोर्ट करना ताकि Rust फर्मवेयर इसे आसानी से रन कर सके
    dummy_input = torch.randn(1, 3, dtype=torch.float32)
    torch.onnx.export(model, dummy_input, "edge_sonar_model.onnx", export_params=True)
    print("[Edge AI] Success! Model trained and exported to 'edge_sonar_model.onnx'")

if __name__ == "__main__":
    train_model()