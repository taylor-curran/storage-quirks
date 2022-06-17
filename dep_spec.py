from prefect.deployments import DeploymentSpec
from prefect.blocks.storage import TempStorageBlock
from prefect.flow_runners import SubprocessFlowRunner

DeploymentSpec(
    flow_location="flow.py",
    name="storage-quirks-0",
    flow_storage=TempStorageBlock(),
    flow_runner=SubprocessFlowRunner()
)


