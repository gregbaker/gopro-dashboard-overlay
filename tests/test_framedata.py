import inspect
import os
from pathlib import Path

from gopro_overlay import ffmpeg
from gopro_overlay.framemeta import framemeta_from_meta
from gopro_overlay.gpmd import GoproMeta
from gopro_overlay.units import units


def load_file(path):
    return GoproMeta.parse(ffmpeg.load_gpmd_from(path))


def file_path_of_test_asset(name):
    sourcefile = Path(inspect.getfile(file_path_of_test_asset))

    meta_dir = sourcefile.parents[0].joinpath("meta")

    the_path = os.path.join(meta_dir, name)

    if not os.path.exists(the_path):
        raise IOError(f"Test file {the_path} does not exist")

    return the_path

def test_loading_data_by_frame():
    filepath = file_path_of_test_asset("hero7.mp4")
    meta = load_file(filepath)

    metameta = ffmpeg.find_streams(filepath).meta

    framemeta_from_meta(
        meta,
        metameta=metameta,
        units=units
    )
