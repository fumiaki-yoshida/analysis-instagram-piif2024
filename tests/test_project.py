from importlib.metadata import metadata

import tomlkit


def test_sample():
    with open("pyproject.toml") as f:
        project_info = tomlkit.parse(f.read())
    package_info = metadata(project_info["tool"]["poetry"]["name"])
    assert package_info["Name"] == project_info["tool"]["poetry"]["name"]
