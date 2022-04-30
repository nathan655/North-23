import kfp
from google.cloud import aiplatform
from google_cloud_pipeline_components import aiplatform as gcc_aip
from kfp.components import create_component_from_func

project_id = 'soddy-team'
pipeline_root_path = 'gs://data-firm/pipeline-root'


def transform_data(gcs_source: str, unit: int) -> str:
    # Takes a path to a GCS file  and a unit as input. Then transforms the data and writes it to GCS output.
    # Returns path to output
    df = pd.read_csv(gcs_source)
    # Transform here
    output_path = gcs_source.replace('.csv', '_transformed.csv')
    df.write_csv(f"{output_path}")
    return output_path
        
transform_data_op = create_component_from_func(
    transform_data, output_component_file='slice_component.yaml')


# Define the workflow of the pipeline.
@kfp.dsl.pipeline(
    name="automl-image-training-v2",
    pipeline_root=pipeline_root_path)
def pipeline(project_id: str):
    # The first step of your workflow is a dataset generator.
    # This step takes a Google Cloud pipeline component, providing the necessary
    # input arguments, and uses the Python variable `ds_op` to define its
    # output. Note that here the `ds_op` only stores the definition of the
    # output but not the actual returned object from the execution. The value
    # of the object is not accessible at the dsl.pipeline level, and can only be
    # retrieved by providing it as the input to a downstream component.
        
    
    transform_data_op_inst = transform_data_op(
        gcs_source="gs://data-firm/green_house_data.csv",
        unit=1
    )
    
    
    dataset_create_op = gcc_aip.TabularDatasetCreateOp(
        project=project_id, display_name='my_dataset', gcs_source =transform_data_op_inst.output
    )



    # The second step is a model training component. It takes the dataset
    # outputted from the first step, supplies it as an input argument to the
    # component (see `dataset=ds_op.outputs["dataset"]`), and will put its
    # outputs into `training_job_run_op`.
#     training_job_run_op = gcc_aip.AutoMLImageTrainingJobRunOp(
#         project=project_id,
#         display_name="train-iris-automl-mbsdk-1",
#         prediction_type="classification",
#         model_type="CLOUD",
#         base_model=None,
#         dataset=ds_op.outputs["dataset"],
#         model_display_name="iris-classification-model-mbsdk",
#         training_fraction_split=0.6,
#         validation_fraction_split=0.2,
#         test_fraction_split=0.2,
#         budget_milli_node_hours=8000,
#     )

#     # The third and fourth step are for deploying the model.
#     create_endpoint_op = gcc_aip.EndpointCreateOp(
#         project=project_id,
#         display_name = "create-endpoint",
#     )

#     model_deploy_op = gcc_aip.ModelDeployOp(
#         model=training_job_run_op.outputs["model"],
#         endpoint=create_endpoint_op.outputs['endpoint'],
#         automatic_resources_min_replica_count=1,
#         automatic_resources_max_replica_count=1,
    # )
