[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "s3dt"
version = "0.1.0"
description = "Reference artifact implementation of the S3DT framework"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "Apache-2.0"}
authors = [
  {name = "Kaavya Rekanar"},
  {name = "Donna O'Shea"}
]
dependencies = [
  "networkx>=3.2",
  "numpy>=1.26",
  "pydantic>=2.0",
  "PyYAML>=6.0"
]

[project.optional-dependencies]
embeddings = ["sentence-transformers>=3.0"]
dev = ["pytest>=8.0"]

[project.scripts]
s3dt = "s3dt.cli:main"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
