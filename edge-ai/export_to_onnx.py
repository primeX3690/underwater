# edge-ai/export_to_onnx.py
import torch
import torch.onnx
from train_model import EdgeSonarClassifier

def export_model():
    print("[Export] Loading trained PyTorch Edge Sonar model...")
    model = EdgeSonarClassifier()
    model.eval()

    dummy_input = torch.randn(1, 3, dtype=torch.float32)
    onnx_path = "edge_sonar_model.onnx"

    torch.onnx.export(
        model,
        dummy_input,
        onnx_path,
        export_params=True,
        opset_version=11,
        input_names=['acoustic_features'],
        output_names=['threat_probability']
    )
    print(f"[Export] Success! Model successfully converted and saved to {onnx_path}")

if __name__ == "__main__":
    export_model()