#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import ezdxf
from ezdxf import recover
from ezdxf.addons.drawing import matplotlib

def input_file_names():
  return glob.glob("./input/*.dxf")

def convert_dxf_to_png(input, output):
  try:
    dxf, auditor = recover.readfile(input)
  except IOError as ioerror:
    raise ioerror
  except ezdxf.DXFStructureError as dxf_structure_error:
    raise dxf_structure_error

  if not auditor.has_errors:
    matplotlib.qsave(dxf.modelspace(), output)

if __name__ == '__main__':
  files = input_file_names()
  for file in files:
    print(file)
    convert_dxf_to_png(file, file.replace('input', 'output').replace('dxf', 'png'))
