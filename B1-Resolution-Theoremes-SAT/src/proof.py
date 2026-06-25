from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
import subprocess

from .domain import SatInstance
from .solver_sat import SolveResult, solve_cnf


@dataclass(frozen=True)
class ProofCheckResult:
    status: str
    proof_path: Path | None = None
    checker_output: str | None = None
    message: str | None = None


def export_pysat_proof(
    instance: SatInstance,
    out_dir: Path,
    solver_name: str = "glucose4",
    time_limit_s: float = 10.0,
    attempt_pysat_proof: bool = False,
) -> tuple[SolveResult, ProofCheckResult]:
    out_dir.mkdir(parents=True, exist_ok=True)
    cnf_path = out_dir / f"{instance.name}.cnf"
    proof_path = out_dir / f"{instance.name}.{solver_name}.drat"
    instance.cnf.save_dimacs(cnf_path)

    result = solve_cnf(instance.cnf, solver_name=solver_name, time_limit_s=time_limit_s)
    if result.status != "UNSATISFIABLE":
        return result, ProofCheckResult(
            status="NO_PROOF",
            message=f"solver status is {result.status}, expected UNSATISFIABLE",
        )
    if not attempt_pysat_proof:
        return result, ProofCheckResult(
            status="NO_PROOF",
            message=(
                "CNF exported; in-process PySAT proof extraction is disabled by default "
                "because some Windows solver builds return a failing process status in proof mode"
            ),
        )

    result = solve_cnf(
        instance.cnf,
        solver_name=solver_name,
        time_limit_s=time_limit_s,
        with_proof=True,
    )
    if not result.proof_lines:
        return result, ProofCheckResult(
            status="NO_PROOF",
            message="solver did not expose a proof trace through PySAT",
        )

    proof_path.write_text("\n".join(result.proof_lines) + "\n", encoding="utf-8")
    return result, ProofCheckResult(status="EXPORTED", proof_path=proof_path)


def verify_with_drat_trim(
    cnf_path: Path,
    proof_path: Path,
    drat_trim_bin: str = "drat-trim",
    timeout_s: float = 30.0,
) -> ProofCheckResult:
    executable = shutil.which(drat_trim_bin)
    if executable is None:
        return ProofCheckResult(
            status="UNAVAILABLE",
            proof_path=proof_path,
            message=f"{drat_trim_bin} was not found in PATH",
        )

    completed = subprocess.run(
        [executable, str(cnf_path), str(proof_path)],
        capture_output=True,
        text=True,
        timeout=timeout_s,
        check=False,
    )
    output = (completed.stdout + "\n" + completed.stderr).strip()
    status = "VALID" if completed.returncode == 0 else "INVALID"
    return ProofCheckResult(status=status, proof_path=proof_path, checker_output=output)
