#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import hydra
from omegaconf import OmegaConf
from os import path


def config_override(cfg):
    """Checks to see if user-defined configuration exists"""
    override_path = hydra.utils.to_absolute_path(cfg.config_override)
    if path.exists(override_path):
        override_conf = OmegaConf.load(override_path)
        cfg = OmegaConf.merge(cfg, override_conf)
    return cfg


@hydra.main(config_path="config.yaml", strict = False)
def main(cfg):
    cfg = config_override(cfg)
    print(cfg.pretty())


# this function is required to allow automatic detection of the module name when running
# from a binary script.
# it should be called from the executable script and not the hydra.main() function directly.
def entry():
    main()


if __name__ == "__main__":
    main()
