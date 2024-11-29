import hydra
from omegaconf import DictConfig
import pytorch_lightning as pl
from pytorch_lightning.loggers import TensorBoardLogger
from modules.data_module import CustomDataModule
from modules.model import CustomClassifier


@hydra.main(version_base=None, config_path="conf", config_name="config")
def train(cfg: DictConfig):
    data_module = CustomDataModule(cfg.data)
    model = CustomClassifier(cfg.model)
    logger = TensorBoardLogger("logs", name="custom_model")

    trainer = pl.Trainer(
        max_epochs=10,
        logger=logger,
        log_every_n_steps=10,
    )
    trainer.fit(model, data_module)


if __name__ == "__main__":
    train()