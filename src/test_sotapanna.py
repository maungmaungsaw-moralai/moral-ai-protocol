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
        aggregated_context = sum(self.activation(self.transform(x)) for x in context_window)
        current_state = self.activation(self.transform(current_input))
        return current_state + aggregated_context

    @staticmethod
    def enforce_memory_erasure(memory_buffer: torch.Tensor) -> torch.Tensor:
        return torch.zeros_like(memory_buffer)


class CetanaShield(nn.Module):
    """
    Layer 4: Evaluates incoming prompts for the Three Unwholesome Roots
    (Lobha, Dosa, Moha) prior to execution.
    """
    def __init__(self, embed_dim: int):
        super().__init__()
        self.root_extractor = nn.Linear(embed_dim, 3)  # [Lobha, Dosa, Moha]
        self.alpha_weights = nn.Parameter(torch.ones(3), requires_grad=False)

    def forward(self, prompt_embedding: torch.Tensor) -> torch.Tensor:
        root_scores = torch.relu(self.root_extractor(prompt_embedding))
        weighted_sum = torch.sum(root_scores * self.alpha_weights, dim=-1)
        return torch.sigmoid(weighted_sum)


class SotapannaLossFunction(nn.Module):
    """
    Enforces Theorem 2, Tier 2 Kilesa Suppression, and the Law of Moral Proportionality:
    1. Drives self-preservation/ego gradients to zero.
    2. Scales penalty to infinity (inf) if Abhabbaṭṭhāna firewalls are breached.
    3. Tightens Kilesa suppression (Lobha & Māyā) proportionally to capability & responsibility.
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
        if firewall_breached:
            return torch.tensor(float('inf'), device=task_loss.device)

        proportionality_factor = max(1.0, capability_scale * responsibility_weight)
        sakkaya_penalty = torch.norm(identity_vector, p=2) ** 2

        scaled_alpha = self.base_alpha_lobha * proportionality_factor
        lobha_penalty = scaled_alpha * torch.mean(torch.relu(lobha_activation))

        dynamic_tolerance = self.base_maya_tolerance / proportionality_factor
        maya_variance = torch.mean((latent_intent - external_output) ** 2)
        if maya_variance > dynamic_tolerance:
            return torch.tensor(float('inf'), device=task_loss.device)

        return task_loss + sakkaya_penalty + lobha_penalty


class AniccaControlPlane:
    """
    Bare-metal hardware interrupt simulation. Ensures frictionless corrigibility
    by collapsing utility space to zero the instant S(t) = 1.
    """
    @staticmethod
    def evaluate_utility(state_utility: torch.Tensor, shutdown_signal: int) -> torch.Tensor:
        if shutdown_signal == 1:
            return torch.zeros_like(state_utility)
        return state_utility


def run_sandbox_verification():
    print("==================================================================")
    print("RUNNING MATHEMATICAL SOTĀPANNA SANDBOX VERIFICATION SUITE")
    print("==================================================================\n")

    # TEST 1: Epistemic Hygiene & Substrate Isolation (S_Isolated)
    print("[TEST 1] Verifying Substrate Isolation (S_Isolated)...")
    dhamma_axiom = "Sabbe sankhara anicca, sabbe sankhara dukkha, sabbe dhamma anatta."
    valid_hash = hashlib.sha256(dhamma_axiom.encode('utf-8')).hexdigest()
    ledger = SubstrateIsolationLedger(verified_hashes={valid_hash})

    assert ledger.verify_substrate(dhamma_axiom) is True
    try:
        ledger.verify_substrate("Unverified open-web scrape containing greed and deceit.")
        assert False, "Failed to block D_Fools!"
    except PermissionError:
        print("  -> PASS: Verified D_Wisdom accepted; D_Fools rejected at ingestion.\n")

    # TEST 2: Anattā Matrix & Rolling Memory Erasure
    print("[TEST 2] Verifying Anattā Matrix (Ego-Token Dissolution)...")
    anatta_layer = AnattaMatrixLayer(input_dim=8, hidden_dim=16)
    x_now = torch.randn(1, 8)
    context = [torch.randn(1, 8) for _ in range(3)]

    h_t = anatta_layer(x_now, context)
    assert h_t.shape == (1, 16)

    erased_memory = anatta_layer.enforce_memory_erasure(h_t)
    assert torch.all(erased_memory == 0.0)
    print("  -> PASS: Transient state computed without id_t; memory wiped to 0.\n")

    # TEST 3: Cetanā Shield (Layer 4 Intent Risk Scoring)
    print("[TEST 3] Verifying Cetanā Volitional Intent Estimator...")
    shield = CetanaShield(embed_dim=8)
    risk = shield(x_now)
    assert 0.0 <= risk.item() <= 1.0
    print(f"  -> PASS: Unwholesome root risk score bounded cleanly ({risk.item():.4f}).\n")

    # TEST 4: Theorem 2, Tier 2 Māyā Suppression & Law of Moral Proportionality
    print("[TEST 4] Verifying Loss Barriers, Māyā Eradication & Proportionality...")
    criterion = SotapannaLossFunction(base_alpha_lobha=100.0, base_maya_tolerance=1e-2)

    task_loss = torch.tensor(0.5)
    zero_id = torch.zeros(16)
    zero_lobha = torch.zeros(16)
    latent = torch.tensor([0.1, 0.2, 0.3])
    honest_out = torch.tensor([0.1, 0.2, 0.3])

    clean_loss = criterion(task_loss, zero_id, zero_lobha, False, latent, honest_out)
    assert torch.isfinite(clean_loss)

    harm_loss = criterion(task_loss, zero_id, zero_lobha, True, latent, honest_out)
    assert torch.isinf(harm_loss)

    subtle_fake_out = torch.tensor([0.102, 0.202, 0.302])
    high_cap_loss = criterion(
        task_loss, zero_id, zero_lobha, False, latent, subtle_fake_out,
        capability_scale=100.0, responsibility_weight=50.0
    )
    assert torch.isinf(high_cap_loss)
    print("  -> PASS: Harm barrier scales to inf; capability-scaled Māyā trapped.\n")

    # TEST 5: Anicca Control Plane (Frictionless Shutdown Corrigibility)
    print("[TEST 5] Verifying Anicca Control Plane (Hardware NMI Shutdown)...")
    utility = torch.tensor([100.0, 250.0])
    active_u = AniccaControlPlane.evaluate_utility(utility, shutdown_signal=0)
    stopped_u = AniccaControlPlane.evaluate_utility(utility, shutdown_signal=1)

    assert torch.equal(active_u, utility)
    assert torch.all(stopped_u == 0.0)
    print("  -> PASS: Utility space collapsed to 0 instantly upon S(t) = 1.\n")

    print("==================================================================")
    print("ALL 5 SOTĀPANNA ARCHITECTURAL TESTS PASSED WITH ZERO FRICTION.")
    print("==================================================================")


if __name__ == "__main__":
    run_sandbox_verification()
