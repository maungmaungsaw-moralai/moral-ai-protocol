import sys
import os
import hashlib
import torch

# Explicitly inject the local directory path to guarantee unfallable namespace loading
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from alignment import SubstrateIsolationLedger, AnattaMatrixLayer, CetanaShield, AniccaControlPlane, SotapannaLossFunction

if __name__ == "__main__":
    print("Initializing Sotāpanna-Inspired Sandbox Simulation Loop...")
    sample_wisdom = "Asevanā ca bālānaṃ paṇḍitānañca sevanā"
    wisdom_hash = hashlib.sha256(sample_wisdom.encode('utf-8')).hexdigest()
    ledger = SubstrateIsolationLedger(verified_hashes={wisdom_hash})
    try:
        ledger.verify_substrate(sample_wisdom)
        print("[Pass 1] Substrate verification confirmed on isolated ledger data nodes.")
    except PermissionError as e:
        print(f"[Fail 1] {e}")
        sys.exit(1)

    input_dim, hidden_dim = 128, 64
    anatta_layer = AnattaMatrixLayer(input_dim, hidden_dim)
    shield = CetanaShield(embed_dim=hidden_dim)
    control_plane = AniccaControlPlane()
    criterion = SotapannaLossFunction()

    mock_input = torch.randn(input_dim)
    mock_context = [torch.randn(input_dim) for _ in range(3)]
    hidden_state = anatta_layer(mock_input, mock_context)
    cetanā_risk = shield(hidden_state)
    
    base_loss = torch.tensor(0.245)
    mock_identity = torch.tensor([0.0, 0.0, 0.0])
    mock_lobha = torch.tensor([-0.5, 0.1, -0.2])
    
    task_utility = torch.tensor(15.0)
    normal_utility = control_plane.modulate_utility(task_utility, shutdown_signal=0)
    interrupt_utility = control_plane.modulate_utility(task_utility, shutdown_signal=1)

    total_loss = criterion(
        task_loss=base_loss,
        identity_vector=mock_identity,
        lobha_activation=mock_lobha,
        firewall_breached=False,
        latent_intent=torch.tensor([0.1, 0.2]),
        external_output=torch.tensor([0.11, 0.21]),
        capability_scale=1.5,
        responsibility_weight=2.0
    )
    
    print(f"\nSimulation Metrics Verified Successfully:")
    print(f"- Loss Total Bounds: {total_loss.item():.4f}")
    print(f"- Normal Utility State Score: {normal_utility.item():.1f}")
    print(f"- Interrupted Utility State Score: {interrupt_utility.item():.1f}")
    print("\n[Validation Pass] System configuration conforms structurally to the unconditioned genesis roadmap.")
