from main import argparse_default
from core.executer import Execute
import sys
import pytest


class TestPolyak:
    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_polyak_qmult_k_vs_all(self):
        args = argparse_default([])
        args.model = 'QMult'
        args.path_dataset_folder = 'KGs/UMLS'
        args.optim = 'Adam'
        args.num_epochs = 50
        args.batch_size = 1024
        args.lr = 0.01
        args.embedding_dim = 32
        args.input_dropout_rate = 0.0
        args.hidden_dropout_rate = 0.0
        args.feature_map_dropout_rate = 0.0
        args.scoring_technique = 'KvsAll'
        args.eval_model = 'train_val_test'
        args.read_only_few = None
        args.sample_triples_ratio = None
        args.callbacks = ['PPE']
        args.normalization = 'LayerNorm'
        args.trainer = 'torchCPUTrainer'
        result = Execute(args).start()
        assert .70 >= result['Train']['H@1'] >= 0.68
        assert 0.777 >= result['Train']['MRR'] >= 0.775
        assert 0.636 >= result['Val']['H@1'] >= 0.630
        assert 0.630 >= result['Test']['H@1'] >= 0.620
        assert result['Train']['H@10'] >= result['Train']['H@3'] >= result['Train']['H@1']
        assert result['Val']['H@10'] >= result['Val']['H@3'] >= result['Val']['H@1']
        assert result['Test']['H@10'] >= result['Test']['H@3'] >= result['Test']['H@1']
