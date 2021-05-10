# PointInPolygon

[![Build Status](https://travis-ci.com/Iceloof/PointInPolygon.svg)](https://travis-ci.com/Iceloof/PointInPolygon)
[![Coverage Status](https://coveralls.io/repos/github/Iceloof/PointInPolygon/badge.svg)](https://coveralls.io/github/Iceloof/PointInPolygon)
[![PyPI](https://img.shields.io/pypi/v/PointInPolygon)](https://pypi.org/project/PointInPolygon/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/PointInPolygon)](https://pypistats.org/packages/PointInPolygon)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/PointInPolygon)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/PointInPolygon)
![GitHub contributors](https://img.shields.io/github/contributors/Iceloof/PointInPolygon)
![GitHub issues](https://img.shields.io/github/issues-raw/Iceloof/PointInPolygon)
![GitHub Action](https://github.com/Iceloof/PointInPolygon/workflows/GitHub%20Action/badge.svg)
![GitHub](https://img.shields.io/github/license/Iceloof/PointInPolygon)

## Install
```
pip install PointInPolygon
```
or
```
pip install --upgrade PointInPolygon
```
## Usage
- Import package
```
import PointInPolygon as pnp
```
- Geometry to Array (skip steps to simplify the data and reduce the size of array)
```
pnp.Geo2Array(geo, skip=0)
```
- Check point in polygon (list or 2D tuple)
```
pnp.PointInPolygon(point, polygon)
```
