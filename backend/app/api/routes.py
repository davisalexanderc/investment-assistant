from fastapi import APIRouter

from app.data.mock_data import SAMPLE_SECURITIES
from app.schemas.domain import MetricRequest, MetricResult, Security
from app.services.metrics import compute_metric_bundle

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/securities", response_model=list[Security])
def list_securities() -> list[Security]:
    return SAMPLE_SECURITIES


@router.post("/metrics", response_model=MetricResult)
def metrics(payload: MetricRequest) -> MetricResult:
    return compute_metric_bundle(payload)
