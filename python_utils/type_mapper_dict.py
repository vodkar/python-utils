# -*- coding: utf-8 -*-

"""Type mapper"""

__author__ = "boombarah@gmail.com"

from collections.abc import Mapping
from typing import Dict, Type


class TypeMappingDict(Mapping):
    def __init__(self, type_dict: Dict[Type, Type]):
        self._type_dict = type_dict

    def __getitem__(self, _type: Type):
        try:
            return self._type_dict[_type]
        except KeyError:
            pass
        for t_class in _type.__subclasses__():
            try:
                return self._type_dict[t_class]
            except KeyError:
                pass
        # for built-in
        for t_class in self._type_dict.keys():
            if issubclass(_type, t_class):
                return self._type_dict[t_class]
        raise KeyError("Unmapped type %s" % _type.__name__)

    def __iter__(self):
        return iter(self._type_dict)

    def __len__(self):
        return len(self._type_dict)
