from pathlib import Path
import yaml
from lotr_transformer.config import Config

def test_config_parsing():
    config_path = Path("configs/default.yaml")
    assert config_path.exists()
    
    cfg_dict = yaml.safe_load(config_path.read_text())
    cfg = Config.from_dict(cfg_dict)
    
    assert cfg.data.min_freq == 2
    assert cfg.data.unk_token == "<UNK>"
    assert cfg.training.chunk_length == 128
    assert cfg.model.d_model == 256
    assert cfg.model.h == 8
