"""Pass a small batch of sequences through PyTorch RNN, LSTM, and GRU layers."""

import torch
from torch import nn


def main() -> None:
    torch.manual_seed(42)
    batch = torch.randn(2, 4, 5)

    recurrent_layers = {
        "RNN": nn.RNN(input_size=5, hidden_size=8, batch_first=True),
        "LSTM": nn.LSTM(input_size=5, hidden_size=8, batch_first=True),
        "GRU": nn.GRU(input_size=5, hidden_size=8, batch_first=True),
    }

    print("Input shape:", tuple(batch.shape))
    for name, layer in recurrent_layers.items():
        output, state = layer(batch)
        if name == "LSTM":
            hidden_state = state[0]
        else:
            hidden_state = state
        print(
            f"{name}: output shape={tuple(output.shape)}, "
            f"hidden shape={tuple(hidden_state.shape)}"
        )


if __name__ == "__main__":
    main()
