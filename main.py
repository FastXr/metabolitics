from utils import *
from preprocessing import *
from extensions import *
from analysis import *
from sklearn_utils.preprocessing import FeatureRenaming

DATASET_PATH = '/home/enis/DrugAnalysis/metabolitics/datasets/naming/toy-mapping.json'
with open(DATASET_PATH) as f:
    data = json.load(f)


def pipeline_builder(drug_name=''):
    # TODO Add DictVectorizer and PCA to this pipeline
    MetaboliticsPipeline.steps['metabolitics-transformer'] = MetaboliticsTransformer(drug=drug_name)
    MetaboliticsPipeline.steps['metabolite-name-mapping'] = FeatureRenaming(data)
    pre = MetaboliticsPipeline([
        'metabolite-name-mapping',
        'standard-scaler',
        'metabolitics-transformer',
        'reaction-diff',
        'pathway-transformer',
        'transport-pathway-elimination',

    ])
    return pre
