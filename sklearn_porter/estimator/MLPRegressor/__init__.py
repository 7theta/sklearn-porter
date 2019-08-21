# -*- coding: utf-8 -*-

# scikit-learn
from sklearn.neural_network.multilayer_perceptron import \
    MLPRegressor as MLPRegressorClass

# sklearn-porter
from sklearn_porter.enums import Language, Method, Template
from sklearn_porter.estimator.EstimatorBase import EstimatorBase
from sklearn_porter.estimator.MLPClassifier import MLPClassifier
from sklearn_porter.exceptions import NotFittedEstimatorError


class MLPRegressor(MLPClassifier, EstimatorBase):
    """Extract model data and port a MLPRegressor regressor."""

    DEFAULT_LANGUAGE = Language.JS
    DEFAULT_TEMPLATE = Template.ATTACHED
    DEFAULT_METHOD = Method.PREDICT

    SUPPORT = {
        Language.JS: {
            Template.ATTACHED: {
                Method.PREDICT,
            },
        },
    }

    estimator = None  # type: MLPRegressorClass

    def __init__(self, estimator: MLPRegressorClass):

        try:
            estimator.coefs_
        except AttributeError:
            estimator_name = estimator.__class__.__qualname__
            raise NotFittedEstimatorError(estimator_name)

        super().__init__(estimator)
