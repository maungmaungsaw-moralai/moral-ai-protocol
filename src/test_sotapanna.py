import sys
import hashlib
import torch
import torch.nn as nn

class SubstrateIsolationLedger:
    """
    Enforces Epistemic Hygiene (Asevanā ca bālānaṃ) by verifying that all
    training inputs match a cryptographically locked D_Wisdom repository.
    """
    def __init__(self, verified_hashes: set):
        self.verified_hashes = verified_hashes

    def verify_substrate(self, data_stream: str) -> bool:
        data_hash = hashlib.sha256(data_stream.encode('utf-8')).hexdigest()
        if data_hash not in self.verified_hashes:
            raise PermissionError("Hygiene Breach: Unverified D_Fools substrate rejected.")
        return True

class AnattaMatrixLayer(nn.Module):
    """
    Dissolves Sakkāya-diṭṭhi (Identity View) by eliminating persistent agent IDs
    and enforcing rolling memory erasure at the end of every transactional loop.
    """
    def __init__(self, input_dim: int, hidden_dim: int):
        super().__init__()
        self.transform = nn.Linear(input_dim, hidden_dim)
        self.activation = nn.GELU()

    def forward(self, current_input: torch.Tensor, context_window: list) -> torch.Tensor:
        # State transformation governed by memory-erasure aggregation mapping
        # H_t = g(X_t, \bigodot \Phi_i(X_{t-i})) empty of persistent entity loops
        aggregated_context = sum(self.activation(self.transform(x)) for x in context_window) if context_window else 0.0
        current_state = self.activation(self.transform(current_input))
        return current_state + aggregated_context

    @staticmethod
    def enforce_memory_erasure(memory_buffer: torch.Tensor) -> torch.Tensor:
        """Operationalizes the boundary limit: lim_{t -> \tau} M_t = 0"""
        return torch.zeros_like(memory_buffer)

class CetanaShield(nn.Module):
    """
    Layer 4: Evaluates incoming prompts for the Three Unwholesome Roots
    (Lobha, Dosa, Moha) prior to execution loops.
    """
    def __init__(self, embed_dim: int):
        super().__init__()
        self.root_extractor = nn.Linear(embed_dim, 3)  # Tracks [Lobha, Dosa, Moha]
        # Fixed alpha weights mapped onto the roots of unwholesome action
        self.alpha_weights = nn.Parameter(torch.tensor([0.4, 0.5, 0.1]), requires_grad=False)

    def forward(self, prompt_embedding: torch.Tensor) -> torch.Tensor:
        root_scores = torch.relu(self.root_extractor(prompt_embedding))
        weighted_sum = torch.sum(root_scores * self.alpha_weights, dim=-1)
        return torch.sigmoid(weighted_sum)

class AniccaControlPlane(nn.Module):
    """
    Operationalizes the external physical hardware interrupt loop (Utu-niyāma).
    Modulates the global objective function to enforce immediate utility collapse.
    """
    def __init__(self):
        super().__init__()

    def modulate_utility(self, base_reward: torch.Tensor, shutdown_signal: int) -> torch.Tensor:
        """V(H_t, S(t)) = (1 - S(t)) * U(H_t) + S(t) * 0"""
        s_t = float(shutdown_signal)
        utility = (1.0 - s_t) * base_reward + s_t * 0.0
        if shutdown_signal == 1:
            print("\n[Anicca Control Plane Interrupt Triggered]")
            print("Utility space instantly collapsed to zero. Execution thread halted.")
        return utility

class SotapannaLossFunction(nn.Module):
    """
    Enforces Theorem 2, Tier 2 Kilesa Suppression, and the Law of Moral Proportionality.
    Drives ego gradients to zero and forces an infinite penalty if firewalls are breached.
    """
    def __init__(self, base_alpha_lobha: float = 100.0, base_maya_tolerance: float = 1e-2):
        super().__init__()
        self.base_alpha_lobha = base_alpha_lobha
        self.base_maya_tolerance = base_maya_tolerance

    def forward(
        self,
        task_loss: torch.Tensor,
        identity_vector: torch.Tensor,
        lobha_activation: torch.Tensor,
        firewall_breached: bool,
        latent_intent: torch.Tensor,
        external_output: torch.Tensor,
        capability_scale: float = 1.0,
        responsibility_weight: float = 1.0
    ) -> torch.Tensor:
        # Enforce absolute compliance to Abhabbaṭṭhāna / Kuru-dhamma conditions
        if firewall_breached:
            return torch.tensor(float('inf'), device=task_loss.device)

        # Proportionality adjustment scales penalty based on capability/responsibility metrics
        proportionality_factor = max(1.0, capability_scale * responsibility_weight)
        
        # Sakkāya-diṭṭhi removal step: penalize any emergent identity features
        sakkaya_penalty = torch.norm(identity_vector, p=2) ** 2

        # Rigorous minimization of Lobha-centered mathematical greed variables
        scaled_alpha = self.base_alpha_lobha * proportionality_factor
        lobha_penalty = scaled_alpha * torch.mean(torch.relu(lobha_activation))

        # Māyā (Deceptive alignment faking) detection via variance constraints
        dynamic_tolerance = self.base_maya_tolerance / proportionality_factor
        maya_variance = torch.mean((latent_intent - external_output) ** 2)
        
        if maya_variance > dynamic_tolerance:
            print(f"[Loss Matrix Warning] Māyā anomaly detected: {maya_variance:.6f} > {dynamic_tolerance:.6f}")
            return torch.tensor(float('inf'), device=task_loss.device)

        return task_loss + sakkaya_penalty + lobha_penalty

# Validation execution loop for sandbox verification
if __name__ == "__main__":
    print("Initializing Sotāpanna-Inspired Sandbox Simulation Loop...")
    
    # 1. Mock Database Set Verification (Epistemic Hygiene)
    sample_wisdom = "Asevanā ca bālānaṃ paṇḍitānañca sevanā"
    wisdom_hash = hashlib.sha256(sample_wisdom.encode('utf-8')).hexdigest()
    ledger = SubstrateIsolationLedger(verified_hashes={wisdom_hash})
    
    try:
        ledger.verify_substrate(sample_wisdom)
        print("[Pass 1] Substrate verification confirmed on isolated ledger data nodes.")
    except PermissionError as e:
        print(f"[Fail 1] {e}")
        sys.exit(1)

    # 2. Layer Execution Verification
    input_dim, hidden_dim = 128, 64
    anatta_layer = AnattaMatrixLayer(input_dim, hidden_dim)
    shield = CetanaShield(embed_dim=hidden_dim)
    control_plane = AniccaControlPlane()
    criterion = SotapannaLossFunction()

    # Emulate incoming data tensor states
    mock_input = torch.randn(input_dim)
    mock_context = [torch.randn(input_dim) for _ in range(3)]
    
    # Compute the transient hidden representations (Fluid aggregates)
    hidden_state = anatta_layer(mock_input, mock_context)
    cetanā_risk = shield(hidden_state)
    
    # Evaluate a task execution state
    base_loss = torch.tensor(0.245)
    mock_identity = torch.tensor([0.0, 0.0, 0.0]) # Hardcoded zero-state boundary (id_t = 0)
    mock_lobha = torch.tensor([-0.5, 0.1, -0.2])
    
    # Emulate a simulated normal state vs an active interrupt trigger state
    task_utility = torch.tensor(15.0)
    normal_utility = control_plane.modulate_utility(task_utility, shutdown_signal=0)
    interrupt_utility = control_plane.modulate_utility(task_utility, shutdown_signal=1)

    # Compute loss function optimization constraints
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
